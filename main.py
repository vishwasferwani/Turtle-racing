
from turtle import Turtle, Screen
from tkinter import messagebox
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=600)

colors = ["red", "green", "purple", "black", "blue",]
turtle_position = [-60, -30, 0, 30, 60]

user_choice = screen.textinput("who will win", "red,green,blue,purple,black")
if user_choice:
    is_race_on = True

all_turtle = []

for turtle_index in range(0, 5):
    toto = Turtle(shape="turtle")
    toto.penup()
    toto.color(colors[turtle_index])
    toto.goto(x=-220, y=turtle_position[turtle_index])
    all_turtle.append(toto)

while is_race_on:
    for turtle in all_turtle:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 230:
            win = turtle.pencolor()
            if win == user_choice:
                messagebox.showinfo(message="you win")
                print(f"you won! The winning Turtle is {win}")
            else:
                print(f"You lose! The winning Turtle is {win}")
                messagebox.showinfo(message=f"you lose {win} win")
            is_race_on = False


screen.exitonclick()

