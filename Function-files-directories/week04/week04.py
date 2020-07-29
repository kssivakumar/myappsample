#Write code to count the number of characters in original_str using the accumulation pattern and assign the answer to a variable num_chars.
#Do NOT use the len function to solve the problem (if you use it while you are working on this problem, comment it out afterward!)
original_str = "The quick brown rhino jumped over the extremely lazy fox."
num_chars = 0
for i in original_str:
    num_chars = num_chars + 1
    print(num_chars)


list1 = [8, 3, 4, 5, 6, 7, 9]
tot = 0
for elem in list1:
    tot = tot + elem

idx = 0
accum = 0
while idx < len(list1):
    accum = accum + list1[idx]
    idx = idx + 1


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for w in nums:
   accum = 0
   accum = accum + w
print(accum)

#Write a while loop that is initialized at 0 and stops at 15. If the counter is an even number, append the counter to a list called eve_nums.
count = 0
eve_nums = []
while count <= 15:
    if count % 2 == 0:
        eve_nums.append(count)
    count = count + 1

#Below, we’ve provided a for loop that sums all the elements of list1.
#Write code that accomplishes the same task, but instead uses a while loop. Assign the accumulator variable to the name accum.
list1 = [8, 3, 4, 5, 6, 7, 9]
tot = 0
for elem in list1:
    tot = tot + elem

idx = 0
accum = 0
while idx < len(list1):
    accum = accum + list1[idx]
    idx = idx + 1

def stop_at_four():
   list_=[3,6,4,1,3]
   accum_lst=[]
   accum_var=0

   while list_[accum_var] != 4 :
       accum_lst.append(list_[accum_var])
       accum_var += 1
   return accum_lst

print(stop_at_four())
