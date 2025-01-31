# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter
window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# save user info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row = 0, column=0)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row = 0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row = 0, column=1)

window.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
