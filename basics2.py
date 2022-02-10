import string

# Coding Exercise 3:

# 1. Write a string that returns just the letter 'r' from 'Hello World'

print("Hello World"[8])

# 2. String slicing to grab the word ink from the word thinker

s = "thinker"
print(s[2:5])

# 3. S='Sammy' what is the output of s[2:]

s = "Sammy"
print(s[2:])

# 4. With a single set function can you turn the word 'Mississippi' to distinct character word.

# I don't understand the question. Please write the question better.

# 5. The word or whole phrase which has the same sequence of letters in both directions is called a palindrome.

def lowerAndRemovePunc(s):
    return "".join(i.lower() for i in s if i in string.ascii_letters)

def isPalindrome(s):
    s = lowerAndRemovePunc(s)
    return s == s[::-1]

a = "Stars"
b = "O, a kak Uwakov lil vo kawu kakao!"
c = "Some men interpret nine memos"

answer = isPalindrome(a)
if answer:
    print("Y")
else:
    print("N")

answer = isPalindrome(b)
if answer:
    print("Y")
else:
    print("N")

answer = isPalindrome(c)
if answer:
    print("Y")
else:
    print("N")