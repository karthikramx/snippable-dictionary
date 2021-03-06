"""
WORD POWER
Author : Karthik Ram

Credits:
+ code from SO thread: https://stackoverflow.com/questions/49901928/how-to-take-a-screenshot-with-python-using-a-click-and-drag-method-like-snipping/61603758#61603758
+ code credits to SO user: Brett Lapierre
+ pytesseract - python dictionary that perform ocr on snipper images to extract word form an image
"""

from tkinter import *
from tkinter import messagebox

import pyautogui

import datetime

import pytesseract
import pandas as pd
import pyttsx3
import os

background_color = "#fc4445"


class Application:
    def __init__(self, master):
        self.master = master
        self.rect = None
        self.x = self.y = 0
        self.start_x = None
        self.start_y = None
        self.curX = None
        self.curY = None
        self.self_word = ""
        self.engine = pyttsx3.init()
        # root.configure(background = 'red')
        # root.attributes("-transparentcolor","red")

        root.attributes("-transparent", "green")
        root.geometry('400x400+200+200')  # set new geometry
        root.title('WORD POWER')

        self.menu_frame = Frame(master, bg="#747474")
        self.menu_frame.pack(fill=X, expand=NO, side=TOP)

        self.buttonBar = Frame(self.menu_frame, bg="")
        self.buttonBar.pack(fill=BOTH, expand=NO)

        self.snipButton = Button(self.buttonBar, font=('System', 11), text="SNIP WORD",
                                 command=self.createScreenCanvas, background="#8e8d8a", fg='white')
        self.snipButton.pack(side=LEFT, expand=True)

        self.pronounce_button = Button(self.buttonBar, font=('System', 11), text="PRONOUNCE WORD",
                                       command=self.pronounce_word, background="#8e8d8a", fg='white')
        self.pronounce_button.pack(side=LEFT, expand=True)

        self.settings_button = Button(self.buttonBar, font=('System', 11), text="Settings",
                                      command=self.pronounce_word, background="#8e8d8a", fg='white')
        self.settings_button.pack(side=LEFT, expand=True)

        self.about_button = Button(self.buttonBar, font=('System', 11), text=" i ",
                                   command=self.about, background="#8e8d8a", fg='white')
        self.about_button.pack(side=LEFT, expand=True)

        self.word_info_frame = LabelFrame(master, font=('System', 11), bg=background_color, text='Word Information',
                                          borderwidth=4, fg='white')
        self.word_info_frame.pack(fill=BOTH, expand=True, side=BOTTOM)

        self.word_info_text = Text(self.word_info_frame, font=('System', 11), bg=background_color, fg='white',
                                   borderwidth=0)
        self.word_info_text.insert(INSERT,
                                   "\nWelcome user \n\nSnip any word on your screen to get its meaning")
        self.word_info_text.pack()

        self.master_screen = Toplevel(root)
        self.master_screen.withdraw()
        self.master_screen.attributes("-transparent", "blue")
        self.picture_frame = Frame(self.master_screen, background="blue")
        self.picture_frame.pack(fill=BOTH, expand=YES)

        self.dictionary = pd.read_csv('english_dictionary.csv')
        self.dictionary = self.dictionary.loc[:, ~self.dictionary.columns.str.contains('^Unnamed')]

        self.last_snipped_file = None

    def about(self):
        messagebox.showinfo("About",
                            "Created by Karthik Ram.\nFind source code:https://github.com/karthikramx/CSV-Format-English-Dictionary")

    def pronounce_word(self):
        self.engine.say(self.self_word)
        self.engine.runAndWait()

    def clear_word_info(self):
        self.word_info_text.delete("1.0", "end")

    def get_word_meaning(self, input_word):
        try:
            word_meaning = self.dictionary.loc[self.dictionary['word'] == input_word].meaning.iloc[0]
        except Exception as e:
            print("Exception :{}".format(e))
            word_meaning = "Couldn't find word meaning of {}. Please try again".format(input_word)
        return word_meaning

    def get_word_type(self, input_word):
        try:
            word_type = self.dictionary.loc[self.dictionary['word'] == input_word].wtype.iloc[0]
        except Exception as e:
            print("Exception :{}".format(e))
            word_type = "Couldn't find word type of {}. Please try again".format(input_word)
        return word_type

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
        snipped_word_path = os.getcwd() + "\\resources\\ocr\\" + self.last_snipped_file + '.png'
        self.word_power(snipped_word_path)

    def word_power(self, snipped_word_path):
        print("Snipper word path: {}".format(snipped_word_path))
        result = pytesseract.image_to_string(snipped_word_path)
        print("RESULT FROM PY-TESSERACT: {}".format(result))
        result.replace("\n", "")
        result.replace(" ", "")
        word = ''.join(e for e in result if e.isalnum())
        word = word.lower()
        print("WORD AFTER ISALNUM:{}".format(word))
        self.self_word = word
        word_meaning = self.get_word_meaning(word)
        word_meaning = word_meaning.replace(";", "\n")
        word_type = self.get_word_type(word)
        print("MEANING:\n {}".format(word_meaning))
        print("WORD TYPE: {}".format(word_type))
        meaning_data = "Meaning: {} \n\n".format(word_meaning)
        type_data = "Type: {}".format(word_type)
        self.word_info_text.insert(END, "Word: {}\n\n".format(word))
        self.word_info_text.insert(END, meaning_data)
        self.word_info_text.insert(END, type_data)

    def exit_application(self):
        print("Application exit")
        root.quit()

    def on_button_press(self, event):
        # save mouse drag start position
        self.clear_word_info()
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
