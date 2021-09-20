import tkinter as tk
from tkinter import Frame, Grid, Label, ttk, font
import time
timeString = time.strftime('%I:%M %p')


main = tk.Tk()
main.title('Lettuce Wall')
main.configure(background='#02394A', width=700, height=700)


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
    background=[('disabled', 'grey'),
                ('active', 'lightblue')]
)
main.style.configure('settings.TButton',
    font=('notosansbold', 10),
    foreground='white',
    background='#02394A')

homeLabel = ttk.Label(main, text='Hydro Home', background='#02394A')
homeLabel.grid(row=0, column=0)
homeLabel.configure(background='#02394A', font='notosansbold', foreground='white')

timeLabel = ttk.Label(main, text=timeString)
timeLabel.grid(row=0, column=7, columnspan=6)
timeLabel.configure(background='#02394A', font='notosansbold', foreground='white')

tempLabel = ttk.Label(main, text='Local Temp')
tempLabel.grid(row=0, column=14, columnspan=6)
tempLabel.configure(background='#02394A', font='notosansbold', foreground='white')

nuteButton = ttk.Button(main, text='Nutrients', padding=25)
nuteButton.grid(row=1, column=0, columnspan=6, rowspan=6)
nuteButton.configure(style='')

lightsButton = ttk.Button(main, text='Lights', padding=25)
lightsButton.grid(row=1, column=6, rowspan=6, columnspan=6)

pumpsButton = ttk.Button(main, text='Pumps', padding=25)
pumpsButton.grid(row=1, column=12, rowspan=6, columnspan=6)

settingsButton = ttk.Button(main, text='Settings', padding=15, style='settings.TButton')
settingsButton.grid(row=14, column=15, rowspan=2, columnspan=3)

main.mainloop()


