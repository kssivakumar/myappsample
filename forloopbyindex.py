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


import image
from PIL import Image
#import image
img = image.Image("luther.jpg")

print(img.getWidth())
print(img.getHeight())

p = img.getPixel(45, 55)
print(p.getRed(), p.getGreen(), p.getBlue())
