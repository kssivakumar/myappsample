def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(1,x):
        sum += square(n)
    return sum

print(sum_squares(10))

friends = ['Taylor', 'Alex', 'Pat', 'eli']
for friend in friends:
	print("Hello my dear " + friend)


values = [ 23, 52, 59, 37, 48 ]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1
    print("Total sum: " + str(sum) + " - Average: " + str(sum/length))


def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

def to_celsius(x):
    return (x-32)*5/9
for x in range(0,101,10):
        print(x, to_celsius(x))


Dominos probability
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end="")
        print()

teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)



def count_chars(txt):
	result = 0
	for char in txt:
		result += 1     # same as result = result + 1
	return result
print count_chars(text)
