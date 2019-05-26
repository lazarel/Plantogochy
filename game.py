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
Pause = False
game_obj = characters.C3JuvenalPlant()
water_level = game_obj.water
stress = False
stress_level = game_obj.stress
day = 9
night = False
nutrient = 80


def start_game(event):
    global okToPressReturn
    if not okToPressReturn:
        restart_game()
    else:
        # update the time left label.
        start_label.config(text="")  # Чтобы не висело "Press return to start
        # start updating the values
        btn_water.config(stat="active")
        update_water_level()
        update_day()
        update_nutrient_level()
        update_display()
        okToPressReturn = False


def restart_game():
    if not is_alive():
        global water_level
        global day
        global stress
        global stress_level
        global night
        global nutrient
        game_obj = characters.C3JuvenalPlant()

        water_level = game_obj.water
        print(water_level)
        stress = False
        stress_level = game_obj.stress
        day = 0
        night = False
        nutrient = 80

        start_label.config(text="")  # Чтобы не висело "Press return to start
        # start updating the values
        update_water_level()
        update_day()
        update_stress_level()
        update_nutrient_level()
        update_display()


def pause():
    global Pause

    if Pause == True:

        Pause = False
        pause_label = tk.Label(text="         ", font=('Helvetica', 20)).grid(row=0, column=2)

    else:
        Pause = True
        pause_label = tk.Label(text="Pause!", font=('Helvetica', 20)).grid(row=0, column=2)


def update_display():
    global water_level
    global day
    global stress
    global stress_level

    if end_game():
        return

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

    if night:
        btn_co2.config(stat="active")
    else:
        btn_co2.config(stat="disabled")

    if not is_alive():
        if day < 3:
            plant_fig.config(image=died_plant)
        else:
            plant_fig.config(image=mature_died_plant)

    # Обновляем уровень воды
    water_level_label.config(text="Water level:")

    # Обновляем счетчик дней
    day_label.config(text="Day: " + str(day))

    # Функция запускается каждые 100ms
    plant_fig.after(100, update_display)

    stress_level_label.after(500, update_stress)


def update_stress():
    global stress
    if is_alive() and not end_game():
        if Pause == False:
            random_number = randint(0, 100)
            if random_number == 0:
                stress = True
                stress_level_label.config(text="MAYDAY MAYDAY MAYDAY", font=('Helvetica', 12, 'bold italic'))
            update_stress_level()


def update_stress_level():
    global stress
    global stress_level
    global water_level
    global day
    global nutrient
    if stress:
        stress_level += (1 + day / 2)
        water_level -= 3
        nutrient -= 2
        stress_bar['value'] = stress_level
        btn_mescaline.config(stat="active")
    else:
        stress_level = 0
        stress_bar['value'] = 0
        stress_level_label.config(text="Situation normal", font=('Helvetica', 12))


def update_water_level():
    global water_level
    global day
    water_level -= day
    water_bar['value'] = water_level
    if is_alive() and not end_game():
        if Pause == False:
            water_level_label.after(500, update_water_level)


def update_nutrient_level():
    global nutrient
    global day
    nutrient -= day / 10
    print(nutrient)
    nutrient_bar['value'] = nutrient
    if is_alive() and not end_game():
        if Pause == False:
            nutrient_label.after(500, update_nutrient_level)


def update_day():
    global day
    global night
    if end_game():
        return
    if is_alive() and not end_game():
        if Pause == False:
            if int(day) - day == 0:  # т.е. day - целое число
                day += 0.5
                night = False
                sky_fig.config(image=sun)
            else:
                day += 0.5
                night = True
                sky_fig.config(image=moon)
            day_label.after(3000, update_day)


def water_the_plant():
    global water_level
    water_level += 20
    water_bar['value'] = water_level


def fixation():
    global nutrient
    nutrient += 2
    nutrient_bar['value'] = nutrient


def mescaline():
    global stress
    stress = False
    btn_mescaline.config(stat="disabled")
    stress_level_label.config(text="Situation normal", font=('Helvetica', 12))


def is_alive():
    global water_level
    if 0 < water_level < 150 and nutrient > 0:
        btn_water.config(stat="active")
        return True
    else:
        if water_level <= 0:
            start_label.config(text="Game over! The plant has withered! Press return to restart")
        elif water_level >= 150:
            start_label.config(text="Game over! The plant has rotted! Press return to restart")
        if nutrient <= 0:
            start_label.config(text="Game over! The plant died of hunger! Press return to restart")
        btn_water.config(stat="disabled")
        btn_mescaline.config(stat="disabled")
        btn_co2.config(stat="disabled")
        return False


def end_game():
    if day == 10.0:
        start_label.config(text="Congratz! There is no prize, lol.")
        btn_water.config(stat="disabled")
        btn_mescaline.config(stat="disabled")
        btn_co2.config(stat="disabled")
        plant_fig.config(image=victory)
        return True


root = tk.Tk()
root.title("Plantogotchi")
root.geometry("1060x720")
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
victory = tk.PhotoImage(file="victory_plant.png")

start_label = tk.Label(text="Press 'Return' to start!", font=('Helvetica', 12))
start_label.grid(row=0, column=2)

water_level_label = tk.Label(text="Water level", font=('Helvetica', 12))
water_level_label.grid(row=1, column=2)

water_bar_style = ttk.Style()
water_bar_style.theme_use('default')
water_bar_style.configure("blue.Horizontal.TProgressbar", background="blue")
water_bar = Progressbar(orient="horizontal", length=200, maximum=150,
                        mode="determinate", style="blue.Horizontal.TProgressbar")
water_bar.grid(row=2, column=2)

stress_level_label = tk.Label(text="Situation normal", font=('Helvetica', 12))
stress_level_label.grid(row=3, column=2)

stress_bar_style = ttk.Style()
stress_bar_style.theme_use('default')
stress_bar_style.configure("red.Horizontal.TProgressbar", background="red")
stress_bar = Progressbar(orient="horizontal", length=200, maximum=100,
                         mode="determinate", style="red.Horizontal.TProgressbar")
stress_bar.grid(row=4, column=2)

nutrient_label = tk.Label(text="Nutrients level:", font=('Helvetica', 12))
nutrient_label.grid(row=2, column=3)

nutrient_bar_style = ttk.Style()
nutrient_bar_style.theme_use('default')
nutrient_bar_style.configure("green.Horizontal.TProgressbar", background="green")
nutrient_bar = Progressbar(orient="horizontal", length=200, maximum=100,
                           mode="determinate", style="green.Horizontal.TProgressbar")
nutrient_bar.grid(row=3, column=3)

day_label = tk.Label(text="Day: " + str(day), font=('Helvetica', 12))
day_label.grid(row=5, column=2)

with open("water.txt", "r") as f1:
    water_text = f1.read()
water_text_label = tk.Label(text=water_text, font=('Helvetica', 12))
water_text_label.grid(row=6, column=1)

with open("stress.txt", "r") as f2:
    stress_text = f2.read()
stress_text_label = tk.Label(text=stress_text, font=('Helvetica', 14))
stress_text_label.grid(row=6, column=3)

plant_fig = tk.Label(image=normal_plant)
plant_fig.grid(row=6, column=2)

sky_fig = tk.Label(image=sun)
sky_fig.grid(row=0, rowspan=6, column=1, sticky=tk.NSEW)

btn_water = tk.Button(image=water_button, command=water_the_plant)
btn_water.config(stat="disabled")
btn_water.grid(row=7, column=1, sticky=tk.NSEW)

btn_co2 = tk.Button(image=co2, command=fixation)
btn_co2.config(stat="disabled")
btn_co2.grid(row=7, column=2, sticky=tk.NSEW)

btn_mescaline = tk.Button(image=mescaline_button, command=mescaline, stat="disabled")
btn_mescaline.grid(row=7, column=3, sticky=tk.NSEW)

# run the 'startGame' function when the enter key is pressed.
root.bind('<Return>', start_game)
btn_pouse = tk.Button(text="Pause", height='12', command=pause)
# btn_pouse.config(stat="disabled")
btn_pouse.grid(row=6, column=0)
# root.bind("<space>", pause)
# start the GUI
root.mainloop()
