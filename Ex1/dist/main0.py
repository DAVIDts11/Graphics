# Submitted  by : Tsibulsky David  309444065
#                   and Haham Omri 308428226

from tkinter import *
import math


# Global variables:

WIDTH = 640
HEIGHT = 480

N=10  # amount of lines in bezier curve

mouse_points = {"MOUSE_CLICK_POS_1_X":0,"MOUSE_CLICK_POS_1_Y":0,
                "MOUSE_CLICK_POS_2_X":0,"MOUSE_CLICK_POS_2_Y":0}
additional_points = {"X1":0,"Y1":0,"X2":0,"Y2":0}
mouse_click_counter = 0
color = "blue"     # color of pixels


def draw_shapes():
    """
    Draw three shapes on the canvas  :  parallelogram  , bezier curve ,  and circle .
        uses global variables of two mouse clicked points  parameters .
    """
    global  mouse_points, color ,img
    img = PhotoImage(width=WIDTH, height=HEIGHT)
    my_canvas.create_image((WIDTH / 2, HEIGHT / 2), image=img, state='normal')
    nubmer_N_text = f"Number of lines in curve is:  {N}"
    my_canvas.create_text(300, 10, fill="darkblue", font="Times 20 italic bold",
                          text=nubmer_N_text)
    color = "blue"
    my_parallelogram(mouse_points["MOUSE_CLICK_POS_1_X"], mouse_points["MOUSE_CLICK_POS_1_Y"],
                     mouse_points["MOUSE_CLICK_POS_2_X"], mouse_points["MOUSE_CLICK_POS_2_Y"])

    x_center = (mouse_points["MOUSE_CLICK_POS_1_X"] + mouse_points["MOUSE_CLICK_POS_2_X"]) // 2
    y_center = (mouse_points["MOUSE_CLICK_POS_1_Y"] + mouse_points["MOUSE_CLICK_POS_2_Y"]) // 2
    radius = math.sqrt((mouse_points["MOUSE_CLICK_POS_1_X"] - mouse_points["MOUSE_CLICK_POS_2_X"]) ** 2 +
                       (mouse_points["MOUSE_CLICK_POS_1_Y"] - mouse_points["MOUSE_CLICK_POS_2_Y"]) ** 2) // 2

    my_circle(x_center, y_center, int(radius))

    color = "black"
    my_bezier_curve(mouse_points["MOUSE_CLICK_POS_1_X"], mouse_points["MOUSE_CLICK_POS_1_Y"], additional_points["X1"],
                    additional_points["Y1"], additional_points["X2"], additional_points["Y2"],
                    mouse_points["MOUSE_CLICK_POS_2_X"], mouse_points["MOUSE_CLICK_POS_2_Y"], N)



def getxy(event):
    """
    get the mouse click params MOUSE_CLICK_POS_1_X, MOUSE_CLICK_POS_1_X (for first click),
                          MOUSE_CLICK_POS_2_X,  MOUSE_CLICK_POS_2_Y (for second click).
            and draw the shapes on any second one .
    :param event:
    """
    global mouse_click_counter , mouse_points
    if (mouse_click_counter %2 == 0):
        mouse_points["MOUSE_CLICK_POS_1_X"] = event.x
        mouse_points["MOUSE_CLICK_POS_1_Y"] = event.y
    else:
        mouse_points["MOUSE_CLICK_POS_2_X"] = event.x
        mouse_points["MOUSE_CLICK_POS_2_Y"] = event.y
        draw_shapes()
    mouse_click_counter = mouse_click_counter + 1


def delete():
    """
     To clear all the canvas
     """
    my_canvas.delete('all')


def increase_lines():
    """
     Increase number of lines in the curve by 1 and draw the shapes again .
    """
    global N ,mouse_click_counter
    if (mouse_click_counter>0 and mouse_click_counter % 2 == 0  ):
        N=N+1
        delete()
        draw_shapes()


def decrease_lines():
    """
     Decrease number of lines in the curve by 1 and draw the shapes again .
    """
    global N ,mouse_click_counter
    if (mouse_click_counter>0 and mouse_click_counter % 2 == 0):
        N=N-1
        delete()
        draw_shapes()


def my_line(x1,y1,x2,y2):
    """
     draw DDA line on the canvas
     :param x1 , y1 :  line start point
     :param x2 , y2 :  line end point
    """
    x,y = x1,y1
    DX = (x2-x1)
    DY = (y2-y1)
    RANGE = int(max(abs(DX),abs(DY)))
    dX = DX/RANGE
    dY = DY/RANGE
    for i in range(RANGE):
        img.put(color,(int(x),int(y)))
        x=x+dX
        y=y+dY


def my_parallelogram(x1,y1,x2,y2):
    """
     Draw parallelogram on the canvas with two given angels
    :param x1 ,y1: first angle point
    :param x2 ,y2: second angle point
    """
    global additional_points
    additional_points["Y1"] = y1
    additional_points["Y2"] = y2
    if((x1<x2 and y1<y2) or (x1<x2 and y1>y2) ) :
        additional_points["X1"] = x1 + 100
        additional_points["X2"] =  x2 - 100
    else:
        additional_points["X1"] = x1 - 100
        additional_points["X2"] = x2 + 100

    my_line(x1, y1, x2, y2)
    my_line(additional_points["X1"],additional_points["Y1"] ,additional_points["X2"], additional_points["Y2"])
    my_line(x1, y1,additional_points["X2"], additional_points["Y2"])
    my_line(x1, y1, additional_points["X1"],additional_points["Y1"])
    my_line(additional_points["X1"],additional_points["Y1"], x2, y2)
    my_line(additional_points["X2"], additional_points["Y2"], x2, y2)


def plot_circle_points(x_center,y_center,x,y):
    """
    Put  eight  points  on the circle by given original one  .
    :param x_center , y_center: center of the circle
    :param x,y: original point
    """
    img.put("red",(x_center + x, y_center + y))
    img.put("red", (x_center - x, y_center + y))
    img.put("red",(x_center + x, y_center - y))
    img.put("red",(x_center - x, y_center - y))
    img.put("red",(x_center + y, y_center + x))
    img.put("red",(x_center - y, y_center + x))
    img.put("red",(x_center + y, y_center - x))
    img.put("red",(x_center - y, y_center - x))


def my_circle(x_center,y_center,radius):
    """
    Draw circle on the canvas with  given center and radius .
    :param x_center ,y_center : center of the circle
    :param radius: radius of the circle
    """
    x=0
    y=radius
    p=3-2*radius
    while (x <= y):
        plot_circle_points(x_center,y_center ,x,y)
        if(p < 0):
            p = p + 4 * x + 6
        else:
            p = p + 4 * (x - y) + 10
            y = y-1
        x = x + 1


def my_bezier_curve(x1, y1, x2, y2, x3, y3, x4, y4, n):
    """
    Draw bezier curve by  given four points ant number of lines in the curve
    :param x1 ,y1: first point
    :param x2 ,y2: second point
    :param x3 ,y3: third  point
    :param x4 ,y4: forth  point
    :param n: number of lines to draw
    """
    ax = 3*x2 + x4 - 3*x3 - x1
    bx = 3*x1 - 6*x2 + 3*x3
    cx = 3*x2 - 3*x1
    dx = x1
    ay = 3*y2 + y4 - 3*y3 - y1
    by = 3*y1 - 6*y2 + 3*y3
    cy = 3*y2 - 3*y1
    dy = y1
    t = 0
    points = list()
    points.append((round(x1), round(y1)))
    for _ in range(n):
        t += 1/n
        xt = ax * (t**3) + bx * (t**2) + cx * t + dx
        yt = ay * (t**3) + by * (t**2) + cy * t + dy
        points.append((round(xt), round(yt)))
    for i in range(len(points)-1):
        my_line(points[i][0], points[i][1], points[i+1][0], points[i+1][1])


# Windows and canvas definitions  :
my_window = Tk()
my_window.title("Targil 1")
my_canvas = Canvas(my_window,width= WIDTH, height= HEIGHT,background = 'white')
my_canvas.grid(row=0,column=0 ,columnspan = 4)
img = PhotoImage(width=WIDTH,height=HEIGHT)
my_canvas.create_image((WIDTH/2,HEIGHT/2),image =img,state='normal')

# Buttons :
button = Button(my_window, text="Delete",width = 20,bg="white",fg="blue",  command=delete)
button1 = Button(my_window, text="Increase",width = 13,bg ="green",fg="white", command=increase_lines)
button2 = Button(my_window, text="Decrrase",width = 13,bg ="red",fg="white", command=decrease_lines)

button.grid(row=1, column=0)
button1.grid(row=1, column=2)
button2.grid(row=1, column=3)

my_canvas.bind('<Button-1>', getxy)

my_window.mainloop()



