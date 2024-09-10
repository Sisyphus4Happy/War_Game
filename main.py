from tkinter import *
from tkinter import messagebox, simpledialog
import tkinter as tk
from random import choice, randint

#Here is the beginning of the game, below an if will be created in case the choice is made by just one player
# (it is impossible to play alone) 
choice_player = [
    1, 2, 3, 4
    ]

#Color of the your army
list_army = [
    "red", "Black", "Yellow", "Branco"
    ]
#separation of territories
South_America = [
    "Brazil","Argentina","Colombia","Peru","Uruguay","Bolivia","Caribbean","French Guinea"
]
North_America = [
    "Mexico","California","New York","Labrador","Ottawa","Vancouver","Mackenzie","Alaska","Greenland",
]
Europe = [
    "Iceland","England","Germany","France","Sweden","Poland","Moscow","Netherlands"
]
Africa = [
    "Algeria","Egypt","Congo","Sudan","Madagascar","South Africa","Nigeria",
]
Asia = [
    "Middle East","Aral","Omsk","Dudinka","Siberia","Mongolia","Vladivostok","China","India","Japan","Vietnam"
]
Oceania = [
    "Borneo","Sumatra","New Zealand","Australia", "Fiji"
]
window = Tk()
class FirstWindow:
    def __init__(self):
        self.window = window
        self.screen()
        self.frames_of_the_screens()
        window.mainloop()
    #function for configuration of the window
    def screen(self):
        self.window.title("Welcome to WAR")
        self.window.configure(background = "red4")
        self.window.geometry("700x500")
        self.window.resizable(True, True)
        self.window.maxsize(width=900, height=700)
        self.window.minsize(width=400, height=300) 
    #function for frames      
    def frames_of_the_screens(self):
        self.frame_1 = Frame(self.window, bd=4, bg="black", highlightbackground="black", highlightthickness=3)
        self.frame_1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.frame_1.configure(background="red2")

        self.frame_2 = Frame(self.window, bd=1, bg="black", highlightbackground="black", highlightthickness=3)
        self.frame_2.place(relx=0.03, rely=0.008, relwidth=0.3, relheight=0.2)
        self.frame_2.configure(background="white")


        
#Action for definition of the players and separation of the territory 
#Here, the name, army and territory of the players are definited
class Player():
    def __init__(self, player_name, total_army, total_territory):
        self.player_name = player_name
        self.total_army = total_army
        self.total_territory = total_territory
    





FirstWindow()