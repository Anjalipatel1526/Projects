list = []
list.append('Anju')
list.append('jee')
list.append('vidhi')
list.append('sharmi')
list.append('loga')
print("append List:",list)

#insert
n = [1, 2, 3, 4, 5]
n.insert(0,100)
n.insert(3,100)
n.append(100)
print(n)

list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2)
print("merge list:",list1)

num=[1, 2, 3, 2, 4, 2, 5]
num.remove(2)
print(num)

num=[10,20,30,40,50]
num.pop()
print("after pop",num)
num.pop(1)
print("after pop 1:",num)


# Add all elements divisible by 7 up to 100
list = []
for i in range(101):
    if i % 7 == 0:
        list.append(i)
print(list)

#Ask the user for a number. If the number is present in a predefined list, remove it; otherwise, print "Not Found".
numbers = [10, 20, 30, 40, 50]
num = int(input("Enter a number: "))
if num in numbers:
    numbers.remove(num)
    print(numbers)
else:
    print("Not Found")

#Create a list of 3 usernames. Insert a new user at the beginning using insert().
n = ['anju','jee','vidhi']
n.insert(0,'sharmi')
print(n)

#Create a list of 5 colors and reverse their order using reverse().
colors=['red','green','blue','yellow','black']
colors.reverse()
print(colors)

#Take a list of integers from the user and sort them in ascending order using sort().
numbers = input("Enter numbers: ").split()#space appaer
x = [int(x) for x in numbers]
x.sort()
print(numbers)

#Create a list of 5 fruits and sort them in alphabetical order.
furits=['banana','mango','jackfurit','apple','guva']
furits.sort()
print(furits)

#Create a list of 10 random numbers. Sort them in descending order using sort(reverse=True).
list=[65,25,45,20,40,13,18,24,5,84]
list.sort(reverse=True)
print(list)

#Create a list of words like ["apple", "banana", "kiwi", "grapes"] and sort them based on word length using sort() with key=len.
words = ["apple", "banana", "kiwi", "grapes"]
words.sort(key=len)
print("Sorted by length:", words)

#Sort a List of Tuples
students = [("John", 80), ("Alice", 95), ("Bob", 70)]
students.sort(key=lambda student: student[1])
print(students)


#Take two lists of numbers from the user, combine them using extend(), and then sort the final list in ascending and descending order.
# Take two lists from user
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
# Combine and sort
list1.extend(list2)
print("Ascending:", sorted(list1))
print("Descending:", sorted(list1, reverse=True))

