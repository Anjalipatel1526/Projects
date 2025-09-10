#input()
num1=input("Enter a number: ")
num2=input("Enter a number: ")
final_result=int(num1) + int(num2)
print("The sum is number:",final_result)

radius=float(input("Enter a number: "))
area = 3.14 * radius * radius
print("The area of the circle is: ",area)

num = 10
msg = "The value is: "
result = msg + str(num)
print(result)


age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age >= 20 and age <= 59:
    print("Adult")
else:
    print("Senior Citizen")


num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


num = float(input("Enter a number: "))
if num > 90 and above:
    print("A")
elif num > 80 and 89:
    print("B")
elif num > 70 and 79:
    print("C")
elif num > 60 and 69:
    print("D")
else:
    print("Fail")

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    print("The largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")
if operator == '+':
    result = num1 + num2
    print("Result:", result)
elif operator == '-':
    result = num1 - num2
    print("Result:", result)
elif operator == '*':
    result = num1 * num2
    print("Result:", result)
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator.")