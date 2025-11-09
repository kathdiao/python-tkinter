import tkinter as tk

root = tk.Tk()
root.title("My First GUI")
root.geometry("300x300")

def hello():
    print("Hello World!")

button = tk.Button(root,  text="Click Me!", command=hello, font=("Arial", 15))
button.pack(pady=60)

root.mainloop()