#Disabmiguating []: creation vs indexing
#Square brackets [] are used in quite a few ways in python. When you’re first learning how to use them it may be confusing, but with practice and repetition they’ll be easy to incorporate!
#You have currently encountered two instances where we have used square brakets. The first is creating lists and the second is indexing. At first glance, creating and indexing are difficult to distinguish. However, indexing requires referencing an already created list while simply creating a list does not.
lst = [0]
n_lst = lst[0]

print(lst)
print(n_lst)

#Here, we see a list called lst being assigned to a list with one element, zero.
#Then, we see how n_lst is assigned the value associated with the first element of lst.
#Dispite the variable names, only one of the above variables is assigned to a list.
#Note that in this example, what sets creating appart from indexing is the reference to the list to let python know that you are extracting an element from another list.
fruit = "grape"
midchar = fruit[len(fruit)//2]

s = "python rocks"
print(len(s))

alist = [3, 67, "cat", 3.14, False]
print(len(alist))

#Assign the number of elements in lst to the variable output.
lst = ["hi", "morning", "dog", "506", "caterpillar", "balloons", 106, "yo-yo", "python", "moon", "water", "sleepy", "daffy", 45, "donald", "whiteboard", "glasses", "markers", "couches", "butterfly", "100", "magazine", "door", "picture", "window", ["Olympics", "handle"], "chair", "pages", "readings", "burger", "juggle", "craft", ["store", "poster", "board"], "laptop", "computer", "plates", "hotdog", "salad", "backpack", "zipper", "ring", "watch", "finger", "bags", "boxes", "pods", "peas", "apples", "horse", "guinea pig", "bowl", "EECS"]
output = len(lst)
print(output)


#Create a new list using the 9th through 12th elements (four items in all) of new_lst and assign it to the variable sub_lst.
new_lst = ["computer", "luxurious", "basket", "crime", 0, 2.49, "institution", "slice", "sun", ["water", "air", "fire", "earth"], "games", 2.7, "code", "java", ["birthday", "celebration", 1817, "party", "cake", 5], "rain", "thunderstorm", "top down"]
sub_lst = new_lst[8:12]
print(sub_lst)
