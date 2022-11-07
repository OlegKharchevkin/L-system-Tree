class UI:
    def __init__(self,turtle):
        self.turtle=turtle
    def reset(self):
        self.turtle.clear()
        self.turtle.penup()
        self.turtle.setposition(0,-300)
        self.turtle.seth(90)
        self.turtle.pendown()
    def num_of_itr(self,i):
        self.turtle.penup()
        self.turtle.setpos(-600,250)
        self.turtle.write(i,font=("Arial", 20, "normal"))
        self.turtle.setposition(0,-300)
        self.turtle.seth(90)
        self.turtle.pendown()
    def goodbye_msg(self):
        self.turtle.penup()   
        self.turtle.setpos(-600,250)
        self.turtle.right(180)
        self.turtle.forward(40)
        self.turtle.write("Click on screen to exit",font=("Arial", 20, "normal"))
    def fullscreen(self):
        """разворачивает окно на полный экран"""
        screen = self.turtle.Screen()
        screenTk = screen.getcanvas().winfo_toplevel()
        screenTk.attributes("-fullscreen", True)
    	