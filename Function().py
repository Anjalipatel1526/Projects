#Greet a User
def greet(name):
    print("Hello,", name + "!")
username = input("Enter your name: ")
greet(username)


#Add Two Numbers
def add(a, b):
    return a + b
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = add(num1, num2)
print("The sum is:", result)

#Find the Square
def square(num):
    return num * num
n = int(input("Enter a number: "))
print("Square of", n, "is:", square(n))

#check weather odd or even
def check_even_odd(n):
    if n % 2 == 0:
        print(n, "is Even")
    else:
        print(n, "is Odd")
num = int(input("Enter a number: "))
check_even_odd(num)

#function of min and max
def maximum(a, b):
    if a > b:
        return a
    else:
        return b
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The larger number is:", maximum(num1, num2))

#Print Numbers from 1 to n
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)
num = int(input("Enter a number: "))
print_numbers(num)

#factorial using loop
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
num = int(input("Enter a number: "))
print("Factorial of", num, "is:", factorial(num))

#count vowel in word
def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count
text = input("Enter a word: ")
print("Number of vowels:", count_vowels(text))

#Reverse string
def reverse_string(s):
    return s[::-1]
text = input("Enter a string: ")
print("Reversed string:", reverse_string(text))

#Mutliplication table
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
num = int(input("Enter a number: "))
multiplication_table(num)
