# gui
# mvc pattern: model view controller

import tkinter

def click(var, value):
    counter.set(var.get() + value)

if __name__ == '__main__':
    window = tkinter.Tk()

    counter = tkinter.IntVar()
    counter.set(0)

    frame = tkinter.Frame(window)
    frame.pack()

    button = tkinter.Button(frame, text='Click +1', command=lambda: click(counter, 1))
    button.pack()

    button = tkinter.Button(frame, text='Click -1', command=lambda: click(counter, -1))
    button.pack()

    label = tkinter.Label(frame, textvariable=counter)
    label.pack()

    window.mainloop()

    