from tkinter import *
import pyautogui

import datetime

import pytesseract
import pandas as pd




class Application():
    def __init__(self, master):
        self.master = master
        self.rect = None
        self.x = self.y = 0
        self.start_x = None
        self.start_y = None
        self.curX = None
        self.curY = None

        # root.configure(background = 'red')
        # root.attributes("-transparentcolor","red")

        root.attributes("-transparent", "blue")
        root.geometry('400x50+200+200')  # set new geometry
        root.title('Lil Snippy')
        self.menu_frame = Frame(master, bg="blue")
        self.menu_frame.pack(fill=BOTH, expand=YES)

        self.buttonBar = Frame(self.menu_frame, bg="")
        self.buttonBar.pack(fill=BOTH, expand=YES)

        self.snipButton = Button(self.buttonBar, width=3, command=self.createScreenCanvas, background="green")
        self.snipButton.pack(expand=YES)

        self.master_screen = Toplevel(root)
        self.master_screen.withdraw()
        self.master_screen.attributes("-transparent", "blue")
        self.picture_frame = Frame(self.master_screen, background="blue")
        self.picture_frame.pack(fill=BOTH, expand=YES)

        self.dictionary = pd.read_csv('english_dictionary.csv')
        self.dictionary = self.dictionary.loc[:, ~self.dictionary.columns.str.contains('^Unnamed')]

        self.last_snipped_file = None

    def get_word_meaning(self, input_word):
        return self.dictionary.loc[self.dictionary['word'] == input_word].meaning.iloc[0]

    def get_word_type(self, input_word):
        return self.dictionary.loc[self.dictionary['word'] == input_word].wtype.iloc[0]

    def takeBoundedScreenShot(self, x1, y1, x2, y2):
        im = pyautogui.screenshot(region=(x1, y1, x2, y2))
        x = datetime.datetime.now()
        fileName = x.strftime("%f")
        im.save("resources/OCR/" + fileName + ".png")
        self.last_snipped_file = fileName
        print("Snipped file name: {}".format(fileName))


    def createScreenCanvas(self):
        self.master_screen.deiconify()
        root.withdraw()

        self.screenCanvas = Canvas(self.picture_frame, cursor="cross", bg="grey11")
        self.screenCanvas.pack(fill=BOTH, expand=YES)

        self.screenCanvas.bind("<ButtonPress-1>", self.on_button_press)
        self.screenCanvas.bind("<B1-Motion>", self.on_move_press)
        self.screenCanvas.bind("<ButtonRelease-1>", self.on_button_release)

        self.master_screen.attributes('-fullscreen', True)
        self.master_screen.attributes('-alpha', .3)
        self.master_screen.lift()
        self.master_screen.attributes("-topmost", True)

    def on_button_release(self, event):
        self.recPosition()

        if self.start_x <= self.curX and self.start_y <= self.curY:
            print("right down")
            self.takeBoundedScreenShot(self.start_x, self.start_y, self.curX - self.start_x, self.curY - self.start_y)

        elif self.start_x >= self.curX and self.start_y <= self.curY:
            print("left down")
            self.takeBoundedScreenShot(self.curX, self.start_y, self.start_x - self.curX, self.curY - self.start_y)

        elif self.start_x <= self.curX and self.start_y >= self.curY:
            print("right up")
            self.takeBoundedScreenShot(self.start_x, self.curY, self.curX - self.start_x, self.start_y - self.curY)

        elif self.start_x >= self.curX and self.start_y >= self.curY:
            print("left up")
            self.takeBoundedScreenShot(self.curX, self.curY, self.start_x - self.curX, self.start_y - self.curY)

        self.exitScreenshotMode()
        return event

    def exitScreenshotMode(self):
        print("Screenshot mode exited")
        self.screenCanvas.destroy()
        self.master_screen.withdraw()
        root.deiconify()
        snipped_word_path = 'C:/Users/karthik/Desktop/CSV-Format-English-Dictionary/resources/OCR/' + self.last_snipped_file + '.png'
        print("Snipper word path: {}".format(snipped_word_path))

        result = pytesseract.image_to_string(snipped_word_path)
        print("RESULT FROM PY-TESSERACT: {}".format(result))
        result.replace("\n", "")
        result.replace(" ", "")
        word = result.capitalize()
        word = ''.join(e for e in word if e.isalnum())
        print("WORD: {}".format(word))

        meaning = self.get_word_meaning(word)
        meaning = meaning.replace(";", "\n")
        type = self.get_word_type(word)

        print("MEANING:\n {}".format(meaning))
        print("WORD TYPE: {}".format(type))

    def exit_application(self):
        print("Application exit")
        root.quit()

    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = self.screenCanvas.canvasx(event.x)
        self.start_y = self.screenCanvas.canvasy(event.y)

        self.rect = self.screenCanvas.create_rectangle(self.x, self.y, 1, 1, outline='red', width=3, fill="blue")

    def on_move_press(self, event):
        self.curX, self.curY = (event.x, event.y)
        # expand rectangle as you drag the mouse
        self.screenCanvas.coords(self.rect, self.start_x, self.start_y, self.curX, self.curY)

    def recPosition(self):
        print(self.start_x)
        print(self.start_y)
        print(self.curX)
        print(self.curY)


if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    root.mainloop()
