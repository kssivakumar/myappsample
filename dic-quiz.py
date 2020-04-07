file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)
file_counts["txt"]

toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
print("Chapter 5" == toc) # Is there a Chapter 5?


file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:
    print(extension)

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for ext, amount in file_counts.items():
#    print("There are {} files with the .{} extension".format(amount, ext))
file_counts.keys()
file_counts.values()

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for value in file_counts.values():
    print(value)

#Complete the code to iterate through the keys and values of the cool_beasts dictionary. Remember that the items method returns a tuple of key, value for each element in the dictionary.
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for item,value in cool_beasts.items():
    print("{} have {}".format(item,value))

#Let's check out a simple example of counting how many times each letter appears in a piece of text.
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result
count_letters("aaaaaa")

#In Python, a dictionary can only hold a single value for a given key. To workaround this, our single value can be a list containing multiple values. Here we have a dictionary called "wardrobe" with items of clothing and their colors. Fill in the blanks to print a line for each item of clothing with each color, for example: "red shirt", "blue shirt", and so on.
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for item, colors in wardrobe.items():
	for color in colors:
		print("{} {}".format(color, item))
