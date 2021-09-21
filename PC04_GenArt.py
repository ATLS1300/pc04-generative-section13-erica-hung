#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 15:54:27 2021

@author: erica (no partner)

This code will generate a gradient art piece of similar hues and 
colors through the use of overlapping lines of various colors. 


"""

import turtle
import random

greenList = ["DarkOliveGreen1", "LightGreen", "PaleGreen", "GreenYellow"]
blueList = ["PowderBlue", "LightSkyBlue", "Cyan4", "LightSeaGreen"]
purpleList = ["plum", "MediumPurple1", "orchid", "magenta4"]

positionListA = [(-360,90), (-360,115), (-360,130), (-360,145), (-360,160), (-360,175), (-360,190), (-360,215), (-360,235), (-360,250)]
positionListB = [(-360,80), (-360,65), (-360,50), (-360,35), (-360,20), (-360,5), (-360,-15), (-360,-30), (-360,-45), (-360,-60), (-360,-75)]
positionListC = [(-360,-90), (-360,-115), (-360,-130), (-360,-145), (-360,-160), (-360,-175), (-360,-190), (-360,-215), (-360,-230), (-360,-245), (-360,-260)]

angleList = [0, 2, 3, 4, -2, -3, -4]

jude = turtle.Turtle() #draws green lines from positions listed in positionList1
crew = turtle.Turtle() #draws blue lines from positions listed in positionList2
gato = turtle.Turtle() #draws purple lines from positions listed in positionList3

#green lines are drawn from random angles and positions listed in angleList and positionListA
for i in range(65):
    jude.color(random.choice(greenList))
    jude.up()
    jude.goto(random.choice(positionListA)) #random positions for jude to use 
    jude.right(random.choice(angleList)) #random angles for jude to use 
    jude.down()
    jude.fd(820)

#blue lines are drawn from random angles and positions listed in angleList and positionListB
for i in range(65): 
    crew.color(random.choice(blueList))
    crew.up()
    crew.goto(random.choice(positionListB)) #random positions for crew to use 
    crew.left(random.choice(angleList)) #random angles for crew to use 
    crew.down()
    crew.fd(820)

#purple lines are drawn from random angles and positions listed in angleList and positionListC
for i in range(65):
    gato.color(random.choice(purpleList))
    gato.up()
    gato.goto(random.choice(positionListC)) #random positions for gato to use 
    gato.right(random.choice(angleList)) #random angles for gato to use 
    gato.down()
    gato.fd(820)
