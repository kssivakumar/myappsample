#Function accumulator
def total(lst):
    tot = 0
    for num in lst:
        tot = tot + num
    return tot
y = total([1, 5, 8])
print(y)

#A function that accumulates
def mylen(seq):
    c = 0
    for _ in seq:
        c = c + 1
    return c
print(mylen("hello"))
print(mylen([1, 2, 7]))

#func-5-1: Rearrange the code statements to match the activecode window above.



#Write a function named total that takes a list of integers as input, and returns the total value of all those integers added together.

def total(x):
    z = 0
    for y in x:
      z += y
    return z
print(total((1,2,3,4,5)))

#Write a function called count that takes a list of numbers as input and returns a count of the number of elements in the list
def count(x):
    count = 0
    for ele in x:
          count = count + 1
    return count


#To do
#8. Write a function named same that takes a string as input, and simply returns that string.
#9. Write a function called same_thing that returns the parameter, unchanged.
#10. Write a function called subtract_three that takes an integer or any number as input, and returns that number minus three.
#11. Write a function called change that takes one number as its input and returns that number, plus 7.
#12. Write a function named intro that takes a string as input. Given the string “Becky” as input, the function should return: “Hello, my name is Becky and I love SI 106.”
#13. Write a function called s_change that takes one string as input and returns that string, concatenated with the string ” for fun.”.
#
14. Write a function called decision that takes a string as input, and then checks the number of characters.
#If it has over 17 characters, return “This is a long string”, if it is shorter or has 17 characters, return “This is a short string”.
