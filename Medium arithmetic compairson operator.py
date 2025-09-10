#Arithmetic , Comparison,Logical
#Medium level
a=int(input("enter the a num:"))
b=int(input("enter the b num:"))
c=int(input("enter the c num:"))
Average=(a+b+c)/3
print("average of number is",Average)

P=int(input("enter the p value:"))
r=int(input("enter the r value:"))
T=int(input("enter the t value:"))
A= P * (1 + r / 100) ** T
print("the total compound intrest are",A)


num = input("Enter a number: ")
sum = 0
for digit in num:
    if digit.isdigit():
        sum += int(digit)
print("The sum of the digits is:", sum)


number = float(input("Enter a number: "))
if number > 10 and number < 50:
    print("The number is greater than 10 and less than 50.")
else:
    print("The number is not range between 10 and 50.")


number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5==0:
    print("The number is divisible by 3 and 5.")
else:
    print("The number is not both divisible by 3 and 5.")

num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
if num1 >= num2:
    print("The num1 greater than and equal to num2")
else:
    print("The num1 less than and equal to num2")

number = int(input("Enter a number: "))
if number % 2 == 0 and number > 50:
    print("The number is even and greater than 50.")
else:
    print("The number is not both even and greater than 50.")


number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5==0:
    print("The number is divisible by 3 and 5.")
else:
    print("The number is divisible by 3 and 5.")

age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").strip().lower()
if is_student or age >= 60:
    print("The person is eligible for a discount.")
else:
    print("The person is not eligible for a discount.")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum = num1 + num2
diff =(num1 - num2)
if sum > 100 and diff < 10:
    print("The sum is greater than 100 and the difference is less than 10.")
else:
    print(" The conditions are not both satisfied.")

