from tkinter import *
import tkinter.tk as ttk
import math

class MyCalculator:
    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator")
        self.root.geometry("350x550")

        self.current = "0"
        self.new_number = True
        self.pending = None
        self.prev_operation = None
        self.prev_number = None

        self.bg_color = "#f0f0f0"
        self.number_color = "#ffffff"
        self.operator_color = "#f8f8f8"
        self.main_color = "#00000"

        self.root.configure(bg=self.bg_color)

        self.frame_making()
        self.frame_constructing()

    def frame_making(self):
        show_frame = Frame(self.root, bg=self.bg_color)
        show_frame.pack(fill=X, padx=10, pady=10)

        self.my_output = Label(show_frame, text="0", font=("Segoe UI", 26, "bold"), bg=self.bg_color, fg=self.main_color, anchor="e")
        self.my_output.pack(fill=X, pady=10)
