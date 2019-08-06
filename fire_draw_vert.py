from tkinter import *
from scipy.stats import expon
import numpy as np
from random import randrange as variance

colors = (
    '#FFFFFF', 
    '#EFEFC7', 
    '#DFDF9F', 
    '#CFCF6F', 
    '#B7B737', 
    '#B7B72F', 
    '#B7AF2F', 
    '#BFAF2F', 
    '#BFA727', 
    '#BF9F1F', 
    '#C7971F', 
    '#C78F17', 
    '#C78717', 
    '#CF8717', 
    '#CF7F0F', 
    '#CF770F', 
    '#CF6F0F', 
    '#D7670F', 
    '#D75F07', 
    '#DF5707', 
    '#DF4F07', 
    '#C74707', 
    '#BF4707', 
    '#AF3F07', 
    '#9F2F07', 
    '#8F2707', 
    '#771F07', 
    '#671F07', 
    '#571707', 
    '#470F07', 
    '#2F0F07', 
    '#1F0707', 
    '#070707', 
    '#000000')

class Fire:

    def __init__(self, canvas, scale, max_height):
        # Seed the bottom row of the fire
        # Should be able to replace this with spots of fire later
        left_x = 0
        right_x = left_x + scale
        top_y = max_height - scale
        bottom_y = max_height
        for i in range(x_pixels):
            map[0,i] = w.create_rectangle(left_x, top_y, right_x, bottom_y, outline=colors[0], fill = colors[0])
            left_x += fire_scale
            right_x += fire_scale

    def fire_loop():
        for y in range(1,y_pixels):
            left_x = 0
            right_x = 0 + fire_scale
            top_y = canvas_height - ((y + 1) * fire_scale)
            bottom_y = canvas_height - (y * fire_scale)
            for x in range(x_pixels):
                color_index = colors.index(w.itemcget(map[y-1,x],"fill"))+1
                if variance(0,4) == 0: # 25% chance of increased decay
                    color_index += 1
                if color_index >= len(colors):
                    color_index = len(colors) - 1
                map[y,x] = w.create_rectangle(left_x, top_y, right_x, bottom_y, outline=colors[color_index], fill=colors[color_index])
                left_x += fire_scale
                right_x += fire_scale


master = Tk(className = 'FIRE')

canvas_width = 1000
canvas_height = 1000
fire_scale = 5

w = Canvas(master, width = canvas_width, height = canvas_height)

map = np.zeros([int(canvas_width/fire_scale), int(canvas_height/fire_scale)], dtype=int)

x_pixels, y_pixels = map.shape

# Seed the bottom row of the fire
# Should be able to replace this with spots of fire later
left_x = 0
right_x = left_x + fire_scale
top_y = canvas_height - fire_scale
bottom_y = canvas_height
for i in range(x_pixels):
    map[0,i] = w.create_rectangle(left_x, top_y, right_x, bottom_y, outline=colors[0], fill = colors[0])
    left_x += fire_scale
    right_x += fire_scale






master.geometry('1000x1000+0+0')
w.configure(background = 'black')
w.pack()
while True:
    fire_loop()
    master.update()