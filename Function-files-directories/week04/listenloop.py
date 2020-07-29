#Inside the while loop there is a function call to get user input. The loop repeats indefinitely, until a particular input is received.
theSum = 0
x = -1
while (x != 0):
    x = int(input("next number to add up (enter 0 if no more numbers): "))
    theSum = theSum + x

print(theSum)
