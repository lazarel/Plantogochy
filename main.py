from game import start_game
import tkinter as tk
from frame import MainFrame

def set_window(root):
    root.title('Plantagotchi')
    root.geometry('310x310+200+200')
    root.resizable(False, False)

okToPressReturn = True

if __name__ == '__main__':
    game = start_game(okToPressReturn)

root = tk.Tk()
set_window(root)
frame = MainFrame(root, game)

