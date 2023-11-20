import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        # Membuat label untuk menampilkan angka dan tombol-tombol
        self.result_label = ttk.Label(self.master, text="0", font=("TkDefaultFont", 48))
        self.result_label.grid(row=0, column=0, columnspan=4)

        # Membuat tombol-tombol
        ttk.Button(self.master, text="7", command=lambda: self.button_click("7")).grid(row=1, column=0)
        ttk.Button(self.master, text="8", command=lambda: self.button_click("8")).grid(row=1, column=1)
        ttk.Button(self.master, text="9", command=lambda: self.button_click("9")).grid(row=1, column=2)
        ttk.Button(self.master, text="÷", command=lambda: self.button_click("÷")).grid(row=1, column=3)

        ttk.Button(self.master, text="4", command=lambda: self.button_click("4")).grid(row=2, column=0)
        ttk.Button(self.master, text="5", command=lambda: self.button_click("5")).grid(row=2, column=1)
        ttk.Button(self.master, text="6", command=lambda: self.button_click("6")).grid(row=2, column=2)
        ttk.Button(self.master, text="×", command=lambda: self.button_click("×")).grid(row=2, column=3)

        ttk.Button(self.master, text="1", command=lambda: self.button_click("1")).grid(row=3, column=0)
        ttk.Button(self.master, text="2", command=lambda: self.button_click("2")).grid(row=3, column=1)
        ttk.Button(self.master, text="3", command=lambda: self.button_click("3")).grid(row=3, column=2)
        ttk.Button(self.master, text="-", command=lambda: self.button_click("-")).grid(row=3, column=3)

        ttk.Button(self.master, text="0", command=lambda: self.button_click("0")).grid(row=4, column=0)
        ttk.Button(self.master, text=".", command=lambda: self.button_click(".")).grid(row=4, column=1)
        ttk.Button(self.master, text="C", command=self.clear).grid(row=4, column=2)
        ttk.Button(self.master, text="+", command=lambda: self.button_click("+")).grid(row=4, column=3)

        ttk.Button(self.master, text="=", command=self.calculate).grid(row=5, column=0, columnspan=4)

        self.current_num = ""
        self.current_op = ""
        self.new_num = True

    def button_click(self, value):
        if value in "0123456789.":
            if self.new_num:
                self.current_num = ""
                self.new_num = False
            self.current_num += value
            self.result_label.config(text=self.current_num)
        else:
            self.calculate()
            self.current_op = value

    def clear(self):
        self.current_num = ""
        self.current_op = ""
        self.new_num = True
        self.result_label.config(text="0")

    def calculate(self):
        if self.current_op == "+":
            result = float(self.current_num) + float(self.result_label["text"])
        elif self.current_op == "-":
            result = float(self.result_label
            ["text"]) - float(self.current_num)
        elif self.current_op == "×":
            result = float(self.current_num) * float(self.result_label["text"])
        elif self.current_op == "÷":
            result = float(self.result_label["text"]) / float(self.current_num)
        else:
            result = float(self.current_num)
        self.current_num = str(result)
        self.result_label.config(text=self.current_num)
        self.new_num = True
        
root = tk.Tk()
calc = Calculator(root)
root.mainloop()

