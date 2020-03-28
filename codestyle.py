def calculate(d):
    q = 3.14
    z = q * (d ** 2)
    print(z)

calculate(5)


Refactoring the above code
def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)

circle_area(10)


def f1(x, y):
	z = x*y  # the area is base*height
	print("The area is " + str(z))

def rectangle_area(base, height):
	z = base * height  # the area is base*height
	print("The area is " + str(z))

rectangle_area(5,6)

def convert_distance(miles):
    km = miles * 1.6
    print(str(km))


convert_distance(55)


def convert_distance(miles):
	km = (miles * 1.6) * 2
    print("The round-trip in kilometers is " + str(km))
convert_distance(55)


def convert_distance(miles):
	km = (miles * 1.6) * 2
	print("The round-trip in kilometers is " + str(km))
convert_distance(55)


def convert_distance(my_trip_miles):
	km = my_trip_miles * 1.6  # approximately 1.6 km in 1 mile
	print("my_trip_km = " + str(km))
my_trip_miles = 55


# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km
result = convert_distance(55)
my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = (str(result))

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(result))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(result*2))

def hint_username(username):
    if len(username) > 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        print("Valid username")



def is_positive(number):
    if number > 0:
        return True
    else:
        return False


Function to check value is even or odd
def if_even(number):
    if number % 2 == 0:
        return True
    return False

elif statements

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 character long")
    else:
        if len(username) > 15:
            print("Invalid username. Must be at most 15 character long")
        else:
            print("Valid username")

To avoid code to be too complicated we use elif

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 character long")
    elif len(username) < 15:
        print("Invalid username. Must be at least 15 character long")
    else:
        print("Valid username")

def number_group(number):
  if number > 0:
    return "Positive"
  elif number == 0:
    return "Zero"
  else:
    return "Negative"

print(number_group(10))
print(number_group(0))
print(number_group(-5))

number = 10
if number > 11:
  print(0)
elif number != 10:
  print(1)
elif number >= 20 or number < 12:
  print(2)
else:
  print(3)


def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return ""

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown


"big" > "small"
