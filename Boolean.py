#Boolean Values and Boolean Expressions
The == operator is one of six common comparison operators; the others are:

x != y               # x is not equal to y
x > y                # x is greater than y
x < y                # x is less than y
x >= y               # x is greater than or equal to y
x <= y               # x is less than or equal to y

#in
print('p' in 'apple')
print('i' in 'apple')
print('ap' in 'apple')
print('pa' in 'apple')

#opposite of in is not in.
print('x' not in 'apple')
print("a" in ["apple", "orange", "banana"])

print("a" in ["a", "b", "c", "d"])
print(9 in [3,2,9,10,9.0])
print('wow' not in ['gee wis', 'gosh golly', 'wow', 'amazing'])

#Arithmetic operators take precedence over logical operators.
#Python will always evaluate the arithmetic operators first (** is highest, then multiplication/division, then addition/subtraction). Next comes the relational operators.
#Finally, the logical operators are done last.
#This means that the expression x*5 >= 10 and y-6 <= 20 will be evaluated so as to first perform the arithmetic and then check the relationships.
#The and will be done last.
#Many programmers might place parentheses around the two relational expressions, (x*5 >= 10) and (y-6 <= 20).
#It is not necessary to do so, but causes no harm and may make it easier for people to read and understand the code.
a = 20
b = 15
print(b > a)
