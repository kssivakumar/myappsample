#A professor with two assistants, Jamie and Drew, wants an attendance list of the students, in the order that they arrived in the classroom. Drew was the first one to note which students arrived, and then Jamie took over. After the class, they each entered their lists into the computer and emailed them to the professor, who needs to combine them into one, in the order of each student's arrival. Jamie emailed a follow-up, saying that her list is in reverse order. Complete the steps to combine them into one list as follows: the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.
def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  return list2+list1[::-1]

Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))


#The format_address function separates out parts of the address string into new strings: house_number and street_name, and returns: "house number X on street named Y". The format of the input string is: numeric house number, followed by the street name which may contain numbers, but never by themselves, and could be several words long. For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.
def format_address(address_string):
  # Declare variables

  # Separate the address string into parts

  # Traverse through the address parts
  for __:
    # Determine if the address part is the
    # house number or part of the street name

  # Does anything else need to be done
  # before returning the result?

  # Return the formatted string
  return "house number {} on street named {}".format(__)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"


def format_address(address_string):
  # Declare variables
  word1=""
  word2=""
  # Separate the address string into parts
  words=address_string.split()
  # Traverse through the address parts
  for word in words:
    # Determine if the address part is the
    # house number or part of the street name
    if(word.isnumeric()):
      word1 += word
    else:
      word2 += word+""
  # Does anything else need to be done
  # before returning the result?

  # Return the formatted string
  return "house number {} on street named {}".format(word1,word2)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
