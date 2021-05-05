"""
creating a DataFrame
row containing the words
columns containing the user_id
"""

import pandas as pd

users_data = {'karthikram570':pd.Series(data = ['meaning x','meaning a','meaning c'], index = ['word x','word a','word c']),
              'karthikram571':pd.Series(data = ['meaning x', 'meaning f','meaing w'], index = ['word x','word f','word w'])}

data_frame = pd.DataFrame(users_data)

print(data_frame)
