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

title_label = tkinter.Label(user_info_frame, text = "Sector")
title_combobox = ttk.Combobox(user_info_frame, values=["Technology", "Financial Services", "Consumer Cyclical", "Healthcare", "Communication Services", "Industrials", "Consumer Defensive", "Energy", "Basic Materials", "Real Estate", "Utilities"])
title_label.grid(row= 4, column=0)
title_combobox.grid(row=5, column=0)

age_label = tkinter.Label(user_info_frame, text = "Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_ = 18, to = 110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row = 1, column=0, sticky="news", pady=20, padx=20)

registered_label = tkinter.Label(courses_frame, text="Registration Status")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered")
registered_label.grid(row = 0, column=0)
registered_check.grid(row =1, column=0)

numcourses_label = tkinter.Label(courses_frame, text="# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numcourses_label.grid(row = 0, column=1)
numcourses_spinbox.grid(row = 1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text="# Semesters")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numsemesters_label.grid(row = 0, column=2)
numsemesters_spinbox.grid(row = 1, column=2)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

terms_frame = tkinter.LabelFrame(frame, text="Terms and Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20)

terms_check = tkinter.Checkbutton(terms_frame, text="I accept the Terms and Conditions")
terms_check.grid(row=0, column=0)

window.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
