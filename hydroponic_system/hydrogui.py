import tkinter as tk
from tkinter import Button, Frame, Grid, Image, Label, PhotoImage, ttk, font
import time
import os
timeString = time.strftime('%I:%M %p')

os.chdir('hydroponic_system')

main = tk.Tk()
main.title('Lettuce Wall')
main.configure(background='#02394A', width=700, height=700)
main.columnconfigure(0, weight=1)
main.rowconfigure(0, weight=1)

img_fanoff = PhotoImage(file='assets/fanoff.png')
img_fanon = PhotoImage(file='assets/fanon.png')
img_o2off = PhotoImage(file='assets/o2off.png')
img_o2on = PhotoImage(file='assets/o2on.png')
img_h2ooff = PhotoImage(file='assets/h2ooff.png')
img_h2oon = PhotoImage(file='assets/h2oon.png')
img_settings = PhotoImage(file='assets/settings.png')

#global is_on function
o2On = True
h2oOn = True
fanOn = True

main.style = ttk.Style(main)
main.style.configure('TButton',
    font=('notosansbold', 15),
    foreground='white',
    background='#02394A',
    highlightcolor='lightblue',
    highlightthickness=20)
main.style.map('TButton',
    foreground=[('disabled', 'black'),
                ('active', 'black')],
    background=[('disabled', '#02394A'),
                ('active', 'lightblue')]
)
main.style.configure('settings.TButton',
    font=('notosansbold', 10),
    foreground='white',
    background='#02394A')


homelbl = ttk.Label(main, text='Hydro Home', background='#02394A')
homelbl.grid(row=0, column=0, columnspan=4)
homelbl.configure(background='#02394A', font='notosansbold', foreground='white')

timelbl = ttk.Label(main, text=timeString)
timelbl.grid(row=0, column=4, columnspan=4)
timelbl.configure(background='#02394A', font='notosansbold', foreground='white')

templbl = ttk.Label(main, text='Local Temp')
templbl.grid(row=0, column=8, columnspan=4, sticky='e')
templbl.configure(background='#02394A', font='notosansbold', foreground='white')

# Nutrients Button, clicks into sub-menu
nutebtn = tk.Button(main,
                        text='Nutrients',
                        bg='#02394A',
                        activebackground='lightblue',
                        fg='white',
                        height=3,
                        width=12,
                        font=('notosansbold', 15))
nutebtn.grid(row=1, column=2, rowspan=2, columnspan=4, padx=5, pady=5)

# Lights Button, clicks into sub-menu
lightsbtn = tk.Button(main,
                        text=' Lights  ',
                        bg='#02394A',
                        activebackground='lightblue',
                        fg='white',
                        height=3,
                        width=12,
                        font=('notosansbold', 15))
lightsbtn.grid(row=1, column=6, rowspan=2, columnspan=4, padx=5, pady=5)

#fan on/off button
# Define our switch function
def fanSwitch():
    global fanOn 
    # Determine is on or off
    if fanOn:
        fanbtn.config(image = img_fanoff)
        fanOn = False
    else:
        fanbtn.config(image = img_fanon)
        fanOn = True
  

fanbtn = tk.Button(main,
                image=img_fanon,
                bg='#02394A',
                activebackground='#02394A',
                command=fanSwitch,
                border=0,
                highlightthickness=0,
                height=100,
                width=100)
fanbtn.grid(row=3, column=1, rowspan=3, columnspan=3)

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
  

o2btn = tk.Button(main,
                image=img_o2on,
                bg='#02394A',
                activebackground='#02394A',
                command=o2Switch,
                border=0,
                highlightthickness=0,
                height=100,
                width=100)
o2btn.grid(row=3, column=4, rowspan=3, columnspan=3)

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
  

h2obtn = tk.Button(main,
                image=img_h2oon,
                bg='#02394A',
                activebackground='#02394A',
                command=h2oSwitch,
                border=0,
                highlightthickness=0,
                height=100,
                width=100)
h2obtn.grid(row=3, column=7, rowspan=3, columnspan=3)


#settings button

settingsButton = tk.Button(main,
                           image=img_settings,
                           background='#02394A',
                           height=70,
                           width=70,
                           border=0,
                           activebackground='#02394A'
                           )
settingsButton.grid(row=9, column=9)


main.mainloop()

