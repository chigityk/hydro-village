import tkinter as tk
from tkinter import Button, Frame, Grid, Image, Label, PhotoImage, Scale, Text, Toplevel, ttk, font, Tk
import time
import os
import sys
from tkinter.constants import S
timeString = time.strftime('%a %b %d %I:%M %p')

## Root Setup ##
main = tk.Tk()
main.title('Hydro System')
main.configure(background='#02394A')
main.geometry('{}x{}'.format(800, 400))


## Add Images ##
img_fanoff = PhotoImage(file='assets/fanoff.png')
img_fanon = PhotoImage(file='assets/fanon.png')
img_o2off = PhotoImage(file='assets/o2off.png')
img_o2on = PhotoImage(file='assets/o2on.png')
img_h2ooff = PhotoImage(file='assets/h2ooff.png')
img_h2oon = PhotoImage(file='assets/h2oon.png')
img_settings = PhotoImage(file='assets/settings.png')
img_addphup = PhotoImage(file='assets/addphup.png')
img_addphdown = PhotoImage(file='assets/addphdown.png')
img_addgro = PhotoImage(file='assets/addgro.png')
img_addmicro = PhotoImage(file='assets/addmicro.png')
img_addbloom = PhotoImage(file='assets/addbloom.png')
img_addwater = PhotoImage(file='assets/addwater.png')

## Create all of the main containers ##
top_frame = Frame(main, bg='#02394A', width=800, height=75)
center = Frame(main, bg='#02394A')
btm_frame = Frame(main, bg='#02394A', width=800, height=10)

## Configure layout of main ##
top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")
btm_frame.grid(row=2, sticky="ew")


## Create Widgets For Top Frame ##
time_lbl = ttk.Label(top_frame, text=timeString)

## Layout Widgets In Top Frame ##
time_lbl.grid(row=0, column=1, sticky='ns')

## Configure Layout For Center Frame ##
ctr_left = Frame(center, bg='#02394A', width=160, height=250)
ctr_mid = Frame(center, bg='#02394A', width=425, height=250)
ctr_right = Frame(center, bg='#02394A', width=125, height=250)

ctr_left.grid(row=1, column=0, sticky='nsew')
ctr_mid.grid(row=1, column=1, sticky='nsew')
ctr_right.grid(row=1, column=2, sticky='nsew')

## Create Widgets For Center Left Frame ##
nutrients_lbl = ttk.Label(ctr_left, text='Nutrient Buttons Add While Pressed', justify='center', wraplength=150, font=('sans-serif', 7))

addphup_btn = tk.Button(ctr_left, 
                        image=img_addphup,
                        bg='#02394A',
                        activebackground='#02394A',
                        command=None,
                        border=0,
                        highlightthickness=0,
                        height=70,
                        width=70)

addphdown_btn = tk.Button(ctr_left, 
                        image=img_addphdown,
                        bg='#02394A',
                        activebackground='#02394A',
                        command=None,
                        border=0,
                        highlightthickness=0,
                        height=70,
                        width=70)

addgro_btn = tk.Button(ctr_left, 
                        image=img_addgro,
                        bg='#02394A',
                        activebackground='#02394A',
                        command=None,
                        border=0,
                        highlightthickness=0,
                        height=70,
                        width=70)

addmicro_btn = tk.Button(ctr_left, 
                        image=img_addmicro,
                        bg='#02394A',
                        activebackground='#02394A',
                        command=None,
                        border=0,
                        highlightthickness=0,
                        height=70,
                        width=70)

addbloom_btn = tk.Button(ctr_left, 
                        image=img_addbloom,
                        bg='#02394A',
                        activebackground='#02394A',
                        command=None,
                        border=0,
                        highlightthickness=0,
                        height=70,
                        width=70)

addwater_btn = tk.Button(ctr_left, 
                        image=img_addwater,
                        bg='#02394A',
                        activebackground='#02394A',
                        command=None,
                        border=0,
                        highlightthickness=0,
                        height=70,
                        width=70)


## Layout Widgets In Center Left Frame ##
nutrients_lbl.grid(row=0, column=0, columnspan=2, sticky='nesw')
addphup_btn.grid(row=2, column=0, pady=2, sticky='nesw')
addgro_btn.grid(row=2, column=1, sticky='nesw')
addphdown_btn.grid(row=3, column=0, pady=2, sticky='nesw')
addmicro_btn.grid(row=3, column=1, sticky='nesw')
addwater_btn.grid(row=4, column=0, pady=2, sticky='nesw')
addbloom_btn.grid(row=4, column=1, sticky='nesw')

## Create Widgets for Center Mid Frame - Sensor Input ##

## Layout Widgets In Center Mid Frame ##

## Create Widgets for Center Right Frame - Lights Control ##
lights_lbl = ttk.Label(ctr_right, text='Slide For Light Start/End Times')
lightsstart_lbl = ttk.Label(ctr_right, text='Start Time:')
start_scale = Scale(ctr_right, background='#02394A', from_=0, to=24, length=150, orient='horizontal', command=None)
lightsstop_lbl = ttk.Label(ctr_right, text='End Time')
stop_scale = Scale(ctr_right, background='#02394A', from_=0, to=24, length=150, orient='horizontal', command=None)

## Layout Widgets In Center Right Frame ##
lights_lbl.grid(row=0, column=0)
lightsstart_lbl.grid(row=1, column=0)
start_scale.grid(row=2, column=0)
lightsstop_lbl.grid(row=3, column=0)
stop_scale.grid(row=4, column=0)


## Create Widgets for Bottom Frame ##

#fan on/off switch
# Define our switch function
def fanSwitch():
    global fanOn 
    # Determine is on or off
    if fanOn:
        fanbtn.config(image = img_fanoff)
        print('the fan is off')
        fanOn = False
    else:
        fanbtn.config(image = img_fanon)
        print('the fan is on')
        fanOn = True
  

fanbtn = tk.Button(btm_frame,
                image=img_fanon,
                bg='#02394A',
                activebackground='#02394A',
                command=fanSwitch,
                border=0,
                highlightthickness=0,
                height=70,
                width=70)

#o2 pump on/off switch
# Define our switch function
def o2Switch():
    global o2On
      
    # Determine is on or off
    if o2On:
        o2btn.config(image = img_o2off)
        o2On = False
    else:
        o2btn.config(image = img_o2on)
        o2On = True
  

o2btn = tk.Button(btm_frame,
                image=img_o2on,
                bg='#02394A',
                activebackground='#02394A',
                command=o2Switch,
                border=0,
                highlightthickness=0,
                height=70,
                width=70)

#water pump on/off switch
# Define our switch function
def h2oSwitch():
    global h2oOn
      
    # Determine is on or off
    if h2oOn:
        h2obtn.config(image = img_h2ooff)
        h2oOn = False
    else:
        h2obtn.config(image = img_h2oon)
        h2oOn = True
  
h2obtn = tk.Button(btm_frame,
                image=img_h2oon,
                bg='#02394A',
                activebackground='#02394A',
                command=h2oSwitch,
                border=0,
                highlightthickness=0,
                height=70,
                width=70)

## Layout Widgets in Bottom Frame ##
fanbtn.grid(row=0, column=0)
o2btn.grid(row=0, column=1)
h2obtn.grid(row=0, column=2)

## global is_on function for toggling pumps - replace with code to fetch pump state##
o2On = True
h2oOn = True
fanOn = True

## Style Configure ##

main.style = ttk.Style(main)
main.style.configure('TLabel', background='#02394A', font='notosansbold', foreground='white')


main.mainloop()
