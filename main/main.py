import tkinter
import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("600x600")  # Window size
root.title("Python Tkinter My First GUI")

# Label
label = tk.Label(root, text="Hello World", font=("Arial", 20))
label.pack(padx=20, pady=20)

# Multi-line Textbox
textbox = tk.Text(root, height=2, width=20, font=("Arial", 15))
textbox.pack(padx=20, pady=10)

# Single-line Entry (optional, for passwords)

# entry = tk.Entry(root)
# entry.pack(padx=10, pady=10)


# Button (optional)
# button = tk.Button(root, text="Pindutin moooo", font=("Arial", 20))
# button.pack(padx=10, pady=10)

# Frame for multiple buttons in grid
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

# Buttons in grid layout
btn1 = tk.Button(buttonframe, text="1", font=("Arial", 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font=("Arial", 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=("Arial", 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4", font=("Arial", 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5", font=("Arial", 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6", font=("Arial", 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

# Pack the frame to fill horizontally
buttonframe.pack(fill='x', padx=20, pady=20)

# Another button using place
anotherbtn = tk.Button(root, text="TEST")
anotherbtn.place(x=130, y=93, width=50, height=40)

# Run the main loop
root.mainloop()
