# Coding Exercise 4:

# 1 Create a list with one number, one word and one float value. Display the output of the list

l = [7, "Word", 3.5]
print(l)

# 2 I have a nested list [1, 1[1, 2]] how to grab the value of 2 from the list

l = [1, 1, [1, 2]]
print(l[2][1])

# 3 lst=['a','b','c'] What is the result of lst[1:]

lst = ['a', 'b', 'c']
print(lst[1:])

# 4 Create a dictionary with weekdays and keys and week index numbers as values. Do assign dictionary to variable

d = {'Monday': '1', 'Tuesday': '2', 'Wednesday': '3', 'Thursday': '4', 'Friday': '5', 'Saturday': '6', 'Sunday': '7' }
print(d)

# 5 D = {'k1': [1,2,3]} what is the output of d[k1][1]

D = {'k1': [1,2,3]}
print(D['k1'][1])

# 6 Can you create a list [1,[2,3]] into a tuple

t = ([1,[2,3]])
print(t)

# 7 With a single set function can you turn the word 'Mississippi' to distinct character word

s = 'Mississippi'
print(set(s))

# 8 Can you add element 'X' to the above created set

newSet = set(s)
newSet.add('X')
print(newSet)

# 9 Output of set ([1,1,2,3])

s = ([1,1,2,3])
print(s)