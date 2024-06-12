import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.result_var = tk.StringVar()
        self.reset_display = False  # Flag to indicate when to reset the display

        self.create_widgets()
        self.bind_keys()

    def create_widgets(self):
        # Display
        self.display = tk.Entry(
            self.root,
            textvariable=self.result_var,
            font=('Arial', 20),
            bd=10,
            insertwidth=2,
            width=14,
            borderwidth=4,
            state='readonly'
        )
        self.display.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0
        for char in buttons:
            button = tk.Button(self.root, text=char, padx=20, pady=20, font=('Arial', 18),
                               command=lambda ch=char: self.on_button_click(ch))
            button.grid(row=row, column=col, sticky="nsew")

            col += 1
            if col > 3:
                col = 0
                row += 1

        # Clear button
        clear_button = tk.Button(self.root, text='C', padx=20, pady=20, font=('Arial', 18),
                                 command=lambda: self.on_button_click('C'))
        clear_button.grid(row=row, column=col, sticky="nsew")

        # Backspace button
        backspace_button = tk.Button(self.root, text='⌫', padx=20, pady=20, font=('Arial', 18),
                                     command=self.on_backspace_click)
        backspace_button.grid(row=row, column=col + 1, sticky="nsew")

        # CE button
        ce_button = tk.Button(self.root, text='CE', padx=20, pady=20, font=('Arial', 18),
                              command=lambda: self.on_button_click('CE'))
        ce_button.grid(row=row, column=col + 2, sticky="nsew")

        # Enter button
        enter_button = tk.Button(self.root, text='Enter', padx=20, pady=20, font=('Arial', 18),
                                 command=lambda: self.on_button_click('='))
        enter_button.grid(row=row, column=col + 3, sticky="nsew")

        for i in range(1, 5):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i-1, weight=1)

    def bind_keys(self):
        # Bind number keys and operators
        for key in '0123456789/*-+.':
            self.root.bind(f'<KeyPress-{key}>', self.on_keypress)

        # Bind Enter key for evaluation
        self.root.bind('<Return>', lambda event: self.on_button_click('='))

        # Bind numpad keys
        self.root.bind('<KP_0>', lambda event: self.on_button_click('0'))
        self.root.bind('<KP_1>', lambda event: self.on_button_click('1'))
        self.root.bind('<KP_2>', lambda event: self.on_button_click('2'))
        self.root.bind('<KP_3>', lambda event: self.on_button_click('3'))
        self.root.bind('<KP_4>', lambda event: self.on_button_click('4'))
        self.root.bind('<KP_5>', lambda event: self.on_button_click('5'))
        self.root.bind('<KP_6>', lambda event: self.on_button_click('6'))
        self.root.bind('<KP_7>', lambda event: self.on_button_click('7'))
        self.root.bind('<KP_8>', lambda event: self.on_button_click('8'))
        self.root.bind('<KP_9>', lambda event: self.on_button_click('9'))
        self.root.bind('<KP_Decimal>', lambda event: self.on_button_click('.'))
        self.root.bind('<KP_Divide>', lambda event: self.on_button_click('/'))
        self.root.bind('<KP_Multiply>', lambda event: self.on_button_click('*'))
        self.root.bind('<KP_Subtract>', lambda event: self.on_button_click('-'))
        self.root.bind('<KP_Add>', lambda event: self.on_button_click('+'))

        # Bind Escape key for clear
        self.root.bind('<Escape>', lambda event: self.on_button_click('C'))

        # Bind Backspace key
        self.root.bind('<BackSpace>', lambda event: self.on_backspace_click())

    def on_keypress(self, event):
        if event.char in '0123456789/*-+.':
            self.on_button_click(event.char)
            return "break"  # Prevent the default behavior

    def on_button_click(self, char):
        if self.reset_display and char not in '/*-+.':
            self.result_var.set("")
            self.reset_display = False

        if char == '=':
            try:
                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
                self.reset_display = True
            except Exception as e:
                self.result_var.set("Error")
        elif char == 'C':
            self.result_var.set("")
            self.reset_display = False
        elif char == 'CE':
            self.result_var.set("")
        else:
            if self.reset_display and char in '/*-+':
                self.reset_display = False

            current_text = self.result_var.get()
            new_text = current_text + char
            self.result_var.set(new_text)

    def on_backspace_click(self):
        current_text = self.result_var.get()
        new_text = current_text[:-1]  # Remove the last character
        self.result_var.set(new_text)


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
