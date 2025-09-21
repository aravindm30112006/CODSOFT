import customtkinter as ctk
import random
from PIL import Image  # for loading PNG images

# CustomTkinter setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

choices = ["Stone", "Paper", "Scissor"]

def play(user_choice):
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Stone" and computer_choice == "Scissor") or \
         (user_choice == "Paper" and computer_choice == "Stone") or \
         (user_choice == "Scissor" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.configure(
        text=f"Your Choice: {user_choice}\nComputer Choice: {computer_choice}\n\n{result}"
    )
    retry_button.pack(pady=10)

def reset_game():
    result_label.configure(text="Make your move!")
    retry_button.pack_forget()

# Main Window
app = ctk.CTk()
app.title("Stone Paper Scissor Game")
app.geometry("550x500")

# Title
title_label = ctk.CTkLabel(app, text="Stone Paper Scissor",
                           font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Instruction
instruction_label = ctk.CTkLabel(app, text="Choose one:", font=("Arial", 14))
instruction_label.pack(pady=5)

# Frame for buttons
button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=10)

# Load images
stone_img = ctk.CTkImage(Image.open("stone.png"), size=(100, 100))
paper_img = ctk.CTkImage(Image.open("paper.png"), size=(100, 100))
scissor_img = ctk.CTkImage(Image.open("scissor.png"), size=(100, 100))

# Buttons with images
stone_btn = ctk.CTkButton(button_frame, image=stone_img, text="",
                          width=120, height=120,
                          command=lambda: play("Stone"))
stone_btn.pack(side="left", padx=10)

paper_btn = ctk.CTkButton(button_frame, image=paper_img, text="",
                          width=120, height=120,
                          command=lambda: play("Paper"))
paper_btn.pack(side="left", padx=10)

scissor_btn = ctk.CTkButton(button_frame, image=scissor_img, text="",
                            width=120, height=120,
                            command=lambda: play("Scissor"))
scissor_btn.pack(side="left", padx=10)

# Result Label
result_label = ctk.CTkLabel(app, text="Make your move!",
                            font=("Arial", 16), justify="center")
result_label.pack(pady=30)

# Retry Button
retry_button = ctk.CTkButton(app, text="Retry", fg_color="red",
                             hover_color="darkred", command=reset_game)

# Run app
app.mainloop()