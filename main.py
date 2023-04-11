from tkinter import *


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("計算機")

        # 設置輸入框
        self.display = Entry(master, width=25, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, pady=10)

        # 設置按鈕
        self.create_button("1", 1, 0)
        self.create_button("2", 1, 1)
        self.create_button("3", 1, 2)
        self.create_button("+", 1, 3)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("-", 2, 3)

        self.create_button("7", 3, 0)
        self.create_button("8", 3, 1)
        self.create_button("9", 3, 2)
        self.create_button("*", 3, 3)

        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("C", 4, 2)
        self.create_button("/", 4, 3)

        self.create_button("=", 5, 0, columnspan=4)

    def create_button(self, text, row, column, columnspan=1, rowspan=1):
        button = Button(self.master, text=text, width=5, height=2, font=('Arial', 16),
                        command=lambda: self.button_click(text))
        button.grid(row=row, column=column, columnspan=columnspan,
                    rowspan=rowspan, padx=5, pady=5)

    def button_click(self, text):
        if text == "C":
            self.display.delete(0, END)
        elif text == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, END)
                self.display.insert(0, "錯誤")
        else:
            self.display.insert(END, text)


root = Tk()
calculator = Calculator(root)
root.mainloop()
