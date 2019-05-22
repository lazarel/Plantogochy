from game import Game
import tkinter as tk

def set_window(root):
    root.title('Plantaegotchi')
    root.geometry('310x310+200+200')
    root.resizable(False, False)


if __name__ == '__main__':
    game = Game()

root = tk.Tk()
set_window(root)
frame = MainFrame(root, game)

