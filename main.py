from game import FullScreenApp, start_game


if __name__ == '__main__':
    app = FullScreenApp(parent=start_game(True))
    app.mainloop()