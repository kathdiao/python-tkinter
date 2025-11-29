import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("TO DO List")
root.geometry("1000x700")

tk.Label(root, text="TO DO List", font=("Arial", 20, "bold")).pack(pady=20)

def end():
    confirm = messagebox.askyesno("Exit Confirmation", "Are you sure you want to exit?")
    if confirm:
        root.destroy()

exit_btn = tk.Button(root, text="x", command=end, font=("Arial", 10), bg="red", fg="white")
exit_btn.place(x=950, y=10)

tasks = []
def refresh_textbox():
    textbox.delete("1.0", tk.END)
    for i, task in enumerate(tasks, start=1):
        textbox.insert(tk.END, f"{i}. {task}\n")

def add():
    task = entry.get().strip()
    if task:
        tasks.append(task)
        refresh_textbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def view():
    if not tasks:
        messagebox.showinfo("Tasks", "No tasks available.")
    else:
        refresh_textbox()

def edit():
    try:
        index = int(entry.get()) - 1
        if 0 <= index < len(tasks):
            new_task = simple_input("Edit Task", "Enter new task:")
            if new_task:
                tasks[index] = new_task
                refresh_textbox()
        else:
            messagebox.showerror("Error", "Invalid task number.")
    except:
        messagebox.showinfo("Info", "Enter the task number to edit in the box.")

def delete():
    try:
        index = int(entry.get()) - 1
        if 0 <= index < len(tasks):
            confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this task?")
            if confirm:
                tasks.pop(index)
                refresh_textbox()
                entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Invalid task number.")
    except:
        messagebox.showinfo("Info", "Enter the task number to delete in the box.")

def simple_input(title, prompt):
    popup = tk.Toplevel(root)
    popup.title(title)
    popup.geometry("300x150")

    tk.Label(popup, text=prompt, font=("Arial", 12)).pack(pady=10)

    inp = tk.Entry(popup, font=("Arial", 12))
    inp.pack(pady=5)

    def submit():
        popup.value = inp.get()
        popup.destroy()

    tk.Button(popup, text="OK", command=submit).pack(pady=5)

    popup.wait_window()
    return getattr(popup, "value", None)


entry = tk.Entry(root, font=("Arial", 20))
entry.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.columnconfigure(0, weight=1)

btn1 = tk.Button(button_frame, text="Add", font=("Arial", 15), width=10, command=add)
btn1.grid(row=1, column=0, padx=5)

btn2 = tk.Button(button_frame, text="View", font=("Arial", 15), width=10, command=view)
btn2.grid(row=1, column=1, padx=5)

btn3 = tk.Button(button_frame, text="Edit", font=("Arial", 15), width=10, command=edit)
btn3.grid(row=1, column=2, padx=5)

btn4 = tk.Button(button_frame, text="Delete", font=("Arial", 15), width=10, command=delete)
btn4.grid(row=1, column=3, padx=5)

button_frame.pack(pady=20)


textbox = tk.Text(root, height=17, width=80, font=("Arial", 15))
textbox.pack()

root.mainloop()
