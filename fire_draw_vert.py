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

    def __init__(self, canvas, scale, max_height, max_width):
        self.canvas = canvas
        # Fill in all rectangles. start with one line of white and then black
        map = []
        
        for y in range(int(max_height/scale)):
            left_x = 0
            right_x = left_x + scale
            top_y = max_height - ((y+1) * scale)
            bottom_y = max_height - ((y) * scale)
            row = []
            for x in range(int(max_width/scale)):
                if y == 0:
                    color = colors[0]
                else:
                    color = colors[-1]
                row.append(w.create_rectangle(left_x, top_y, right_x, bottom_y, outline=color, fill = color))
                left_x += fire_scale
                right_x += fire_scale
            map.append(row)
        temp = []
        for row in map:
            temp.append(tuple(row))
        self.map = tuple(temp)

    def fire_loop(self):
        for y in range(1,len(self.map)):
            for x in range(len(self.map[y])):
                color_index = colors.index(w.itemcget(self.map[y-1][x],"fill")) + 1
                if variance(0,4) == 0: # 25% chance of increased decay
                    color_index += 1
                if color_index >= len(colors):
                    color_index = len(colors) - 1
                w.itemconfig(self.map[y][x], outline=colors[color_index], fill=colors[color_index])
        self.canvas.after(10,self.fire_loop)


master = Tk(className = 'FIRE')

canvas_width = 1000
canvas_height = 1000
fire_scale = 10

w = Canvas(master, width = canvas_width, height = canvas_height)

fire = Fire(w, fire_scale, canvas_height, canvas_width)






master.geometry('1000x1000+0+0')
w.configure(background = 'black')
w.pack()
fire.fire_loop()
master.mainloop()