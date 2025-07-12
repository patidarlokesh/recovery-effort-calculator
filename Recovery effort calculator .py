# Drawdown Recovery Calculator
# Created: 12 July 2025

"""A small Tkinter-based desktop tool that helps traders/investors
calculate the percentage gain required to recover from a given drawdown.

How it works
------------
1. The user enters a drawdown percentage (0 ≤ dd < 100).
2. On clicking **Calculate**, the app computes the recovery percentage
   using the formula:

       recovery effort in % = ((1/(1 - total drawdown/100))-1)*100

3. The result is displayed below the button.

Run
start code from here
"""


import tkinter as tk
from tkinter import ttk

# Function to calculate and display recovery needed
def calculate_and_display():
    try:
        drawdown = float(entry_drawdown.get())
        if drawdown < 0 or drawdown >= 100:
            result_label.config(text="Drawdown should be between 0 and 100")
            return
        recovery = ((1 / (1 - drawdown / 100)) - 1) * 100   # formula explain above
        result_label.config(text=f"Recovery needed: {recovery:.2f}%")
    except ValueError:
        result_label.config(text="Please enter a valid number")

# Create main window
root = tk.Tk()
root.title("Drawdown Recovery Calculator")
root.geometry("500x400")
root.resizable(False, False)

# Drawdown input
label = tk.Label(root, text="Enter Drawdown (%)", font=("Arial", 15))
label.pack(pady=10)

entry_drawdown = tk.Entry(root, font=("Arial", 15), justify="center")
entry_drawdown.pack(pady=5)

# Calculate button
calc_button = tk.Button(root, text="Calculate Recovery", font=("Arial", 15), command=calculate_and_display)
calc_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 15, "bold"))
result_label.pack(pady=10)

root.mainloop()
