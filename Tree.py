from random import randint
class Tree:
    def __init__(self,turtle):
            self.turtle = turtle
            self.thin = []
            self.turtles = []
            for i in range(81):
                self.turtles.append(turtle.Turtle("turtle"))
                self.turtles[i].speed(0)
                self.turtles[i].hideturtle()
            for i in range(100):
                self.thin.append(2**(-i/2))
    def L_system(self,axiom):
        axmTemp = []
        for ch in axiom:
            if ch[0] == '0':
                if randint(0,100) > 30:
                    axmTemp.append(["1",ch[1],ch[3]])
                    axmTemp.append(["["])
                    axmTemp.append(["-",randint(5,27)])
                    axmTemp.append(["2",ch[1]+1,randint(0,10)>4])
                    axmTemp.append(["0",ch[1]+1, randint(0,10),randint(0,2)==2])
                    axmTemp.append(["]"])
                    axmTemp.append(["["])
                    axmTemp.append(["+",randint(5,27)])
                    axmTemp.append(["2",ch[1]+1,randint(0,10)>4])
                    axmTemp.append(["0",ch[1]+1,randint(0,10),randint(0,2)==2])
                    axmTemp.append(["]"])
                else:
                    axmTemp.append(["1",ch[1],ch[3]])
                    axmTemp.append(["["])
                    axmTemp.append(["-",randint(5,27)])
                    axmTemp.append(["2",ch[1]+1,randint(0,10)>4])
                    axmTemp.append(["0",ch[1]+1, randint(0,10),randint(0,2)==2])
                    axmTemp.append(["]"])
                    axmTemp.append(["["])
                    axmTemp.append(["+",randint(5,27)])
                    axmTemp.append(["2",ch[1]+1,randint(0,10)>4])
                    axmTemp.append(["0",ch[1]+1,randint(0,10),randint(0,2)==2])
                    axmTemp.append(["]"])
                    axmTemp.append(["["])
                    axmTemp.append(["!",randint(-11,10)])
                    axmTemp.append(["2",ch[1]+1,randint(0,10)>4])
                    axmTemp.append(["0",ch[1]+1,randint(0,10),randint(0,2)==2])
                    axmTemp.append(["]"])
            elif ch[0] == '1':
                axmTemp.append(["2",ch[1],randint(0,10)>4])
                axmTemp.append(["1",ch[1],ch[2]])
            elif ch[0] == '2':
                if randint(0,100) < 12 and ch[1] > 3 :
                    ug = randint(-30,30)
                    axmTemp.append(["3",ch[1],randint(0,10)>4])
                    axmTemp.append(["["])
                    axmTemp.append(["^",ug-25 if ug <= 0 else ug+25])
                    axmTemp.append(["3",ch[1]+1,randint(0,10)>4])
                    axmTemp.append(["0",ch[1]+1,randint(0,10),randint(0,2)==2])
                    axmTemp.append(["]"])
                else:
                    axmTemp.append(["2",ch[1],ch[2]])
            else:
                axmTemp.append(ch)
        return axmTemp
    def output(self,axiom,thin,length,update):
        stc = []
        shoot = [0,0]
        for ch in axiom:
            if   ch[0] == "+":
                self.turtle.right(ch[1])
            elif ch[0] == "-":
                self.turtle.left(ch[1])
            elif ch[0] == "!":
                self.turtle.left(ch[1])
            elif ch[0] == "^":
                self.turtle.left(ch[1])
            elif ch[0] == "[":
                if shoot[0] != 0:
                    self.turtle.pensize(thin*self.thin[shoot[1]])
                    self.turtle.forward(shoot[0])
                    shoot = [0,0]
                stc.append(self.turtle.pos())
                stc.append(self.turtle.heading())     
            elif ch[0] == "]":
                self.turtle.penup()
                self.turtle.setheading(stc.pop())
                self.turtle.setpos(stc.pop())
                self.turtle.pendown()
            elif ch[0] == "0":
                if shoot[0] != 0:
                    self.turtle.pensize(thin*self.thin[shoot[1]])
                    self.turtle.forward(shoot[0])
                    shoot = [0,0]
                self.turtle.pensize(4)
                r = ch[2]
                if r<3:
                        self.turtle.pencolor('#009900')
                elif r>6:
                        self.turtle.pencolor('#667900')
                else:
                        self.turtle.pencolor('#20BB00')
                if ch[3] :self.turtle.forward(8)   
                self.turtle.pencolor('#000000')
            else:
                if ch[2]:
                    shoot = [shoot[0]+length,ch[1]]
            if update: self.turtle.update()
                    
