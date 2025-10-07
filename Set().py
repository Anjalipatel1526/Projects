#Create a Set and Print It
set={10,20,30,40,50}
print(set)

#Add and Remove Elements
set={10,20,30,40}
set.add(50)
print(set)
set.remove(20)
print(set)

# Set Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("union",set1|set2)
#Set Intersection
print("intersection",set1-set2)
print("5" in set2)

#Dictionary Assignments (5 Easy Questions)
# Create and Print Dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(person)

#Given a dictionary {"name": "Alice", "age": 22}, write code to print the value of the "name" key.
person = {"name": "Alice", "age": 22}
print(person["name"])

#Write a program to change the "age" value in the dictionary from 22 to 23.
person = {"name": "Alice", "age": 22}
person["age"] = 23
print(person)

#Add a new key "grade": "A" to a dictionary and then remove the "city" key.
# Original dictionary
student = {"name": "Alice", "age": 22, "city": "New York"}
student["grade"] = "A"
student.pop("city")
print(student)

#Write a program to print all keys and their values from the dictionary:
student = {"name": "Bob", "age": 20, "grade": "B"}
for key, value in student.items():
    print(key, ":", value)
