from tkinter import *
from scipy.stats import expon

def create_row(canvas, row_no, max_width, max_height, scale, color):
    top_y = max_height - ((row_no + 1) * scale)
    bottom_y = max_height - (row_no * scale)
    left_x = 0
    right_x = 0 + scale
    oid_list = []
    for i in range(0,max_width,scale):
        
        oid_list.append(canvas.create_rectangle(left_x, top_y, right_x, bottom_y, outline = color, fill = color))
        left_x = left_x + scale
        right_x = right_x + scale
    return oid_list

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

master = Tk(className = 'FIREEEE!!!!!!')

w = Canvas(master, width = 1000, height = 1000)

fire_scale = 10

# We didn't start the fire
always_burning = create_row(w, 0, 1000, 1000, fire_scale, "#FFFFFF")

map = []
for fire in always_burning:
    map.append([fire])



i = 1
for color in colors:
    oid_list = create_row(w, i, 1000, 1000, 10, color)
    j = 0
    for oid in oid_list:
        map[j].append(oid)
        j += 1
    i += 1

for items in map:
    for item in items:
        print(w.itemcget(item, "fill"))

master.geometry('1000x1000+0+0')
w.configure(background = 'black')
w.pack()
master.mainloop()