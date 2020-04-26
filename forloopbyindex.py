#Traversal and the for Loop: By Index
#For example, consider the list ['apple', 'pear', 'apricot', 'cherry', 'peach']. ‘apple’ is at position 0, ‘pear’ at position 1, and ‘peach’ at position 4.
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(5):
    print(n, fruits[n])

fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(len(fruits)):
    print(n, fruits[n])

#moreiter-6-1: How many times is the letter p printed by the following statements?
s = "python"
for idx in range(len(s)):
   print(s[idx % 2])

#Nested Iteration: Image Processing
import image

p = image.Pixel(45, 76, 200)
print(p.getRed())
p.setRed(66)
print(p.getRed())
p.setBlue(p.getGreen())
print(p.getGreen(), p.getBlue())

#Image Processing and Nested Iteration
#Image processing refers to the ability to manipulate the individual pixels in a digital image.
#In order to process all of the pixels, we need to be able to systematically visit all of the rows and columns in the image. The best way to do this is to use nested iteration.
for i in range(5):
    for j in range(3):
        print(i, j)

#The for i iteration is the outer iteration and the for j iteration is the inner iteration.
#Each pass through the outer iteration will result in the complete processing of the inner iteration from beginning to end.
#This means that the output from this nested iteration will show that for each value of i, all values of j will occur.
#Here is the same example in activecode. Try it. Note that the value of i stays the same while the value of j changes. The inner iteration, in effect, is moving faster than the outer iteration.
