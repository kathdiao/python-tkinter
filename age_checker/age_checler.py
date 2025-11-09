import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Age Checker")
root.geometry("600x300")

label = tk.Label(root, text="Enter your age:", font=("Arial", 15))
label.pack(pady=10)

entry_age = tk.Entry(root, width=20, font=("Arial", 20))
entry_age.pack(pady=10,)

def check_age():
    age_text = entry_age.get()
    if age_text.isdigit():
        age = int(age_text)
        if age >= 18:
            messagebox.showinfo("Result", "You are an adult!")
        else:
            messagebox.showinfo("Result", "You are a minor!")
    else:
        messagebox.showwarning("Invalid input", "Please enter a valid number")

button = tk.Button(root, text="Check Age", command=check_age, font=("Arial", 13))
button.pack(pady=10)

root.mainloop()
