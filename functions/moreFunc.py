# Plotting a function:
import tkinter


# Creating a parabola function:


def parabola(x):
    y = (x**2) / 100
    return y

# Making an axis

def draw_axis(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() /2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill='black')
    canvas.create_line(0, y_origin, 0, -y_origin, fill='black')
    print(locals())     # locals() function allows you to print local variables for a function. It prints all variables
    # that have been defined for use by the function.

# Plotting Function.

def plot(canvas, x, y):
    canvas.create_line(x, y, x + 1, y + 1, fill="red")

mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry('640x480')

canvas = tkinter.Canvas(mainWindow, width=320, height=480)
canvas.grid(row=0, column=0)    # Canvas lets you draw shapes on the window, like parabolas.

canvas2 = tkinter.Canvas(mainWindow, width=320, height=480, background="blue")
canvas2.grid(row=0, column=1)

print(repr(canvas)) # repr method allows you to print a report of the object in question.
print(repr(canvas2))
draw_axis(canvas)
draw_axis(canvas2)

for x in range(-100, 100):
    y = parabola(x)
    print(y)
    plot(canvas, x, -y)

mainWindow.mainloop()