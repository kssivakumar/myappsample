#The Accumulator Pattern
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
accum = 0
for w in nums:
    accum = accum + w
    print(accum)
#In the program above, notice that the variable accum starts out with a value of 0. Next, the iteration is performed 10 times.
#Inside the for loop, the update occurs. w has the value of current item (1 the first time, then 2, then 3, etc.). accum is reassigned a new value which is the old value plus the current value of w.
#The anatomy of the accumulation pattern includes:
#   initializing an “accumulator” variable to an initial value (such as 0 if accumulating a sum)

#    iterating (e.g., traversing the items in a sequence)

#   updating the accumulator variable on each iteration (i.e., when processing each item in the sequence)

# Range Function

#We can utilize the range function in this situation as well. Previously, you’ve seen it used when we wanted to draw in turtle.
#There we used it to iterate a certain number of times. We can do more than that though. The range function takes at least one input - which should be an integer - and returns a list as long as your input.
#While you can provide two inputs, we will focus on using range with just one input. With one input, range will start at zero and go up to - but not include - the input. Here are the examples:
print("range(5): ")
for i in range(5):
    print(i)

print("range(0,5): ")
for i in range(0, 5):
    print(i)

# Notice the casting of `range` to the `list`
print(list(range(5)))
print(list(range(0,5)))

# Note: `range` function is already casted as `list` in the textbook
print(range(5))

accum = 0
for w in range(11):   #Because the range function is exclusive of the ending number, we have to use 11 as the function input.
    accum = accum + w
print(accum)

# or, if you use two inputs for the range function

sec_accum = 0
for w in range(1,11): #Because the range function is exclusive of the ending number, we have to use 11 as the function input.
    sec_accum = sec_accum + w
print(sec_accum)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for w in nums:
    count = count + 1
print(count)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for w in nums:
   accum = 0
   accum = accum + w
print(accum)

#example:
n = int(input("How many odd numbers would you like to add together?"))
thesum = 0
oddnumber = 1

for counter in range(n):
    thesum = thesum + oddnumber
    oddnumber = oddnumber + 2
print(thesum)

#troubleshooting
w = range(10)
tot = 0
print('******Before the for loop**************')
for num in w:
    print('**********A new loop iteration*******')
    print("Value for num:", num)
    tot += num
    print("Value of tot:", tot)
print("**********End of FOR loop*******")
print('******Final Total:', tot)


item = ["M", "I", "S", "S", "O", "U", "R", "I"]
for val in item:
    val = val + "!"

#Count the number of characters in string str1. Do not use len(). Save the number in variable numbs.
str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."
numbs = 0
for s in str1:
   numbs = numbs + 1
print(numbs)

#Create a list of numbers 0 through 40 and assign this list to the variable numbers.
#Then, accumulate the total of the list’s values and assign that sum to the variable sum1.
numbers = range(0,41)
sum1 = 0
for w in range(0,41):
    sum1 = sum1 + w
print(sum1)
