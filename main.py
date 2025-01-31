# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter
from tkinter import ttk
window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# save user info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row = 0, column=0, padx=20, pady=20)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row = 0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row = 0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text = "Title")
title_combobox = ttk.Combobox(user_info_frame, values=["Technology", "Financial Services", "Consumer Cyclical", "Healthcare", "Communication Services", "Industrials", "Consumer Defensive", "Energy", "Basic Materials", "Real Estate", "Utilities"])
title_label.grid(row= 0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text = "Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_ = 18, to = 110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

window.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
