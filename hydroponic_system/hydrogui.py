import tkinter as tk
from tkinter import Button, Frame, Grid, Image, Label, PhotoImage, ttk, font
import time
timeString = time.strftime('%I:%M %p')

main = tk.Tk()
main.title('Lettuce Wall')
main.configure(background='#02394A', width=700, height=700)
#test
img_fanoff = PhotoImage(file='hydroponic_system/assets/fanoff.png')
img_fanon = PhotoImage(file='hydroponic_system/assets/fanon.png')
img_o2off = PhotoImage(file='hydroponic_system/assets/o2off.png')
img_o2on = PhotoImage(file='hydroponic_system/assets/o2on.png')
img_h2ooff = PhotoImage(file='hydroponic_system/assets/h2ooff.png')
img_h2oon = PhotoImage(file='hydroponic_system/assets/h2oon.png')
img_settings = PhotoImage(file='hydroponic_system/assets/settings.png')

#global is_on function
is_on = False

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
homelbl.grid(row=0, column=0)
homelbl.configure(background='#02394A', font='notosansbold', foreground='white')

timelbl = ttk.Label(main, text=timeString)
timelbl.grid(row=0, column=5, columnspan=5)
timelbl.configure(background='#02394A', font='notosansbold', foreground='white')

templbl = ttk.Label(main, text='Local Temp')
templbl.grid(row=0, column=10, columnspan=5, sticky='e')
templbl.configure(background='#02394A', font='notosansbold', foreground='white')

# Nutrients Button, clicks into sub-menu
nutebtn = tk.Button(main,
                        text='Nutrients',
                        bg='#02394A',
                        activebackground='lightblue',
                        fg='white',
                        height=3,
                        width=11,
                        font=('notosansbold', 15))
nutebtn.grid(row=1, column=2, rowspan=5, columnspan=5, padx=5, pady=5)

# Lights Button, clicks into sub-menu
lightsbtn = tk.Button(main,
                        text='Lights',
                        bg='#02394A',
                        activebackground='lightblue',
                        fg='white',
                        height=3,
                        width=11,
                        font=('notosansbold', 15))
lightsbtn.grid(row=1, column=9, rowspan=5, columnspan=5, padx=5, pady=5)

#fan on/off button
# Define our switch function
def switch():
    global is_on
      
    # Determine is on or off
    if is_on:
        fanbtn.config(image = img_fanoff)
        is_on = False
    else:
        fanbtn.config(image = img_fanon)
        is_on = True
  

fanbtn = tk.Button(main,
                image=img_fanon,
                bg='#02394A',
                activebackground='#02394A',
                command=switch,
                border=0,
                highlightthickness=0,
                borderwidth=0,
                height=100,
                width=100)
fanbtn.grid(row=8, column=0, rowspan=6, columnspan=6)

#o2 pump on/off switch

# Define our switch function
def switch():
    global is_on
      
    # Determine is on or off
    if is_on:
        o2btn.config(image = img_o2off)
        is_on = False
    else:
        o2btn.config(image = img_o2on)
        is_on = True
  

o2btn = tk.Button(main,
                image=img_o2on,
                bg='#02394A',
                activebackground='#02394A',
                command=switch,
                border=0,
                highlightthickness=0,
                height=100,
                width=100)
o2btn.grid(row=8, column=4, rowspan=6, columnspan=6)

#water pump on/off switch

# Define our switch function
def switch():
    global is_on
      
    # Determine is on or off
    if is_on:
        h2obtn.config(image = img_h2ooff)
        is_on = False
    else:
        h2obtn.config(image = img_h2oon)
        is_on = True
  

h2obtn = tk.Button(main,
                image=img_h2oon,
                bg='#02394A',
                activebackground='#02394A',
                command=switch,
                border=0,
                highlightthickness=0,
                height=100,
                width=100)
h2obtn.grid(row=8, column=9, rowspan=6, columnspan=6)


#settings button

settingsButton = tk.Button(main,
                           image=img_settings,
                           background='#02394A',
                           height=70,
                           width=70,
                           border=0,
                           highlightthickness=0,
                           activebackground='#02394A'
                           )
settingsButton.grid(row=14, column=15, rowspan=2, columnspan=3)

main.mainloop()

