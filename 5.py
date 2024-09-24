from tkinter import *
import ttkbootstrap as tbs
from ttkbootstrap.constants import *
import pygame


root = tbs.Window(themename="superhero")
root.title("Horse Trainer")
root.geometry("800x600")


# New Game Button
ng_button = tbs.Button(bootstyle="primary, outline", text="New Game", command="", width=30)
ng_button.pack(pady=100)

# Options Button
options_button = tbs.Button(bootstyle="primary, outline", text="Options", command="", width=30)
options_button.pack()

# Exit Button
exit_button = tbs.Button(bootstyle="danger, outline", text="Quit", command="", width=30)
exit_button.pack(pady=100)


run = True




root.mainloop()