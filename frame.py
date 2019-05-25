import tkinter as tk
from tkinter.ttk import Progressbar
from game import day, water_the_plant, mescaline


class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        pad = 3
        self._geom = '1000x900+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom




start_label = tk.Label(text="Press 'Return' to start!", font=('Helvetica', 12))
start_label.pack()

water_level_label = tk.Label(text="Water level", font=('Helvetica', 12))
water_level_label.pack()

stress_level_label = tk.Label(text="Situation normal", font=('Helvetica', 12))
stress_level_label.pack()

water_bar = Progressbar(orient="horizontal",length=200, maximum=150,
                        mode="determinate", style='green.Horizontal.TProgressbar')
water_bar.pack()

# add a 'day' label.
day_label = tk.Label(text="Day: " + str(day), font=('Helvetica', 12))
day_label.pack()

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


# using an image
plant_fig = tk.Label(image=normal_plant)
plant_fig.pack()

btn_water = tk.Button(image=water_button, command=water_the_plant)
btn_water.pack(side=tk.RIGHT)


btn_mescaline = tk.Button(image=mescaline_button, command=mescaline, stat="disabled")
# if stress:
#     btn_mescaline.config(state="enabled")
# else:
#     btn_mescaline.config(state="disabled")
btn_mescaline.pack(side=tk.LEFT)
