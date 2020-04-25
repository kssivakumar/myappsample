#For loops
for name in ["Siva", "Kumar", "Arunan", "Neha"]:
    print("Hi" , name, "please come to my home.")


import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

for acolor in ["Yellow", "red", "Purple", "Blue"]:
    alex.color(acolor)
    alex.pensize(10)
    alex.forward(50)
    alex.left(90)
wn.exitonclick()


#Strings and for loops
#Since a string is simply a sequence of characters, the for loop iterates over each character automatically.
for achar in "Go Spot Go":
    print(achar)

# Lists and for loops
#It is also possible to perform list traversal using iteration by item. A list is a sequence of items, so the for loop iterates over each item in the list automatically.
fruits = ["apple", "Orange", "Banana", "Cherry"]
for afruit in fruits:
    print(afruit)

#Using the range Function to Generate a Sequence to Iterate Over
#We are now in a position to understand the inner workings we glossed over previously when we first introduced repeated execution with a for loop. Here was the example:
print("This will excuite first")

for _ in range(3):
    print("This line will execute three times")
    print("This line will also execute three times")
print("Now we are outside of the for loop!")

#The range function takes an integer n as input and returns a sequence of numbers, starting at 0 and going up to but not including n. Thus, instead of range(3), we could have written [0, 1, 2].
#The loop variable _ is bound to 0 the first time lines 4 and 5 execute. The next time, _ is bound to 1. Third time, it is bound to 2. _ is a strange name for a variable but if you look carefully at the rules about variable names, it is a legal name.
#By convention, we use the _ as our loop variable when we don’t intend to ever refer to the loop variable.
#That is, we are just trying to repeat the code block some number of times (once for each item in a sequence), but we are not going to do anything with the particular items. _ will be bound to a different item each time, but we won’t ever refer to those particular items in the code.
#By contrast, notice that in the previous activecode window, the loop variable is afruit. In that for loop, we do refer to each item, with print(afruit).

#Iteration Simplifies our Turtle Program
import turtle            # set up alex
wn = turtle.Screen()
alex = turtle.Turtle()

for i in range(4):      # repeat four times
    alex.forward(50)
    alex.left(90)

wn.exitonclick()

import turtle            # set up alex
wn = turtle.Screen()
alex = turtle.Turtle()
for aColor in ["yellow", "red", "green", "blue"]:
   alex.forward(50)
   alex.left(90)
