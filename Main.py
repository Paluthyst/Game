import turtle
import random

player_1 = turtle.Turtle()
player_1.color("green")
player_1.shape("turtle")
player_1.penup()
player_1.goto(-200, 100)
player_2 = player_1.clone()
player_2.color("orange")
player_2.goto(-200, 50)

