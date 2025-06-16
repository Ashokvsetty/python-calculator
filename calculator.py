import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        # Variables
        self.current = "0"
        self.previous = ""
        self.operator = ""
        self.total = 0
        
        # Create display
        self.create_display()
        
        # Create buttons
        self.create_buttons()
    
    def create_display(self):
        """Create the calculator display"""
        self.display_frame = tk.Frame(self.root, bg="black")
        self.display_frame.pack(expand=True, fill="both")
        
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        
        self.display = tk.Label(
            self.display_frame,
            textvariable=self.display_var,
            font=("Arial", 24, "bold"),
            bg="black",
            fg="white",
            anchor="e",
            padx=10
        )
        self.display.pack(expand=True, fill="both")
    
    def create_buttons(self):
        """Create calculator buttons"""
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(expand=True, fill="both")
        
        # Button layout
        buttons = [
            ['C', '±', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '']
        ]
        
        # Button colors
        colors = {
            'number': {'bg': '#505050', 'fg': 'white'},
            'operator': {'bg': '#FF9500', 'fg': 'white'},
            'function': {'bg': '#A6A6A6', 'fg': 'black'},
            'equals': {'bg': '#FF9500', 'fg': 'white'}
        }
        
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                if text == '':
                    continue
                    
                # Determine button type and color
                if text in ['C', '±', '%']:
                    color = colors['function']
                elif text in ['÷', '×', '-', '+']:
                    color = colors['operator']
                elif text == '=':
                    color = colors['equals']
                else:
                    color = colors['number']
                
                # Special handling for 0 button (spans 2 columns)
                if text == '0':
                    btn = tk.Button(
                        self.button_frame,
                        text=text,
                        font=("Arial", 18, "bold"),
                        command=lambda t=text: self.button_click(t),
                        **color
                    )
                    btn.grid(row=i, column=j, columnspan=2, sticky="nsew", padx=1, pady=1)
                else:
                    btn = tk.Button(
                        self.button_frame,
                        text=text,
                        font=("Arial", 18, "bold"),
                        command=lambda t=text: self.button_click(t),
                        **color
                    )
                    btn.grid(row=i, column=j, sticky="nsew", padx=1, pady=1)
        
        # Configure grid weights for responsive design
        for i in range(5):
            self.button_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.button_frame.grid_columnconfigure(j, weight=1)
    
    def button_click(self, char):
        """Handle button clicks"""
        try:
            if char.isdigit():
                self.number_press(char)
            elif char == '.':
                self.decimal_press()
            elif char in ['÷', '×', '-', '+']:
                self.operator_press(char)
            elif char == '=':
                self.equals_press()
            elif char == 'C':
                self.clear_press()
            elif char == '±':
                self.sign_press()
            elif char == '%':
                self.percent_press()
        except Exception as e:
            messagebox.showerror("Error", "Invalid operation")
            self.clear_press()
    
    def number_press(self, num):
        """Handle number button presses"""
        if self.current == "0":
            self.current = num
        else:
            self.current += num
        self.update_display()
    
    def decimal_press(self):
        """Handle decimal point button press"""
        if '.' not in self.current:
            self.current += '.'
            self.update_display()
    
    def operator_press(self, op):
        """Handle operator button presses"""
        if self.operator and self.previous:
            self.equals_press()
        
        self.previous = self.current
        self.current = "0"
        self.operator = op
    
    def equals_press(self):
        """Handle equals button press"""
        if self.operator and self.previous:
            try:
                # Convert display symbols to calculation symbols
                op_map = {'÷': '/', '×': '*', '-': '-', '+': '+'}
                calc_op = op_map.get(self.operator, self.operator)
                
                # Perform calculation
                result = eval(f"{self.previous} {calc_op} {self.current}")
                
                # Handle division by zero
                if calc_op == '/' and float(self.current) == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                
                # Format result
                if result == int(result):
                    self.current = str(int(result))
                else:
                    self.current = str(round(result, 10))
                
                self.operator = ""
                self.previous = ""
                self.update_display()
                
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero")
                self.clear_press()
            except:
                messagebox.showerror("Error", "Invalid calculation")
                self.clear_press()
    
    def clear_press(self):
        """Handle clear button press"""
        self.current = "0"
        self.previous = ""
        self.operator = ""
        self.total = 0
        self.update_display()
    
    def sign_press(self):
        """Handle plus/minus button press"""
        if self.current != "0":
            if self.current.startswith('-'):
                self.current = self.current[1:]
            else:
                self.current = '-' + self.current
            self.update_display()
    
    def percent_press(self):
        """Handle percent button press"""
        try:
            result = float(self.current) / 100
            if result == int(result):
                self.current = str(int(result))
            else:
                self.current = str(result)
            self.update_display()
        except:
            messagebox.showerror("Error", "Invalid operation")
    
    def update_display(self):
        """Update the calculator display"""
        # Limit display length
        display_text = self.current
        if len(display_text) > 12:
            try:
                # Try to format as scientific notation for very large numbers
                num = float(display_text)
                display_text = f"{num:.6e}"
            except:
                display_text = display_text[:12]
        
        self.display_var.set(display_text)

def main():
    """Main function to run the calculator"""
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()

