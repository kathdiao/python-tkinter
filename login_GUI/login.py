import tkinter as tk

root = tk.Tk()
root.title("Login GUI")
root.geometry("600x400")

tk.Label(root, text="Login Form", font=("Arial", 20, "bold")).pack(pady=20)

label = tk.Label(root, text="Username", font=("Arial", 10))
label.pack()
uname = tk.Entry(root, width=20, font=("Arial", 20) )
uname.pack(padx=10,pady=10)

label = tk.Label(root, text="Password", font=("Arial", 10))
label.pack()
password = tk.Entry(root, width=20, font=("Arial", 20), show="*")
password.pack(padx=10,pady=10)

button = tk.Button(root,  text="Login", font=("Arial", 15))
button.pack(pady=60, ipadx=20)

root.mainloop()