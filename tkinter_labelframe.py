import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import menubar_
from tkinter import Menu

win = tk.Tk()
win.title("Second Tkinter GUI *LABEL FRAMES*")

main_labelframe = ttk.LabelFrame(win, text="Label Frame",)
main_labelframe.grid(column=0, row=0, padx=10, pady=5)

def button_clicked():
	submit_button.configure(text="Submitted")
  

name_label = ttk.Label(main_labelframe, text="Name")
name_label.grid(column=0, row=0, sticky="W")

country_label = ttk.Label(main_labelframe, text="Country")
country_label.grid(column=1, row=0)

name_return = tk.StringVar()
name_entry = ttk.Entry(main_labelframe, width=20, textvariable=name_return)
name_entry.grid(column=0, row=1, sticky="W")

name_label = ttk.Label(main_labelframe, text="Name", width=15)
name_label.grid(column=0, row=0, sticky="W")

choice_country = tk.StringVar()
country_chosen = ttk.Combobox(main_labelframe, width=15,textvariable=choice_country)
country_chosen["values"] = ("Kenya","Ugande","Rwanda","Tanzania","Burundi","Other")
country_chosen.grid(column=1, row=0, sticky="W")
country_chosen.current(0)

submit_button = ttk.Button(main_labelframe, text="Submit", width=10,
						   command=button_clicked)

submit_button.grid(column=2, row=1, sticky="w")

basic_pack = tk.IntVar()
basic_pack_chckbtn = tk.Checkbutton(main_labelframe, text="Basic Package",variable=basic_pack, state="disabled")
basic_pack_chckbtn.select()
basic_pack_chckbtn.grid(column=0, row=2, sticky="W")
'''
bsc = basic_pack.get()
print(bsc)
'''
advanced_pack = tk.IntVar()
advanced_pack_chckbtn = tk.Checkbutton(main_labelframe, text="Advanced Package",variable=advanced_pack)
advanced_pack_chckbtn.grid(column=1, row=2, sticky="W")
'''
adv = advanced_pack.get()
print(adv)
'''

xlen=40
ylen=4
scrolled_textbar = scrolledtext.ScrolledText(main_labelframe, width=xlen,
height=ylen, wrap=tk.WORD)
scrolled_textbar.grid(columnspan=3, row=3)


Menu_Bar = Menu(win)
win.config(menu=Menu_Bar)

def _exit():
	win.quit()
	exit()

file_menu = Menu(Menu_Bar, tearoff=0)
Menu_Bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_exit)

help_menu = Menu(Menu_Bar, tearoff=0)
Menu_Bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About")
help_menu.add_command(label="Help")

win.mainloop()
