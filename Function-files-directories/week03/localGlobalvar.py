#localvariable
#An assignment statement in a function creates a local variable for the variable on the left hand side of the assignment operator.
#It is called local because this variable only exists inside the function and you cannot use it outside. For example, consider again the square function:
def square(x):
    y = x * x
    return y

z = square(10)
print(z)


by = "You are"
az = "doing a great "
io = "job"
qy = "keep it up!"

message = (by + ' ' + az + io + ', ' + qy)
print(message)


def square(x):
    return x*x

def g(y):
    return y + 3

def h(y):
    return square(y) + 3

print(g(h(2))
