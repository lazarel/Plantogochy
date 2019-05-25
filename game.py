import tkinter as tk
import tkinter.ttk as ttk
from tkinter.ttk import Progressbar
from random import randint
import characters
import json, os

SAVE_DIR = '~/Plantogotchi/save'

class FullScreenApp(tk.Frame):
    def __init__(self, parent, **kw):
        super().__init__(**kw)
        self.parent = parent
        menubar = tk.Menu(self.parent)
        self.parent.config(menu=menubar)
        fileMenu = tk.Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=fileMenu)


okToPressReturn = True
game_obj = characters.C3JuvenalPlant()
water_level = game_obj.water
stress = False
stress_level = game_obj.stress
day = 0
night = False


def start_game(event):
    global okToPressReturn
    if okToPressReturn == False:
        pass
    else:
        # update the time left label.
        start_label.config(text="")  # Чтобы не висело "Press return to start
        # start updating the values
        btn_water.config(stat="active")
        update_water_level()
        update_day()
        update_display()
        okToPressReturn = False


def update_display():
    global water_level
    global day
    global stress
    global stress_level

    if water_level <= 15 or water_level >= 115:
        if day < 3:
            plant_fig.config(image=dying_plant)
        else:
            plant_fig.config(image=mature_dying_plant)
    else:
        if day < 3:
            plant_fig.config(image=normal_plant)
        else:
            plant_fig.config(image=mature_plant)

    if stress:
        if day < 3:
            plant_fig.config(image=stress_plant)
        else:
            plant_fig.config(image=mature_stress_plant)
        btn_mescaline.config(stat="active")

    if not is_alive():
        if day < 3:
            plant_fig.config(image=died_plant)
        else:
            plant_fig.config(image=mature_died_plant)

    # Обновляем уровень воды
    water_level_label.config(text="Water level:")  # + str(water_level))

    # Обновляем счетчик дней
    day_label.config(text="Day: " + str(day))

    # Функция запускается каждые 100ms
    plant_fig.after(100, update_display)

    stress_level_label.after(500, update_stress)


def update_stress():
    global stress
    if is_alive():
        random_number = randint(0, 100)
        if random_number == 0:
            stress = True
            stress_level_label.config(text="MAYDAY MAYDAY MAYDAY", font=('Helvetica', 12, 'bold italic'))
        update_stress_level()


def update_stress_level():
    global stress
    global stress_level
    global water_level
    if stress:
        stress_level += 1
        water_level -= 3
        stress_bar['value'] = stress_level
        btn_mescaline.config(stat="active")
    else:
        stress_level = 0
        stress_bar['value'] = 0


def update_water_level():
    global water_level
    water_level -= 1
    water_bar['value'] = water_level
    if is_alive():
        water_level_label.after(500, update_water_level)


def update_day():
    global day
    global night
    if is_alive():
        night = False
        day += 1
        day_label.after(2000, update_night())



def update_night():
    global night
    if is_alive():
        night = True
        day_label.after(2000, update_day())


def water_the_plant():
    global water_level
    water_level += 20
    water_bar['value'] = water_level


def mescaline():
    global stress
    stress = False
    btn_mescaline.config(stat="disabled")
    stress_level_label.config(text="Situation normal", font=('Helvetica', 12))


def is_alive():
    global water_level
    if water_level != 0 and water_level < 150:
        btn_water.config(stat="active")
        return True
    else:
        if water_level <= 0:
            start_label.config(text="Game over! The plant has withered!")
        elif water_level >= 150:
            start_label.config(text="Game over! The plant has rotted!")
        btn_water.config(stat="disabled")
        btn_mescaline.config(stat="disabled")
        return False


root = tk.Tk()
root.title("Plantogotchi")
root.geometry("1010x720")
root.resizable(width=False, height=False)

app = FullScreenApp(root)

##################################################################
# ADDING IMAGES
dying_plant = tk.PhotoImage(file="dying_plant.png")
normal_plant = tk.PhotoImage(file="normal_plant.png")
mature_plant = tk.PhotoImage(file="mature_plant.png")
stress_plant = tk.PhotoImage(file="stress_plant.png")
mature_stress_plant = tk.PhotoImage(file="mature_stress_plant.png")
mature_dying_plant = tk.PhotoImage(file="mature_dying_plant.png")
died_plant = tk.PhotoImage(file="died_plant.png")
mature_died_plant = tk.PhotoImage(file="mature_died_plant.png")
water_button = tk.PhotoImage(file="water_splash.png")
msg = tk.PhotoImage(file="magic.png")
mescaline_button = tk.PhotoImage(file="mescaline.png")
sun = tk.PhotoImage(file="creepy_sun.png")
moon = tk.PhotoImage(file="molester_moon.png")
co2 = tk.PhotoImage(file="co2.png")

start_label = tk.Label(text="Press 'Return' to start!", font=('Helvetica', 12))
start_label.grid(row=0, column=2)

water_level_label = tk.Label(text="Water level", font=('Helvetica', 12))
water_level_label.grid(row=1, column=2)


water_bar_style = ttk.Style()
water_bar_style.theme_use('default')
water_bar_style.configure("blue.Horizontal.TProgressbar", background="blue")
water_bar = Progressbar(orient="horizontal",length=200, maximum=150,
                        mode="determinate", style="blue.Horizontal.TProgressbar")
water_bar.grid(row=2, column=2)

stress_level_label = tk.Label(text="Situation normal", font=('Helvetica', 12))
stress_level_label.grid(row=3, column=2)

stress_bar_style = ttk.Style()
stress_bar_style.theme_use('default')
stress_bar_style.configure("redHorizontal.Tprogressbar", background="red")
stress_bar = Progressbar(orient="horizontal", length=200, maximum=100,
                         mode="determinate", style="red.Horizontal.TProgressbar")
stress_bar.grid(row=4, column=2)

day_label = tk.Label(text="Day: " + str(day), font=('Helvetica', 12))
day_label.grid(row=5, column=2)

with open("water.txt", "r") as f1:
    water_text = f1.read()
water_text_label = tk.Label(text=water_text, font=('Helvetica', 12))
water_text_label.grid(row=6, column=1)

with open("stress.txt", "r") as f2:
    stress_text = f2.read()
stress_text_label = tk.Label(text=stress_text, font=('Helvetica', 12))
stress_text_label.grid(row=6, column=4)

plant_fig = tk.Label(image=normal_plant)
plant_fig.grid(row=6, column=2)

# sky_fig = tk.Label(image=sun)
# sky_fig.grid(rowspan=5, column=1, sticky=tk.NSEW)

btn_water = tk.Button(image=water_button, command=water_the_plant)
btn_water.config(stat="disabled")
btn_water.grid(row=7, column=1, sticky=tk.NSEW)

btn_co2 = tk.Button(image=co2)
btn_co2.config(stat="disabled")
btn_co2.grid(row=7, column=2, sticky=tk.NSEW)

btn_mescaline = tk.Button(image=mescaline_button, command=mescaline, stat="disabled")
btn_mescaline.grid(row=7, column=4, sticky=tk.NSEW)

# run the 'startGame' function when the enter key is pressed.
root.bind('<Return>', start_game)
# start the GUI
root.mainloop()