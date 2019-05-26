import json
import os
from tkinter import filedialog
from tkinter import messagebox

#self.lock = False


def _get_save_file_name(self):
    initialdir = os.path.expanduser(SAVE_DIR)
    if not os.path.exists(initialdir):
        os.makedirs(initialdir)
    save_file_name = filedialog.asksaveasfilename(
        initialdir=initialdir,
        title='Save game',
        filetypes=(("json files", "*.json"), ("all files", "*.*"))
    )
    if save_file_name in [(), '']:
        return None
    return save_file_name
    
def _get_load_file_name(self):
    initialdir = os.path.expanduser(SAVE_DIR)
    if not os.path.exists(initialdir):
        initialdir = os.path.expanduser('~')
    save_file_name = filedialog.askopenfilename(
        initialdir=initialdir,
        filetypes=(("json files", "*.json"), ("all files", "*.*"))
    )
    if save_file_name in [(), '']:
        return None
    return save_file_name

def save(self):
    old_lock = self.lock
    self.lock = True
    save_file_name = self._get_save_file_name()
    if save_file_name is not None:
        saved_game = {
            "water_level": game_obj.water,
            "stress_level": game_obj.stress,
            "day": game_obj.update_day,
            "stress": game_obj.update_stress,
        }
        with open(save_file_name, 'w') as f:
            json.dump(saved_game, f)
    self.lock = old_lock



def _init_atributes_with_loaded_values(self, saved_game):
    self.turn = saved_game['turn']
    self.moves = saved_game['moves']
    self.bot = eval(saved_game['bot_class_name'] + '(self)')
    self.grid = saved_game['grid']
    self.finished = saved_game['finished']
    self.human = saved_game['human']
    self.victory_line = saved_game['victory_line']
    return saved_game['lock']
#     
#     
    
def load(self):
    self.lock = True
    load_file_name = self._get_load_file_name()
    if load_file_name is not None:
        with open(load_file_name) as f:
            saved_game = json.load(f)
        saved_lock = self._init_atributes_with_loaded_values(saved_game)
        # self._redraw(self.moves, self.victory_line)
        self.lock = saved_lock
        # if self.human != self.turn and not self.finished:
        #     self._move_bot()


def start_new_game(self):
    answer = messagebox.askyesno("New game", "Bot makes the first move in the game?")
    self.lock = True
    self.turn = 0
    self.human = int(answer)
    self.moves = []
    self.grid = [[None]*3 for _ in range(3)]
    self.finished = False
    self.frame.reset_canvas()
    self._move_bot()
    self.lock = False
    self.victory_line = None