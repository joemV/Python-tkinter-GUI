import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.title("Second Tkinter GUI *LABEL FRAMES*")

main_labelframe = ttk.LabelFrame(win, text="Label Frame",)
main_labelframe.grid(column=0, row=0, padx=10, pady=5)

def button_clicked():
	submit_button.configure(text="Submitted")

name_label = ttk.Label(main_labelframe, text="Name", width=15)
name_label.grid(column=0, row=0, sticky="W")

choice_country = tk.StringVar()
country_chosen = ttk.Combobox(main_labelframe, width=15, textvariable=choice_country)
country_chosen["values"] = ("Kenya","Ugande","Rwanda","Tanzania","Burundi","Other")
country_chosen.grid(column=1, row=0, sticky="W")
country_chosen.current(0)

submit_button = ttk.Button(main_labelframe, text="Submit", width=10,
						   command=button_clicked)
submit_button.grid(column=2, row=0, sticky="w")

basic_pack = tk.IntVar()
basic_pack_chckbtn = tk.Checkbutton(main_labelframe, text="Basic Package", variable=basic_pack, state="disabled")
basic_pack_chckbtn.select()
basic_pack_chckbtn.grid(column=0, row=1, sticky="W")

advanced_pack = tk.IntVar()
advanced_pack_chckbtn = tk.Checkbutton(main_labelframe, text="Advanced Package", variable=advanced_pack)
advanced_pack_chckbtn.grid(column=1, row=1, sticky="W")

win.mainloop()
