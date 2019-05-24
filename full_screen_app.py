import tkinter as tk


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