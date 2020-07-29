#writing to a file:

file_obj = open("squares_01.txt", "w")
for number in range(13):
    square = number * number
    file_obj.write(str(square))
    file_obj.write('\n') # for new line \n is required
file_obj.close()

#reading a written file
new_file_obj = open("squares.txt", "r")
print(new_file_obj.read()[:10])

#Second example
filename = "squared_numbers_01.txt"
outfile = open(filename, "w")

for number in range(1, 13):
    square = number * number
    outfile.write(str(square) + "\n")

outfile.close()

infile = open(filename, "r")
print(infile.read()[:10])
infile.close()


# using with explained
fname = "data2.txt"
with open(fname, 'w') as md:
    for num in range(10):
        md.write(str(num))
        md.write('\n')

fname = "data2.txt"
with open(fname, 'r') as md:
    for line in md:
        print(line)

s = "python rocks"
for ch in s:
   print("HELLO")
