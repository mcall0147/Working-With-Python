import math

# Coding Exercise 2:
# 1. Numbers: Example code to add two numbers 50+50 and 100-10 and print it.

print(50 + 50)
print(100 - 10)

# 2. 30+*6, 6^6, 6**6, 6+6+6+6+6+6

# 30+*6 throws a syntax error
# print(30+*6)

# 6^6 outputs 0.
print(6^6)

# 6**6 outputs 46656
print(6**6)

# 6+6+6+6+6+6 outputs 36
print(6+6+6+6+6+6)

# 3. Print "Hello World" on the console output. Print output "Hello World : 10"
# Make sure capitalization and spacing matches.

print("Hello World")
print("Hello World : 10")

# 4. Mathematically, mortgage works by the following algorithm:

# Interest rate
r = 0.06
# Length of time in months
l = 103

def calculateAmount(length):
    # Loan amount
    p = 800000
    # Monthly payment amount
    m = 10000 

    # For loop to reduce the total amount owed after each month.
    for i in range(l - 1):
        interest = math.ceil(p) * (r/12)
        p += math.ceil(interest)
        p -= m

    # Setting monthly payment to the remaining amount below 10,000
    m = p
    # Subtracting final monthly payment from remaining loan amount.
    p -= m
    
    # Printing the final amount of 0 after the loan has been paid off over the 103 months
    print(p)

# Calling the function with the parameter l for the number of months
calculateAmount(l)