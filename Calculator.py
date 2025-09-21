import customtkinter as ctk # type: ignore

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

win = ctk.CTk()
win.title("Calculator")
win.geometry("300x400")
win.resizable(False, False)

eq = ""
inp = ctk.StringVar()

entry = ctk.CTkEntry(win, textvariable=inp, font=("Consolas", 22), width=280, height=50,
                     justify="right", text_color="#bb86fc")
entry.pack(pady=10, padx=10)

def press(n):
    global eq
    eq += str(n)
    inp.set(eq)

def clr():
    global eq
    eq = ""
    inp.set("")

def eqf():
    global eq
    try:
        eq = str(eval(eq))
    except:
        eq = "Error"
    inp.set(eq)

frame = ctk.CTkFrame(win)
frame.pack(expand=True, fill="both", padx=10, pady=10)

btns = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for i, row in enumerate(btns):
    for j, b in enumerate(row):
        action = eqf if b == '=' else lambda x=b: press(x)
        btn = ctk.CTkButton(
            frame, text=b, command=action,
            font=("Consolas", 18), width=60, height=60,
            corner_radius=15,
            fg_color="#1a1a1a", hover_color="#333", text_color="#fff"
        )
        btn.grid(row=i+1, column=j, padx=5, pady=5)

clr_btn = ctk.CTkButton(
    frame, text="C", command=clr,
    font=("Consolas", 18), width=60, height=60,
    corner_radius=15,
    fg_color="#790ea0", hover_color="#8e2ebc", text_color="#fff"
)
clr_btn.grid(row=0, column=3, padx=5, pady=5)

for i in range(4):
    frame.grid_columnconfigure(i, weight=1)
for i in range(5):
    frame.grid_rowconfigure(i, weight=1)

win.mainloop()