import tkinter as tk               
from tkinter import font  as tkfont 
from game import start_game
import game


class Pages(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage,PageOne,PageTwo,PageThree,PageFour,PageFive,PageSix):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
#     root.title('Plantagotchi')
#     root.geometry('310x310+200+200')
#     root.resizable(False, False)
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        with open('startpage.txt','r') as f:   
            text = f.read()
        label = tk.Label(self, text=text, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Next",
                            command = lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Skip",
                            command = lambda: controller.show_frame("PageSix"))
        button1.pack(side = tk.RIGHT)
        button2.pack(side = tk.BOTTOM)
        #button1.grid(row=1, column=1, sticky="nsew")


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        with open('first_page.rtf','r') as f:   
            text = f.read()
        label = tk.Label(self, text=text, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Next",
                           command=lambda: controller.show_frame("PageTwo"))
        button2 = tk.Button(self, text="Prev",
                            command = lambda: controller.show_frame("StartPage"))
        button3 = tk.Button(self, text="Skip",
                            command = lambda: controller.show_frame("PageSix"))
        button1.pack(side = tk.RIGHT)
        button2.pack(side = tk.LEFT)
        button3.pack(side = tk.BOTTOM)
        #button1.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        with open('photosyntesys.txt','r') as f:   
            text = f.read()
        label = tk.Label(self, text=text, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Next",
                           command=lambda: controller.show_frame("PageThree"))
        button2 = tk.Button(self, text="Prev",
                            command = lambda: controller.show_frame("PageOne"))
        button3 = tk.Button(self, text="Skip",
                            command = lambda: controller.show_frame("PageSix"))
        button1.pack(side = tk.RIGHT)
        button2.pack(side = tk.LEFT)
        button3.pack(side = tk.BOTTOM)
        

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        with open('water.txt','r') as f:   
            text = f.read()
        label = tk.Label(self, text=text, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Next",
                           command=lambda: controller.show_frame("PageFour"))
        button2 = tk.Button(self, text="Prev",
                            command = lambda: controller.show_frame("PageTwo"))
        button3 = tk.Button(self, text="Skip",
                            command = lambda: controller.show_frame("PageSix"))
        button1.pack(side = tk.RIGHT)
        button2.pack(side = tk.LEFT)
        button3.pack(side = tk.BOTTOM)
        
class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        with open('hormon.txt','r') as f:   
            text = f.read()
        label = tk.Label(self, text=text, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Next",
                           command=lambda: controller.show_frame("PageFive"))
        button2 = tk.Button(self, text="Prev",
                            command = lambda: controller.show_frame("PageThree"))
        button3 = tk.Button(self, text="Skip",
                            command = lambda: controller.show_frame("PageSix"))
        button1.pack(side = tk.RIGHT)
        button2.pack(side = tk.LEFT)
        button3.pack(side = tk.BOTTOM)
        
class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        with open('stress.txt','r') as f:   
            text = f.read()
        label = tk.Label(self, text=text, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Next",
                           command=lambda: controller.show_frame("PageSix"))
        button2 = tk.Button(self, text="Prev",
                            command = lambda: controller.show_frame("PageFour"))
        button3 = tk.Button(self, text="Skip",
                            command = lambda: controller.show_frame("PageSix"))
        button1.pack(side = tk.RIGHT)
        button2.pack(side = tk.LEFT)
        button3.pack(side = tk.BOTTOM)
        
class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="GOOD LUCK", font=controller.title_font)
        label.pack(side="top", fill ="x", pady=10)
        
        button1 = tk.Button(self, text="Game",command = switching_game)
        button2 = tk.Button(self, text="Prev",
                            command = lambda: controller.show_frame("PageFive"))
       
        button1.pack(side = tk.BOTTOM)
        button2.pack(side = tk.LEFT)
       
        
        
def switching_game():
    Start_button = True
    game = start_game(Start_button)
        
        
        

        
# if __name__ == "__main__":
#     game = start_game(Start_button)