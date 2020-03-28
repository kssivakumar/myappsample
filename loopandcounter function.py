The loop function is similar to range(), but handles the parameters somewhat differently: it takes in 3 parameters: the starting point, the stopping point, and the increment step. When the starting point is greater than the stopping point, it forces the steps to be negative. When, instead, the starting point is less than the stopping point, it forces the step to be positive. Also, if the step is 0, it changes to 1 or -1. The result is returned as a one-line, space-separated string of numbers. For example, loop(11,2,3) should return 11 8 5 and loop(1,5,0) should return 1 2 3 4. Fill in the missing parts to make that happen.
def loop(start, stop, step):
	return_string = ""
	if step == 0:
		___
	if ___:
		step = abs(step) * -1
	else:
		step = abs(step)
	for ___:
		return_string += str(count) + " "
	return return_string.strip()

print(loop(11,2,3)) # Should be 11 8 5
print(loop(1,5,0)) # Should be 1 2 3 4
print(loop(-1,-2,0)) # Should be -1
print(loop(10,25,-2)) # Should be 10 12 14 16 18 20 22 24
print(loop(1,1,1)) # Should be empty

The counter function counts down from start to stop when start is bigger than stop, and counts up from start to stop otherwise. Fill in the blanks to make this work correctly.
def counter(start, stop):
	x = start
	if ___:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if ___:
				return_string += ","
			___
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if ___:
				return_string += ","
			___
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"
