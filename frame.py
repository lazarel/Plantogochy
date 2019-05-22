import tkinter as tk

'''
Root is an ordinary window, with a title bar and other
    decoration provided by your window manager
    
    root = Tk()
    
    A Label widget can display either text or an icon or other image
    Pack tells it to size itself to fit the given text,
    and make itself visible
    
    w = Label(root, text="Hello world")
    w.pack()
    
    The window won’t appear
    until we’ve entered the Tkinter event loop

    root.mainloop()   
'''


class MainFrame(tk.Frame):
    def __init__(self, root, game):
        super().__init__()
        #self._canvas = None
        self._game = game
        self._game.add_frame(self)
        self._add_menu()
        #self._add_canvas()

    def _add_menu(self):
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar)
        game_menu = tk.Menu(menu_bar)

        file_menu.add_command(label="save", command=self._game.save)
        file_menu.add_command(label="load", command=self._game.load)

        game_menu.add_command(label='new', command=self._game.start_new_game)

        menu_bar.add_cascade(label="file", menu=file_menu)
        menu_bar.add_cascade(label='game', menu=game_menu)







#class MainFrame(tk.Frame):
    #def __init__(selfself, root, game):