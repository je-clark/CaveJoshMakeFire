from tkinter import *
from scipy.stats import expon
import numpy as np
from random import randrange as variance
from timeit import default_timer as timer
from numba import njit

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

@njit
def compute_new_color(map):
    color_list_len = len(colors)
    for y in range(1,len(map)):
        for x in range(1,len(map[y])-1): # adding explicit bounds to avoid out of bounds in lookup
            left = map[y][x-1][1]
            right = map[y][x+1][1]
            below = map[y-1][x][1]
            adjacencies = [left, right]
            if variance(0,4) == 0:
                color_index = min(adjacencies) + 1
            else:
                color_index = below #+ 1
            if variance(0,3) == 0: 
                color_index += 1
            if color_index >= color_list_len:
                color_index = color_list_len - 1
            map[y][x][1] = color_index
    return map

class Fire:

    def __init__(self, canvas, scale, max_height, max_width):
        self.canvas = canvas
        # Fill in all rectangles. start with one line of white and then black
        map = []
        color_list_len = len(colors)
        for y in range(int(max_height/scale)):
            left_x = 0
            right_x = left_x + scale
            top_y = max_height - ((y+1) * scale)
            bottom_y = max_height - ((y) * scale)
            middle_fifth = 2*int((max_width/scale)/5)
            row = []
            for x in range(int(max_width/scale)):
                if (y == 0) and (middle_fifth <= x <= (int(max_width/scale)-middle_fifth)):
                    color_index = 0
                else:
                    color_index = color_list_len - 1
                row.append([w.create_rectangle(left_x, top_y, right_x, bottom_y, outline=colors[color_index], fill = colors[color_index]),color_index])
                left_x += fire_scale
                right_x += fire_scale
            map.append(row)
        self.map = np.array(map)
        print("Created initial map")




    def fire_loop(self):
        start = timer()
        self.map = compute_new_color(self.map)
        new_color_time = timer()
        for y in range(1,len(self.map)):
            for x in range(1,len(self.map[y])-1):
                w.itemconfig(self.map[y][x][0], outline=colors[self.map[y][x][1]], fill=colors[self.map[y][x][1]])
        print(f"Computed new color in {new_color_time - start} sec. Updated colors in {timer() - new_color_time} sec.")
        self.canvas.after(100,self.fire_loop)


master = Tk(className = 'FIRE')

fire_scale = 10
canvas_width = 1000
canvas_height = (fire_scale * len(colors))*3


w = Canvas(master, width = canvas_width, height = canvas_height)

fire = Fire(w, fire_scale, canvas_height, canvas_width)






master.geometry(f'{canvas_width}x{canvas_height}+0+0')
w.configure(background = 'black')
w.pack()
fire.fire_loop()
master.mainloop()