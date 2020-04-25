#concatenate and repetition
fruit = ["apple", "Orange", "Banana", "Cherry"]
print([1,2] + [3,4])
print(fruit+[6,7,8,9])
print([0,1] * 4)

#count and indexing
#Count
a = "I have had an apple on my desk before!"
print(a.count("e"))
print(a.count("ha"))

z = ['atoms', "4", 'neutron', 6, 'proton', 4, 'electron', 4, 'electron', 'atoms']
print(z.count("4"))
print(z.count(4))
print(z.count("a"))
print(z.count("electron"))

#indexing
music = "Pull out your music and dancing can begin"
bio = ["Metatarsal", "Metatarsal", "Fibula", [], "Tibia", "Tibia", 43, "Femur", "Occipital", "Metatarsal"]
print(music.index("m"))
print(music.index("your"))

print(bio.index("Metatarsal"))
print(bio.index([]))
print(bio.index(43))

#splitting and joining
song = "The rain in Spain..."
wds = song.split()
print(wds)

#An optional argument called a delimiter can be used to specify which characters to use as word boundaries.
song = "The rain in Spain..."
wds = song.split('ai')
print(wds)

#The inverse of the split method is join. You choose a desired separator string, (often called the glue) and join the list with the glue between each of the elements.
wds = ["red", "blue", "green"]
glue = ';'
s = glue.join(wds)
print(s)
print(wds)

print("***".join(wds))
print("".join(wds))

#Create a new list of the 6th through 13th elements of lst (eight items in all) and assign it to the variable output.
lst = ["swimming", 2, "water bottle", 44, "lollipop", "shine", "marsh", "winter", "donkey", "rain", ["Rio", "Beijing", "London"], [1,2,3], "gold", "bronze", "silver", "mathematician", "scientist", "actor", "actress", "win", "cell phone", "leg", "running", "horse", "socket", "plug", ["Phelps", "le Clos", "Lochte"], "drink", 22, "happyfeet", "penguins"]
output = lst[6:13]
print(output)

#Create a variable output and assign it to a list whose elements are the words in the string str1.
str1 = "OH THE PLACES YOU'LL GO"
output = str1.split()
print(output)

let = "z"
let_two = "p"
c = let_two + let
m = c*5
print(m)


sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
last = sports[-3:]
print(last)


ls = ['run', 'world', 'travel', 'lights', 'moon', 'baseball', 'sea']
new = ls[2:4]
print(new)


l = ['w', '7', 0, 9]
m = l[1:2]

b = "My, what a lovely day"
x = b.split(',')
print(x)


b = "My, what a lovely day"
x = b.split(',')
z = "".join(x)
y = z.split()
a = "".join(y)
