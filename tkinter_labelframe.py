import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
# import menubar_
from tkinter import Menu

win = tk.Tk()
win.title("Second Tkinter GUI *LABEL FRAMES*")

menu_bar = Menu(win)
win.config(menu=menu_bar)

def quit_():
	win.quit()
	win.destroy()
	exit()

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit_)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Help")
help_menu.add_command(label="About")

tab_controller = ttk.Notebook(win)
tab_1 = ttk.Frame(tab_controller)
tab_controller.add(tab_1, text="Packages")
tab_controller.pack()

tab_2 = ttk.Frame(tab_controller)
tab_controller.add(tab_2, text="Feedback")
tab_controller.pack(fill="both", expand=1)

package_labelframe = ttk.LabelFrame(tab_1, text="Package Management")
package_labelframe.grid(column=0, row=0, padx=10, pady=5, sticky="WE")

feedback_labelframe = ttk.LabelFrame(tab_2, text="Feedback and Response")
feedback_labelframe.grid(column=0, row=0, padx=10, pady=5)

def button_clicked():
	submit_button.configure(text="Submitted")

""" Feedback_labelframe Related Code"""
name_label = ttk.Label(feedback_labelframe, text="Name")
name_label.grid(column=0, row=0, sticky="W")

country_label = ttk.Label(feedback_labelframe, text="Country")
country_label.grid(column=1, row=0)

name_return = tk.StringVar()
name_entry = ttk.Entry(feedback_labelframe, width=25, textvariable=name_return)
name_entry.grid(column=0, row=1, sticky="W")

name_label = ttk.Label(feedback_labelframe, text="Name")
name_label.grid(column=0, row=0, sticky="W")

choice_country = tk.StringVar()
country_chosen = ttk.Combobox(feedback_labelframe, width=20,textvariable=choice_country)
country_chosen["values"] = ("Kenya","Uganda","Rwanda","Tanzania","Burundi","Other")
country_chosen.grid(column=1, row=1, sticky="W")
country_chosen.current(0)

submit_button = ttk.Button(feedback_labelframe, text="Submit", width=10,
						   command=button_clicked)
submit_button.grid(column=2, row=1, sticky="w")

xlen=40
ylen=4
scrolled_textbar = scrolledtext.ScrolledText(feedback_labelframe, width=xlen,
height=ylen, wrap=tk.WORD)
scrolled_textbar.grid(columnspan=3, row=3, sticky="WE")

""" package_labelframe Related Code """
basic_pack = tk.IntVar()
basic_pack_chckbtn = tk.Checkbutton(package_labelframe, text="Basic Package",
variable=basic_pack, state="disabled")
basic_pack_chckbtn.select()
basic_pack_chckbtn.grid(column=0, row=2, sticky="W")
'''
bsc = basic_pack.get()
print(bsc)
'''
advanced_pack = tk.IntVar()
advanced_pack_chckbtn = tk.Checkbutton(package_labelframe, text="Advanced Package",
variable=advanced_pack)
advanced_pack_chckbtn.grid(column=1, row=2, sticky="W")
'''
adv = advanced_pack.get()
print(adv)
'''

custom_pack = tk.IntVar()
custom_package = tk.Checkbutton(package_labelframe, text="Custom Package",
variable=custom_pack)
custom_package.grid(column=2, row=2)

content_labelframe = ttk.LabelFrame(package_labelframe, text="Package Contents")
content_labelframe.grid(column=0, row=4, padx=10, pady=5)

if basic_pack.get() == 1:
	ttk.Label(content_labelframe, text="Content 1").grid(column=0, row=0)
	ttk.Label(content_labelframe, text="Content 2").grid(column=0, row=1)

win.mainloop()
