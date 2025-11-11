import tkinter as tk

root = tk.Tk()
root.title("Happy Path")
root.geometry("600x400")

tk.Label(root, text="Login Form", font=("Arial", 20, "bold")).pack(pady=20)

label = tk.Label(root, text="Username", font=("Arial", 10))
label.pack()
uname = tk.Entry(root , width=20, font=("Arial", 20))
uname.pack(padx=10,pady=10)

label = tk.Label(root, text="Password", font=("Arial", 10))
label.pack()
pas = tk.Entry(root, width=20, font=("Arial", 20), show="*")
pas.pack(padx=10,pady=10)

def login():
    username = "admin"
    password = "admin123"

    if username == uname.get() and password == pas.get():
        messagebox.showinfo("Success", "Login Successful")
    else:
        messagebox.showerror("Error", "Incorrect username or password")
        uname.delete(0, "end")
        pas.delete(0, "end")

button = tk.Button(root,  text="Login", command=login , font=("Arial", 13, "bold"))
button.pack(pady=30, ipadx=100)

root.mainloop()