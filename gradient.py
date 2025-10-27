from turtle import *

tom = Turtle()
tom.shape('turtle')
tom.speed(0)

def cube ():
    tom.begin_fill()
    for i in range (4):
        tom.fd(50)
        tom.rt(90)
    tom.end_fill()




def cube2 ():
    tom.begin_fill()
    tom.fd(l1)
    tom.rt(90)
    tom.fd(l2)
    tom.rt(90)
    tom.fd(l1)
    tom.rt(90)
    tom.fd(l2)
    tom.end_fill()

def coordinate():
    tom.penup()
    tom.goto(coord1, coord2)

def gradient1 ():
    tom.pd()
    tom.color("#4A148C")
    cube2()

def gradient2 ():
    tom.pd()
    tom.color("#6A1B9A")
    cube2()

def gradient3():
    tom.pd()
    tom.color("#7B1FA2")
    cube2()

def gradient4():
    tom.pd()
    tom.color("#8E24AA")
    cube2()

def gradient5():
    tom.pd()
    tom.color("#9C27B0")
    cube2()

def gradient6():
    tom.pd
    tom.color("#AB47BC")
    cube2()

def gradient7():
    tom.pd()
    tom.color("#BA68C8")
    cube2()

def gradient8():
    tom.pd()
    tom.color("#CE93D8")
    cube2()

def gradient9():
    tom.pd()
    tom.color("#E1BEE7")
    cube2()

def gradient10():
    tom.pd()
    tom.color("#F3E5F5")
    cube2()

def gradient11():
    tom.pd()
    tom.color("#FCE4EC")
    cube2()

def gradient12():
    tom.pd()
    tom.color("#F8BBD0")
    cube2()

def gradient13():
    tom.pd()
    tom.color("#F48FB1")
    cube2()

def gradient14():
    tom.pd()
    tom.color("#F06292")
    cube2()

def gradient15():
    tom.pd()
    tom.color("#EC407A")
    cube2()

def gradient16():
    tom.pd()
    tom.color("#E91E63")
    cube2()

coord1=-450
coord2=-300
l1=1000
l2=50
coordinate()
tom.pd()
gradient15()

coord1=-450
coord2=-300
l1=50
l2=1000
coordinate()
tom.pd()
gradient14()

coord1=550
coord2=-250
l1=1000
l2=50
coordinate()
tom.pd()
gradient13()

coord1=550
coord2=-150
l1=50
l2=1000
coordinate()
tom.pd()
gradient12()

coord1=-450
coord2=-100
l1=1000
l2=50
coordinate()
tom.pd()
gradient11()

coord1=-450
coord2=-100
l1=50
l2=1000
coordinate()
tom.pd()
gradient10()

coord1=550
coord2=-50
l1=1000
l2=50
coordinate()
tom.pd()
gradient9()

coord1=550
coord2=50
l1=50
l2=1000
coordinate()
tom.pd()
gradient8()

coord1=-450
coord2=100
l1=1000
l2=50
coordinate()
tom.pd()
gradient7()

coord1=-450
coord2=100
l1=50
l2=1000
coordinate()
tom.pd()
gradient6()

coord1=550
coord2=150
l1=1000
l2=50
coordinate()
tom.pd()
gradient5()

coord1=550
coord2=250
l1=50
l2=1000
coordinate()
tom.pd()
gradient4()

coord1=-450
coord2=300
l1=1000
l2=50
coordinate()
tom.pd()
gradient3()

coord1=-450
coord2=300
l1=50
l2=1000
coordinate()
tom.pd()
gradient2()

coord1=550
coord2=350
l1=1000
l2=50
coordinate()
tom.pd()
gradient1()

coord1=550
coord2=-350
l1=50
l2=1000
coordinate()
tom.pd()
gradient16()

def light ():
    tom.pd()
    tom.color('#bd6a28')
    cube()

def teal():
    tom.pd()
    tom.color('#a85f58')
    cube()

def dbrown():
    tom.pd()
    tom.color('#552925')
    cube()

def blue():
    tom.pd()
    tom.color('#a05611')
    cube()

def black():
    tom.pd()
    tom.color('#331712')
    cube()

def brown():
    tom.pendown()
    tom.color('#7e3f39')
    cube()

def dblack():
    tom.pd()
    tom.color('#532B0B')
    cube()

tom.penup()
tom.goto(-250,-300)
black()

tom.penup()
tom.goto(-200,-300)
black()

tom.penup()
tom.goto(-300,-250)
black()

tom.penup()
tom.goto(-300,-200)
dblack()

tom.pu()
tom.goto(-250,-200)
brown()

tom.pu()
tom.goto(-250,-250)
brown()

tom.pu()
tom.goto(-200,-250)
brown()

tom.pu()
tom.goto(-200,-200)
light()

tom.pu()
tom.goto(-200,-150)
light()

tom.pu()
tom.goto(-150,-150)
light()

tom.penup()
tom.goto(-250,-150)
dblack()

tom.penup()
tom.goto(-200,-100)
dblack()

tom.penup()
tom.goto(-150,-100)
blue()

tom.penup()
tom.goto(-150,-200)
blue()

tom.penup()
tom.goto(-150,-250)
black()

tom.penup()
tom.goto(-150,-50)
dbrown()

tom.penup()
tom.goto(-150,0)
brown()

tom.penup()
tom.goto(-100,-50)
teal()


tom.penup()
tom.goto(-100,-150)
blue()

tom.penup()
tom.goto(-100,-100)
black()

tom.penup()
tom.goto(-100,-200)
dblack()

tom.pu()
tom.goto(-100,-50)
teal()

tom.pu()
tom.goto(-100,0)
teal()

tom.pu()
tom.goto(-100,50)
brown()

tom.pu()
tom.goto(-50,50)
teal()

tom.pu()
tom.goto(-50,0)
teal()


tom.penup()
tom.goto(-50,100)
brown()

tom.penup()
tom.goto(-50,150)
blue()

tom.penup()
tom.goto(-50,-50)
brown()

tom.penup()
tom.goto(-50,-100)
dbrown()

cube()

tom.penup()
tom.goto(-50,-150)
black()

tom.penup()
tom.goto(0,-150)
black()

tom.penup()
tom.goto(0,-100)
dbrown()

tom.pu()
tom.goto(0,-50)
dbrown()

tom.pu()
tom.goto(50,-50)
dbrown()

tom.penup()
tom.goto(50,-100)
black()

tom.pu()
tom.goto(0,0)
brown()



def yellow():
    tom.pd()
    tom.color('#f4e063')
    cube()

def dyellow():
    tom.pd()
    tom.color('#de923a')
    cube()

def bryellow():
    tom.pd()
    tom.color('#bd6a28')
    cube()

def white():
    tom.pd()
    tom.color("#FFFFFF")
    cube()

tom.pu()
tom.goto(0,50)
yellow()

tom.pu()
tom.goto(0,100)
yellow()

tom.pu()
tom.goto(50,50)
yellow()

tom.pu()
tom.goto(50,100)
white()

tom.pu()
tom.goto(250,250)
white()

tom.pu()
tom.goto(50,150)
yellow()

tom.pu()
tom.goto(100,100)
yellow()

tom.pu()
tom.goto(100,200)
yellow()

tom.pu()
tom.goto(100,250)
yellow()

tom.pu()
tom.goto(150,150)
yellow()

tom.pu()
tom.goto(200,100)
yellow()

tom.pu()
tom.goto(250,100)
yellow()

tom.pu()
tom.goto(0,150)
dyellow()

tom.pu()
tom.goto(50,200)
dyellow()

tom.pu()
tom.goto(100,150)
dyellow()

tom.pu()
tom.goto(150,100)
dyellow()

tom.pu()
tom.goto(100,50)
dyellow()

tom.pu()
tom.goto(50,0)
dyellow()

tom.pu()
tom.goto(100,0)
bryellow()

tom.pu()
tom.goto(150,0)
bryellow()

tom.pu()
tom.goto(150,50)
bryellow()

tom.pu()
tom.goto(200,50)
bryellow()

tom.pu()
tom.goto(100,-50)
black()

tom.pu()
tom.goto(150,-50)
dblack()

tom.pu()
tom.goto(200,0)
dblack()

tom.pu()
tom.goto(250,50)
dblack()

tom.pu()
tom.goto(100,150)

tom.pu()
tom.goto(0,200)
blue()

tom.pu()
tom.goto(50,250)
blue()

tom.pu()
tom.goto(100,300)
dyellow()

tom.pu()
tom.goto(150,350)
dyellow()

tom.pu()
tom.goto(300,100)
dyellow()

tom.pu()
tom.goto(350,150)
dyellow()

tom.pu()
tom.goto(350,200)
dyellow()

tom.pu()
tom.goto(350,250)
bryellow()

tom.pu()
tom.goto(300,300)
bryellow()

tom.pu()
tom.goto(250,350)
bryellow()

tom.pu()
tom.goto(200,350)
bryellow()




def miku():
    tom.pd()
    tom.color('#68bdbd')
    cube()

def cyan():
    tom.pd()
    tom.color('#339090')
    cube()

def dcyan():
    tom.pd()
    tom.color('#1e6566')
    cube()

tom.pu()
tom.goto(150,300)
dcyan()

tom.pu()
tom.goto(150,200)
dcyan()

tom.pu()
tom.goto(200,150)
dcyan()

tom.pu()
tom.goto(300,150)
dcyan()

tom.pu()
tom.goto(200,300)
cyan()

tom.pu()
tom.goto(150,250)
cyan()

tom.pu()
tom.goto(200,200)
cyan()

tom.pu()
tom.goto(250,150)
cyan()

tom.pu()
tom.goto(250,300)
miku()

tom.pu()
tom.goto(200,250)
miku()

tom.pu()
tom.goto(250,200)
miku()

tom.pu()
tom.goto(300,200)
miku()

tom.pu()
tom.goto(300,250)
miku()

done()
