import tkinter as tk

import characters

Start_button = True

game_obj = characters.C3JuvenalPlant()
water_level = game_obj.water
day = 0


def start_game(event):
    global Start_button

    if Start_button == False:
        pass

    else:
        # update the time left label.
        #start_label.config(text="")
        # start updating the values
        update_water_level()
        update_day()
        update_display()

        Start_buttom = False

def update_display():
    global water_level
    global day

    if water_level <= 15 or water_level >= 115:
        plant_fig.config(image = dying_plant)
    else:
        plant_fig.config(image = normal_plant)

    # Обновляем уровень воды
    water_level_label.config(text="Water level: " + str(water_level))

    # Обновляем счетчик дней
    day_label.config(text="Day: " + str(day))

    # Функция запускается каждые 100ms
    plant_fig.after(100, update_display)


def update_water_level():
    global water_level
    water_level -= 1
    if is_alive():
        water_level_label.after(500, update_water_level)


def update_day():
    global day
    day += 1
    if is_alive():
        day_label.after(5000, update_day)


def water_the_plant():
    global water_level
    water_level += 20


def is_alive():
    global water_level
    if water_level == 0:
        start_label.config(text="Game over! The plant has withered!")
        return False
    elif water_level >= 150:
        start_label.config(text="Game over! The plant has rotted!")
        return False
    else:
        return True


root = tk.Tk()
#set the title.
root.title("Stay Alive!")
#set the size.
root.geometry("500x300")

start_label = tk.Label(root, text="Press 'Return' to start!", font=('Helvetica', 12))
start_label.pack()

water_level_label = tk.Label(root, text="Water level: " + str(water_level), font=('Helvetica', 12))
water_level_label.pack()

#add a 'day' label.
day_label = tk.Label(root, text="Day: " + str(day), font=('Helvetica', 12))
day_label.pack()

# ADDING IMAGES
dying_plant = tk.PhotoImage(file="dying_plant.png")
normal_plant = tk.PhotoImage(file="normal_plant.png")

#add a cat image
plant_fig = tk.Label(root, image=normal_plant)
plant_fig.pack()

btn_water = tk.Button(root, text="Water the plant", command=water_the_plant)
btn_water.pack()

#run the 'startGame' function when the enter key is pressed.
root.bind('<Return>', start_game)

#start the GUI
root.mainloop()