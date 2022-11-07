class UI:
    def __init__(self,turtle):
        self.turtle=turtle
        screen = self.turtle.Screen()
        self.w = screen.getcanvas().winfo_screenwidth()
        self.h = screen.getcanvas().winfo_screenheight()
    def reset(self):
        self.turtle.clear()
        self.turtle.penup()
        self.turtle.setposition(0,-300)
        self.turtle.seth(90)
        self.turtle.pendown()
    def num_of_itr(self,i):
        self.turtle.penup()
        self.turtle.setpos(-(self.w/2)+(self.w/16),(self.h/2)-(self.h/9))
        self.turtle.write(i,font=("Arial", int(self.w/80), "normal"))
        self.turtle.setposition(0,-300)
        self.turtle.seth(90)
        self.turtle.pendown()
    def goodbye_msg(self):
        self.turtle.penup()   
        self.turtle.setpos(-(self.w/2)+(self.w/16),(self.h/2)-(self.h/4.5))
        self.turtle.write("Click on screen to exit",font=("Arial", int(self.w/80), "normal"))
    def fullscreen(self):
        """разворачивает окно на полный экран"""
        screen = self.turtle.Screen()
        screenTk = screen.getcanvas().winfo_toplevel()
        screenTk.attributes("-fullscreen", True)
    def scale(self):
        screen = self.turtle.Screen()
        