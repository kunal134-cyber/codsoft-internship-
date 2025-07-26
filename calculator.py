import tkinter as tk
import math

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "√":
        try:
            val = float(entry.get())
            result = math.sqrt(val)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "%":
        try:
            val = float(entry.get())
            result = val / 100
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "^":
        entry.insert(tk.END, "**")
    else:
        entry.insert(tk.END, text)

# Main window
root = tk.Tk()
root.title("Real Calculator")
root.geometry("350x500")
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, font="Arial 24", bd=10, relief=tk.SUNKEN, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button configuration
buttons = [
    ["7", "8", "9", "/", "C"],
    ["4", "5", "6", "*", "√"],
    ["1", "2", "3", "-", "%"],
    ["0", ".", "=", "+", "^"]
]

# Create button layout
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        button = tk.Button(frame, text=btn_text, font="Arial 18", relief=tk.RAISED, bd=4)
        button.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        button.bind("<Button-1>", click)

root.mainloop()

