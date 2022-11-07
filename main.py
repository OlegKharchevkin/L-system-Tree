# импортируем библиотеки
import turtle
from random import randint
from time import sleep
from Tree import Tree
from UI import UI
import json
import configparser 
# создаем  объекты
config = configparser.ConfigParser()
ui = UI(turtle)
tree = Tree(turtle)

ui.fullscreen() # разворачиваем окно на полный экран

turtle.hideturtle()
turtle.tracer(0) # настраиваем черепаху

config.read("config.ini") # читаем файл настроек

# считывание аксионы
axiom = []
if config["Modes"]["drawing"]=="3":
    with open(config["Files"]["save"], "r") as f:
    	axiom = json.load(f) # загрузка сохранения
else:
    with open(config["Files"]["axiom"], "r") as f:
    	axiom = json.load(f) # загрузка стандартной аксиомы

itr = int(config["Modes"]["iterations"]) # количество итераций

if config["Modes"]["drawing"]!="3":
	for i in range(itr+1):
		axiom.append(tree.L_system(axiom[i])) # построение дерева
		
if config["Modes"]["save"]=="1":
	with open(config["Files"]["save"],"w") as f:
		json.dump(axiom[itr+1], f) # сохранение дерева
		

for i in range(itr+1):
    ui.reset() # очистка экрана 
    if config["Modes"]["drawing"] == "2" or i == itr:
        if config["Modes"]["number"] == "1":
            ui.num_of_itr(i) 
        if config["Modes"]["drawing"] in ["1","3"]:
            tree.output(axiom[i+1],i*1.5,10,True) # отрисовка дерева
        else:
            tree.output(axiom[i+1],i*1.5,10,False) # отрисовка дерева
        turtle.update()
        sleep(1)
if config["Modes"]["goodbye"] == "1":
    ui.goodbye_msg()
turtle.update()
turtle.exitonclick()
turtle.mainloop()
