#method1

import random

prob = random.random()
print(prob)

diceThrow = random.randrange(1,7)
print(diceThrow)


#method2
from random import random, randrange
prob = random()
print(prob)

diceThrow = randrange(1,7)
print(diceThrow)

import turtle

jane = turtle.Turtle()
jane.forward(20)
print(jane.x)


lst = ["hi", "morning", "dog", "506", "caterpillar", "balloons", 106, "yo-yo", "python", "moon", "water", "sleepy", "daffy", 45, "donald", "whiteboard", "glasses", "markers", "couches", "butterfly", "100", "magazine", "door", "picture", "window", ["Olympics", "handle"], "chair", "pages", "readings", "burger", "juggle", "craft", ["store", "poster", "board"], "laptop", "computer", "plates", "hotdog", "salad", "backpack", "zipper", "ring", "watch", "finger", "bags", "boxes", "pods", "peas", "apples", "horse", "guinea pig", "bowl", "EECS"]

output = print(lst[30])
