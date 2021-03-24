from tkinter import *

root = Tk()
root.geometry('700x600')
root.title('Draw')

def show(event):
    x = event.x
    y = event.y
    statusbar.configure(text='{},{}'.format(x,y))

def draw(event):
    x1 = event.x-2
    y1 = event.y-2
    x2 = event.x+2
    y2 = event.y+2

    canvas.create_oval(x1,y1,x2,y2,fill='black')

canvas = Canvas(root,bg='white')
canvas.pack(fill=BOTH,expan=YES)
#status bar
statusbar = Label(root,text='cursor pos:',font=('corbel',20),bg='black',fg='white')
statusbar.pack(side=BOTTOM,fill=X)

root.bind('<B1-Motion>',show)
canvas.bind('<B1-Motion>',draw)
root.mainloop()