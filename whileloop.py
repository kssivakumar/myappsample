x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
    print("x=" + str(x))


while loop in a function


def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("done")
attempts(5)
