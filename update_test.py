'''

KEY BITS OF STUFF LEARNED:

1. Create a class, and use the after() method to update your item
2. Use mainloop() and let Tkinter call your update stuff on its own
3. Use itemconfig() to update the existing rectangle instead of creating new objects

'''


from tkinter import *

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

    def __init__(self, canvas):
        self.canvas = canvas
        self.oid = w.create_rectangle(0,0,100,100, outline=colors[0], fill=colors[0])

    def fire_loop(self):
        color_index = colors.index(w.itemcget(self.oid,"fill"))+1
        if color_index >= len(colors):
            color_index = 0
        w.itemconfig(self.oid, outline=colors[color_index], fill=colors[color_index])
        self.canvas.after(10,self.fire_loop)

master = Tk(className = 'FIRE')

canvas_width = 1000
canvas_height = 1000

w = Canvas(master, width = canvas_width, height = canvas_height)
fire = Fire(w)
master.geometry('1000x1000+0+0')
w.configure(background = 'black')
w.pack()

fire.fire_loop()
master.mainloop()