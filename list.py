fruits = [ "Pineapple", "Banana", "Apple", "Melon" ]
fruits.append("Kiwi")
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")
fruits.pop(3)
fruits[2]= "Strawberry"
print(fruits)

#The skip_elements function returns every other element from the list, starting from the first. Complete this function to do that.
def skip_elements(elements):
    new_list = []
    for i in range(0, len(elements), 2):
        new_list.append(elements[i])
    return new_list
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []


animals = ["lion", "Dolphin", "Monkey", "Zebra"]
chars = 0
for animal in animals:
    chars += len(animal)
print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))

winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result
print(full_emails([("alex@example.com", "Alex Diego"), ("sivakumks@gmail.com", "Sivakumar Saravanamuthu")]))

multiples = []
for x in range(1,11):
    multiples.append(x*7)
    print(multiples)

#list Comprehensions
multiples = [ x*7 for x in range(1,11)]
print(multiples)

languages = ["python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)


def skip_elements(elements):
  new_list = []
  for i in range(-0, len(elements), 2):
    new_list.append(elements[i])
  return new_list



print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

def skip_elements(elements):
  new_list = []
  for i in range(-0, len(elements), 2):
    new_list.append(elements[i])
  return new_list


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']


#list Comprehensions
def skip_elements(elements):
    new_list = [(for i in range(-0, len(elements), 2):, new_list.append(elements[i]), return new_list)]
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
