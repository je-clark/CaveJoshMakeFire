from tkinter import *
from scipy.stats import expon
import numpy as np
from random import randrange as variance
from timeit import default_timer as timer
import copy

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
        temp = []
        for row in map:
            temp.append(tuple(row))
        self.map = tuple(temp)

    def fire_loop(self):
        #start = timer()
        color_list_len = len(colors)
        for y in range(1,len(self.map)):
            for x in range(len(self.map[y])):
                start_loop = timer()
                try:
                    #left = colors.index(w.itemcget(self.map[y][x-1],"fill"))
                    left = self.map[y][x-1][1]
                except:
                    left = color_list_len - 1
                    pass
                try:
                    #right = colors.index(w.itemcget(self.map[y][x+1],"fill"))
                    right = self.map[y][x+1][1]
                except:
                    right = color_list_len - 1
                try:
                    #below = colors.index(w.itemcget(self.map[y-1][x],"fill"))
                    below = self.map[y-1][x][1]
                except:
                    below = color_list_len - 1
                lookups = timer()
                adjacencies = [left, right]
                if variance(0,4) == 0:
                    color_index = min(adjacencies) + 1
                else:
                    color_index = below #+ 1
                if variance(0,3) == 0: 
                    color_index += 1
                if color_index >= color_list_len:
                    color_index = color_list_len - 1
                rand_calls = timer()
                w.itemconfig(self.map[y][x][0], outline=colors[color_index], fill=colors[color_index])
                self.map[y][x][1] = color_index
                print(f"Lookups occurred in {lookups-start_loop} sec, while random calls occurred in {rand_calls-lookups} sec.")
        #print(f"fire_loop completed in {timer() - start}")
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