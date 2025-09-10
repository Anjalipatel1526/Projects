#- Concatenate two lists: `[1, 2, 3]` and `[4, 5, 6]`
#Multiply the resulting list 2 times
a=[1,2,3]
b=[4,5,6]
sum=a+b
mul=sum*2
print(mul)

#ake two lists as input from the user. Compare them using:Equality (`==`) Relational (`<`, `>`) operators
# Take two lists as input from the user
list1 = int(input("Enter the first list: "))
list2 = int(input("Enter the second list: "))
if list1 == list2:
    print("Both lists are equal.")
else:
    print("The lists are not equal.")
# Compare using relational operators (based on elements)
if list1 > list2:
    print("First list is greater than second list.")
elif list1 < list2:
    print("Second list is greater than first list.")


#Create a list of numbers from 1 to 10. Ask the user to enter a number. Check: If the number is in the list ,If the number is not in the list
numbers=list(range(1,11))
num=int(input("Enter the number: "))
if num in numbers:
    print("The number is in the list.")
else:
    print("The number is not in the list.")

#Create a list with some elements. Use the clear() method to remove all elements and print the empty list.
x = [1, 2, 3,4,5,6,7,8,9]
x.clear()
print(x)

#Access Elements in a Nested List
n = [100, 200, [300, 400, [500, 600]]]
print(n)
print(n[0])
print(n[1])
print(n[2][0])
print(n[2][1])
print(n[2][2][0])
print(n[2][2][1])

#Create a 3x3 matrix using a nested list. Print:All rows one by one Elements in matrix style using nested loops
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print("Matrix (Nested List):")
print(matrix)
print("\nElements by Row-wise:")
for row in matrix:
    print(row)
print("\nElements by Matrix style:")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()

#Use list comprehension to generate a list of squares of numbers from 1 to 15.
squares = [x*x for x in range(1, 16)]
print(squares)

# Filter Even and Odd Numbers
even=[x for x in range(1, 31) if x % 2 == 0]
print(even)
odd=[x for x in range(1, 31) if x % 2 != 0]
print(odd)

#Given a list of strings like ["HELLO", "WORLD", "PYTHON"], use list comprehension to convert them all to lowercase
words=["HELLO","WORLD","PYTHON"]
lowercase=[word.lower() for word in words]
print(lowercase)

#Given a list of words, use list comprehension to create a new list containing only the vowels from each word.
words = ['apple', 'banana', 'grapes']
vowels_list = [[ch for ch in word if ch in "aeiouAEIOU"] for word in words]
print(vowels_list)
