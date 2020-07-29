# The Pythonic Way to Enumerate Items in a Sequence
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(len(fruits)):
    print(n, fruits[n])

#We are now prepared to understand a more pythonic approach to enumerating items in a sequence. Python provides a built-in function enumerate
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for item in enumerate(fruits):
    print(item[0], item[1])

#The pythonic way to consume the results of enumerate, however,
#is to unpack the tuples while iterating through them, so that the code is easier to understand.
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for idx, fruit in enumerate(fruits):
    print(idx, fruit)


#If you remember, the .items() dictionary method produces a sequence of tuples. Keeping this in mind, we have provided you a dictionary called pokemon.
#For every key value pair, append the key to the list p_names, and append the value to the list p_number. Do not use the .keys() or .values() methods.
pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
p_names = list()
p_number = list()

for pok in pokemon.items():
    p_names.append(pok[0])
    p_number.append(pok[1])
print(p_names)
print(p_number)



#The .items() method produces a sequence of key-value pair tuples.
#With this in mind, write code to create a list of keys from the dictionary track_medal_counts and assign the list to the variable name track_events. Do NOT use the .keys() method.
track_medal_counts = {'shot put': 1, 'long jump': 3, '100 meters': 2, '400 meters': 2, '100 meter hurdles': 3, 'triple jump': 3, 'steeplechase': 2, '1500 meters': 1, '5K': 0, '10K': 0, 'marathon': 0, '200 meters': 0, '400 meter hurdles': 0, 'high jump': 1}
track_events = list()
for track_medal in track_medal_counts.items():
    track_events.append(track_medal[0])
print(track_events)
