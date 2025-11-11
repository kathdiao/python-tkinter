import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("TO DO List")
root.geometry("1000x700")

tk.Label(root, text="TO DO List", font=("Arial", 20, "bold")).pack(pady=20)

def end():
    messagebox.askyesno("Exit Confirmation", "Are you sure you want to exit?")
    root.destroy()

exit_btn = tk.Button(root,  text="x", command=end, font=("Arial", 10), bg="red", fg="white")
exit_btn.place(x=950, y=10)

task_count = 0

def add():
    global task_count
    task = entry.get()
    if task != "":
        task_count += 1
        textbox.insert(tk.END, f"{task_count}. {task}\n")
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# one line text box
entry = tk.Entry(root, font=("Arial", 20))
entry.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.columnconfigure(0, weight=1)

btn1 = tk.Button(button_frame, text="Add",font=("Arial", 15), command=add)
btn1.grid(row=1, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(button_frame, text="View", font=("Arial", 15))
btn2.grid(row=1, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(button_frame, text="Edit", font=("Arial", 15))
btn3.grid(row=1, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(button_frame, text="Delete", font=("Arial", 15))
btn4.grid(row=1, column=3, sticky=tk.W+tk.E)

button_frame.pack(padx=20, pady=20)

# Multi line text box
textbox = tk.Text(root, height=17,width=80, font=("Arial", 15))
textbox.pack()

root.mainloop()