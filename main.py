# импортируем библиотеки
import turtle
from random import randint
from time import sleep
from Tree import Tree
from UI import UI
import json
import configparser 
# глубина массива
def depth(l):
    if isinstance(l, (list, tuple)):
        t = ()
        for itm in l:
            t += depth(itm),
        return 1 + max(t)
    return 0 
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
print(depth(axiom))

itr = int(config["Modes"]["iterations"])

if config["Modes"]["drawing"]!="3":
	for i in range(itr+1):
		axiom.append(tree.L_system(axiom[i]))
		
if config["Modes"]["save"]=="1":
	with open(config["Files"]["save"],"w") as f:
		json.dump(axiom, f)
elif config["Modes"]["save"]=="2":
	with open(config["Files"]["save"],"w") as f:
		json.dump(axiom[itr+1], f)
		

for i in range(itr+1):
    ui.reset()
    #if i >= 11: 
    tree.output(axiom[i+1],i*1.5)
    #f = open("lsys.txt","w")
	#f.write(str(axiom[i+1]))
    #f.close()
    ui.num_of_itr(i)
    turtle.update()
    #image = ImageGrab.grab()
    #image.save('scr'+str(itr)+'.png')
    sleep(1)

ui.goodbye_msg()
turtle.update()
turtle.exitonclick()
turtle.mainloop()
