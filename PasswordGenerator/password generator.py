import random
import string
import tkinter as tk
from tkinter import messagebox

# Define character sets
symbols = "_#%*€$&₹@!"
letters = string.ascii_letters   # A-Z + a-z
digits = string.digits           # 0-9

# Combine all into one pool
all_chars = symbols + letters + digits

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 1:
            messagebox.showerror("Error", "Password length must be at least 1")
            return

        # Generate password
        password = "".join(random.choices(all_chars, k=length))

        # Display password
        password_box.config(state="normal")
        password_box.delete(0, tk.END)
        password_box.insert(0, password)
        password_box.config(state="readonly")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# Tkinter window setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("420x220")
root.configure(bg="black")

# Title Label
tk.Label(root, text="Password Generator", bg="black", fg="cyan",
         font=("Arial", 16, "bold")).pack(pady=10)

# Input label + entry
tk.Label(root, text="Enter Password Length:", bg="black", fg="white", font=("Arial", 12)).pack(pady=5)
length_entry = tk.Entry(root, width=10, font=("Arial", 12), bg="gray15", fg="white", insertbackground="white")
length_entry.pack()

# Button
tk.Button(root, text="Generate Password", command=generate_password,
          bg="gray20", fg="white", activebackground="gray35", activeforeground="white",
          font=("Arial", 12)).pack(pady=10)

# Output box
password_box = tk.Entry(root, font=("Arial", 14), justify="center", width=30,
                        bg="gray15", fg="black", insertbackground="white", state="readonly")
password_box.pack(pady=10)

# Run the app
root.mainloop()