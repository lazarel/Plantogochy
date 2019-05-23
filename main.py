#from game import start_game
import tkinter as tk
#from frame import MainFrame
from Frames_switching import *

# def set_window(root):
#     root.title('Plantagotchi')
#     root.geometry('310x310+200+200')
#     root.resizable(False, False)

Start_button = False

if __name__ == '__main__':
    #game = start_game(Start_buttom)
    app = Pages()
    app.mainloop()

# root = tk.Tk()
# set_window(root)
# frame = MainFrame(root, game)

