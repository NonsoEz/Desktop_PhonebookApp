import sys
import os
import tkinter as tk   #-- This is for python 3.x and above
from MyPy import MyPy

win = tk.Tk()
win.title("Lookup Number")

search_entry_number = tk.IntVar()
search_entry = tk.Entry(win, width=20, textvariable=search_entry_number)
search_entry.grid(column=0, row=0, padx=10, pady=10)

def LookupContact(phone_number):
    print(phone_number)


search_button = tk.Button(win, text="Search", command=lambda: LookupContact(search_entry_number.get()))
search_button.grid(column=0, row=1, padx=10, pady=10)

result_sheet = tk.Label(win, width=10, height=5)
result_sheet.grid(column=0, row=3, padx=10, pady=10)
result_sheet.grid_forget()

win.mainloop()