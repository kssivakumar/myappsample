def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n-1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result
factorial(4)


def multiplication_table(start, stop):
   for x in range(start,stop+1):
       for y in range(start,stop+1):
           print(str(x*y), end=" ")
       print()
 multiplication_table(1, 3)


def votes(params):
	for vote in params:
	    print("Possible option:" + vote)


for x in range(10):
    for y in range(x):
        print(y)

for x in range(1, 10, 3):
    print(x)


def decade_counter():
	while year < 50:
		year += 10
	return year
decade_counter(10)
