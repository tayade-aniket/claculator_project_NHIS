from tkinter import *
from tkinter import ttk
import math

class MyCalculator:
    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator")
        self.root.geometry("350x650")

        self.current = "0"
        self.new_number = True
        self.op_pending = None
        self.prev_operation = None
        self.prev_number = None

        self.bg_color = "#f0f0f0"
        self.number_color = "#ffffff"
        self.operator_color = "#f8f8f8"
        self.main_color = "#000000"

        self.root.configure(bg=self.bg_color)

        self.frame_making()
        self.frame_constructing()

    def frame_making(self):
        show_frame = Frame(self.root, bg=self.bg_color)
        show_frame.pack(fill=X, padx=10, pady=10)

        self.my_output = Label(show_frame, text="0", font=("Segoe UI", 26, "bold"), bg=self.bg_color, fg=self.main_color, anchor="e")
        self.my_output.pack(fill=X, pady=10)

        self.my_buttons_frame = Frame(self.root, bg=self.bg_color)
        self.my_buttons_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        my_buttons_data = [
            ['%', '√', 'x²', '1/x'],
            ['CE', 'C', '⌫', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['±', '0', '.', '=']
        ]

        for row_data in my_buttons_data:
            frame = Frame(self.my_buttons_frame, bg=self.bg_color)
            frame.pack(fill=X, expand=True, pady=2)
            for text in row_data:
                self.generate_main_button(frame, text)

    def generate_main_button(self, parent, text):
        if text in '0123456789':
            result = lambda: self.numer_click(text)
            color = self.number_color
            font_weight = "bold"
        elif text in '+-x÷':
            result = lambda: self.operation(text)
            color = self.operator_color
            font_weight = "normal"
        else:
            result = lambda: self.unique_function(text)
            color = self.operator_color
            font_weight = "normal"
        
        my_btn = Button(parent, text=text, relief="flat", bg=color, fg=self.main_color, font=("Segoe UI", 16, font_weight), width=5, height=2, command=result)
        my_btn.pack(side=LEFT, padx=2, pady=2, expand=True, fill=BOTH)

    def numer_click(self, num):
        if self.new_number:
            self.current = num
            self.new_number = False
        else:
            if num == '.' and '.' in self.current:
                return
            self.current += num
        self.update_display()

    def operation(self, oper):
        if self.current == "Error":
            self.current = "0"

        if not self.new_number:
            self.calculator()  # Corrected method name
            self.new_number = True

        self.op_pending = oper

        try:
            self.prev_number = float(self.current)
        except ValueError:
            self.prev_number = 0  # Default to 0 if conversion fails


    def calculator(self):
        if self.op_pending and self.prev_number is not None:
            try:
                current = float(self.current)
                if self.oper_pending == '+':
                    output = self.prev_number + current
                elif self.op_pending == '-':
                    output = self.prev_number - current
                elif self.op_pending == 'x':
                    output = self.prev_number * current
                elif self.op_pending == '÷':
                    if current == 0:
                        self.current = "Error"
                        self.update_display()
                        return
                    output = self.prev_number / current

                self.current = str(output)
                self.op_pending = None
                self.update_display()
            except:
                self.current = "Error"
                self.update_display()

    def unique_function(self, func):
        if func == 'C' or func == 'CE':
            self.current = "0"
            self.new_number = True
            self.op_pending = None
            self.prev_number = None
        elif func == '⌫':
            if not self.new_number:
                self.current = self.current[:-1]
                if not self.current:
                    self.current = "0"
                    self.new_number = True
        elif func == '=':
            self.calculator()
        elif func == '±':
            if self.current != "0":
                if self.current.startswith('-'):
                    self.current = self.current[1:]
                else:
                    self.current = '-' + self.current
        elif func == '%':
            try:
                self.current = str(float(self.current) / 100)
            except:
                self.current = "Error"
        elif func == '√':
            try:
                self.current = str(math.sqrt(float(self.current)))
            except:
                self.current = "Error"
        elif func == 'x²':
            try:
                self.current = str(float(self.current) ** 2)
            except:
                self.current = "Error"
        elif func == '1/x':
            try: 
                self.current = str(1 / float(self.current))
            except:
                self.current = "Error"
        self.update_display()

    def update_display(self):
        if self.current.endswith('.0'):
            self.current = self.current[:-2]
        self.my_output.config(text=self.current)

    def frame_constructing(self):
        self.root.bind('<Key>', self.key_press)

    def key_press(self, event):
        key = event.char
        if key in '0123456789.':
            self.number_press(key)
        elif key in '+-*/':
            op = 'x' if key == '*' else '÷' if key == '/' else key
            self.operation(op)
        elif key == '\r':
            self.unique_function("=")
        elif key == '\x08':
            self.unique_function('⌫')
        elif key == '\x1b':
            self.unique_function('C')

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    calc = MyCalculator()
    calc.run()

