#We can apply functions to the turtle drawings we’ve done in the past as well.
import turtle
def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""

    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()      # Set up the window and its attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()    # create alex
drawSquare(alex, 50)      # Call the function to draw the square passing the actual turtle and the actual side size

wn.exitonclick()

#How do we write our own fruitful function? Let’s start by creating a very simple mathematical function that we will call square.
#The square function will take one number as a parameter and return the result of squaring that number.
#Here is the black-box diagram with the Python code following.
def square(x):
    y = x * x
    return y
toSquare = 10
result = square(toSquare)
print("The result of {} squared is {}.".format(toSquare, result))



#func-4-5: What will the following code output?
def cyu2(s1, s2):
    x = len(s1)
    y = len(s2)
    return x-y

z = cyu2("Yes", "no")
if z > 0:
    print("First one was longer")
else:
    print("Second one was at least as long")

#func-4-6: Which will print out first, square, g, or a number?
def square(x):
    print("square")
    return x*x

def g(y):
    print("g")
    return y + 3

print(square(g(2)))

#func-4-7: How many lines will the following code print?
def show_me_numbers(list_of_ints):
    print(10)
    print("Next we'll accumulate the sum")
    accum = 0
    for num in list_of_ints:
        accum = accum + num
    return accum
    print("All done with accumulation!")

show_me_numbers([4,2,3])


def longer_than_five(list_of_names):
    for name in list_of_names: # iterate over the list to look at each name
        if len(name) > 5: # as soon as you see a name longer than 5 letters,
            return True # then return True!
        else:     # If Python executes that return statement, the function is over and the rest of the code will not run -- you already have your answer!
            return False # You will only get to this line if you
    # iterated over the whole list and did not get a name where
    # the if expression evaluated to True, so at this point, it's correct to return False!

# Here are a couple sample calls to the function with different lists of names. Try running this code in Codelens a few times and make sure you understand exactly what is happening.

list1 = ["Sam","Tera","Sal","Amita"]
list2 = ["Rey","Ayo","Lauren","Natalie"]

print(longer_than_five(list1))
print(longer_than_five(list2))


def weird():
    print("here")


#Create one conditional to find whether “false” is in string str1. If so, assign variable output the string “False. You aren’t you?”. Check to see if “true” is in string str1 and if it is then assign “True! You are you!” to the variable output.
#If neither are in str1, assign “Neither true nor false!” to output.
str1 = "Today you are you! That is truer than true! There is no one alive who is you-er than you!"
if 'false' in str1:
    output = "False. You aren't you?"
elif 'true' in str1:
    output = "True! You are you!"
else:
    output = "Neither true nor false"
