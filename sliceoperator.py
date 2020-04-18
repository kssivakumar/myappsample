#A substring of a string is called a slice. Selecting a slice is similar to selecting a character:
singers = "Peter, Paul, and Mary"
print(singers[0:5])
print(singers[7:11])
print(singers[17:21])


a_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(a_list[1:3])
print(a_list[:4])
print(a_list[3:])
print(a_list[:])

#Tuple Slices
#We can’t modify the elements of a tuple, but we can make a variable reference a new tuple holding different information. #
#Thankfully we can also use the slice operation on tuples as well as strings and lists.
#To construct the new tuple, we can slice parts of the old tuple and join up the bits to make the new tuple.
#So julia has a new recent film, and we might want to change her tuple. We can easily slice off the parts we want and concatenate them with the new tuple
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia[2])
print(julia[2:6])

print(len(julia))

julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
print(julia)


s = "python rocks"
print(s[3:8])

alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]
print(alist[4:])

#What is printed by the following statements?
L = [0.34, '6', 'SI106', 'Python', -2]
print(len(L[1:-1]))
