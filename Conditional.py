#condition execution
x = 14
if x % 2 == 0:
    print(x, "is even")
    print("It is even")
else:
    print(x, "is odd")
    print("It is odd")

#write code to assign the string "You can apply to SI" to output if the string "SI 106" is in the courses. If it is not in courses, assign the value "Take SU 106!" to the variable output.

courses = ["ENGR 101" , "SI 110", "ENG 125", "SI 106", "CHEM 130"]

if "SI 106" in courses:
    output = "You can apply to SI!"
else:
    output = "Take SI 106!"

The syntax for an if statement looks like this:

if BOOLEAN EXPRESSION:
    STATEMENTS_1        # executed if condition evaluates to True
else:
    STATEMENTS_2        # executed if condition evaluates to False
#The boolean expression after the if statement is called the condition.
#If it is true, then the indented statements get executed.
#If not, then the statements indented under the else clause get executed.
