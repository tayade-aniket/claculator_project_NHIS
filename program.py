import tkinter as tk 
from tkinter import PhotoImage

SMALL_FONT = ("Arial", 16)
LARGE_FONT = ("Arial", 40, "bold")
DIGIT_FONT = ("Arial", 24, "bold")
DEFAULT_FONT = ("Arial", 20)

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("350x550")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""

        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7:(1,0), 8:(1,1), 9:(1,2),
            4:(2,0), 5:(2,1), 6:(2,2),
            1:(3,0), 2:(3,1), 3:(3,2),
            0:(4,1), '.':(4,0)
        }

        self.operations = {"/": "\u00F7", "*":"\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()
        
        for x in range(5):
            self.buttons_frame.rowconfigure(x, weight=1)
        for x in range(4):  
            self.buttons_frame.columnconfigure(x, weight=1)  

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

        self.theme = "light"
        self.create_theme_button()

    def create_theme_button(self):
        self.moon_img = PhotoImage(file="./assets/moon.png").subsample(3, 3)
        self.sun_img = PhotoImage(file="./assets/sun.png").subsample(3, 3)
        self.theme_btn = tk.Button(self.window, image=self.moon_img, bd=0, command=self.toggle_theme)
        self.theme_btn.place(x=5, y=5)

    def toggle_theme(self):
        if self.theme == "light":
            self.theme = "dark"
            self.set_dark_theme()
        else:
            self.theme = "light"
            self.set_light_theme()

    def set_dark_theme(self):
        dark_bg = "#1e1e1e"
        dark_fg = "#ffffff"
        dark_button = "#333333"
        self.window.config(bg=dark_bg)
        self.display_frame.config(bg=dark_bg)
        self.buttons_frame.config(bg=dark_bg)
        self.total_label.config(bg=dark_bg, fg=dark_fg)
        self.label.config(bg=dark_bg, fg=dark_fg)
        self.theme_btn.config(image=self.sun_img, bg=dark_bg)
        for child in self.buttons_frame.winfo_children():
            child.config(bg=dark_button, fg=dark_fg)

    def set_light_theme(self):
        light_bg = "#F5F5F5"
        light_fg = "#26265E"
        light_button = "#FFFFFF"
        self.window.config(bg=light_bg)
        self.display_frame.config(bg=light_bg)
        self.buttons_frame.config(bg=light_bg)
        self.total_label.config(bg=light_bg, fg=light_fg)
        self.label.config(bg=light_bg, fg=light_fg)
        self.theme_btn.config(image=self.moon_img, bg=light_bg)
        for child in self.buttons_frame.winfo_children():
            child.config(bg=light_button, fg=light_fg)

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))
        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg="#F5F5F5", fg="#26265E", padx=24, font=SMALL_FONT)
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg="#F5F5F5", fg="#26265E", padx=24, font=LARGE_FONT)
        label.pack(expand=True, fill="both")

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg="#F5F5F5")
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg="#FFFFFF", fg="#26265E", font=DIGIT_FONT, borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg="#F8FAFF", fg="#26265E", font=DEFAULT_FONT, borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=3, sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg="#F8FAFF", fg="#26265E", font=DEFAULT_FONT, borderwidth=0, command=self.clear)
        button.grid(row=0, column=0, sticky=tk.NSEW)

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg="#F8FAFF", fg="#26265E", font=DEFAULT_FONT, borderwidth=0, command=self.square)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg="#F8FAFF", fg="#26265E", font=DEFAULT_FONT, borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg="#CCEDFF", fg="#26265E", font=DEFAULT_FONT, borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=2, columnspan=2, sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()