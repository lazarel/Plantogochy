from game import Game
import tkinter as tk

def set_window(root):
    root.title('Plantaegotchi')
    root.geometry('310x310+200+200')
    root.resizable(False, False)


root = tk.Tk()
set_window(root)
