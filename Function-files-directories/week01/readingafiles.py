fileref = open('filename.txt', "r")
#contents = fileref.read()
#print(len(contents))
for lin in fileref: # common way of reading files in python
    print(lin.strip())
fileref.close()


#Using the file school_prompt2.txt, find the number of characters in the file and assign that value to the variable num_char.
fileref = open("L:\Mygit\Function-files-directories\school_prompt2.txt", "r")
data = fileref.read()
num_char = len(data)
print(num_char)


file = ("L:\Mygit\Function-files-directories\travel_plan2.txt", "r")
fname = input("Enter file name: ")
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines:")
print(num_lines)

#Find the number of lines in the file, travel_plans2.txt, and assign it to the variable num_lines
file = open("travel_plans2.txt", "r")
num_lines = len(file.readlines())
print(num_lines)

#Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt.
fileref = open("emotion_words2.txt" , "r")
first_forty = fileref.read(40)
print(first_forty)


#Write code to find out how many lines are in the file emotion_words.txt as shown above. Save this value to the variable num_lines. Do not use the len method.
fileref = "emotion_words.txt"
num_lines = 0
with open(fileref, 'r') as f:
    for line in f:
        num_lines += 1
print(num_lines)

#writing to a file:

file_obj = open("squares.txt", "w")
for number in range(13):
    square = number * number
    file_obj.write(str(square))
    file_obj.write('\n') # for new line \n is required
file_obj.close()

#reading a written file
new_file_obj = open("squares.txt", "r")
print(new_file_obj.read()[:10])

filename = "squared_numbers.txt"
outfile = open(filename, "w")

for number in range(1, 13):
    square = number * number
    outfile.write(str(square) + "\n")

outfile.close()

infile = open(filename, "r")
print(infile.read()[:10])
infile.close()
