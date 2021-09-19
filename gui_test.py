from tkinter import Grid
from guizero import App, Text, TextBox, yesno, warn, error, PushButton, Box, Window

def open_nutes():
    nutrients_page.show()

def close_nutes():
    nutrients_page.hide() 

app = App(title ="Hydro Village", bg="#C5D1EB")
title_box = Box(app, align="top")
intro_text = Text(title_box, text="Hydro Home", size=15, font="Arial", align="left", color="#02394A")
time_text = Text(title_box, text="4:45", size=15, font="Arial", align="left", color="#02394A")
temp_text = Text(title_box, text="75.6f", size=15, font="Arial", align="right", color="#02394A")

buttons_box = Box(app, layout="grid", width="fill")
nutrients_display = PushButton(buttons_box, text="Nutrients", height=3, grid=(0,0), command=open_nutes)
humidity_display = PushButton(buttons_box, text="Humidity", height=3, grid=(1,0))
lights_display = PushButton(buttons_box, text="Lights", padx=20, pady=10, height=3, grid=(2,0))

# following code for Nutrients page
nutrients_page = Window(app, title="Nutrients", bg="#C5D1EB")

nutrients_title_box = Box(nutrients_page, align="top")
nutrients_intro_text = Text(nutrients_title_box, text="Hydro Home", size=15, font="Arial", align="left", color="#02394A")
nutrients_time_text = Text(nutrients_title_box, text="4:45", size=15, font="Arial", align="left", color="#02394A")
nutrients_temp_text = Text(nutrients_title_box, text="75.6f", size=15, font="Arial", align="right", color="#02394A")
nutrients_info_text = Text(nutrients_page, text="This build is set up to use General Hydroponics Flora series Nutrients and ph Up and Down. Check your product if you are using different nutrients.")
nute_button_box = Box(nutrients_page, layout="grid", width="fill")
flora_gro_button = PushButton(nute_button_box, text="Add FloraGro", grid=(0,0))
flora_micro_button = PushButton(nute_button_box, text="Add FloraMicro", grid=(1,0))
flora_bloom_button = PushButton(nute_button_box, text="Add FloraBloom", grid=(2,0))
ph_up_button = PushButton(nute_button_box, text="Add ph Up", grid=(0,1))
ph_down_button = PushButton(nute_button_box, text="Add ph Down", grid=(1,1))

# following code for Humidity page

# following code for Lights page
app.display()