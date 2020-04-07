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

username = get_username()
while not valid_username(username):
    print("Invalid username")
    username = get_username()

my_variable = 5
while my_variable <  10:
    print("Hello")
    my_variable +=1


In this code, there's an initialization problem that's causing our function to behave incorrectly. Can you find the problem and fix it?
def count_down(start_number):
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)

Answer:

def count_down(current):
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)


x = 4
if x != 0:
    while x % 2 == 0:
        x = x / 2
        print(x)True

def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor+=1
  return "Done"

print_prime_factors(100)


def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while n % 2 == 0:
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False

print(is_power_of_two(0))
