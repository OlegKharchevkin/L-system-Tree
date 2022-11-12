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
basic_length = ui.scale()

turtle.hideturtle()
turtle.tracer(0) # настраиваем черепаху

config.read("config.ini") # читаем файл настроек

itr = int(config["Modes"]["iterations"]) # количество итераций

# считывание аксионы
axiom = []
if config["Modes"]["drawing"]=="3":
    with open(config["Files"]["save"], "r") as f:
        axiom=json.load(f)# загрузка сохранения
    itr=axiom[1]
else:
    with open(config["Files"]["axiom"], "r") as f:
    	axiom = json.load(f) # загрузка стандартной аксиомы
    	



if config["Modes"]["drawing"]!="3":
    for i in range(itr+1):
        axiom.append(tree.L_system(axiom[i])) # построение дерева
    for i in range(itr+1):
        ui.reset() # очистка экрана 
    if config["Modes"]["drawing"] == "2" or i == itr:
        length = (i + 1)**(-1) * basic_length 
        thin = 0.15 * basic_length 
        if config["Modes"]["number"] == "1":
            ui.num_of_itr(i) 
        if config["Modes"]["drawing"] in ["1","3"]:
            tree.output(axiom[i+1],thin,length,True) # отрисовка дерева
        else:
            tree.output(axiom[i+1],thin,length,False) # отрисовка дерева
            turtle.update()
        sleep(1)
else:
		ui.reset()
		if config["Modes"]["number"] == "1":
			ui.num_of_itr(itr)
		length = (itr + 1)**(-1) * basic_length 
		thin = 0.15 * basic_length 
		#print(axiom[0])
		tree.output(axiom[0],thin,length,True) # отрисовка дерева
		
if config["Modes"]["save"]=="1"and config["Modes"]["drawing"]!="3":
	with open(config["Files"]["save"],"w") as f:
		print('save')
		temp =[]
		temp.append(axiom[itr+1])
		temp.append(itr)
		json.dump(temp,f) # сохранение дерева
		


if config["Modes"]["goodbye"] == "1":
    ui.goodbye_msg()
turtle.update()
turtle.exitonclick()
turtle.mainloop()
