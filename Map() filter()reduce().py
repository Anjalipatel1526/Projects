#map
#Double each number in the list using map()
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)

#Convert list of strings to uppercase using map()
words = ["apple", "banana", "cherry"]
uppercase_words = list(map(str.upper, words))
print(uppercase_words)

#square the number
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

#Convert a list of integers to strings using map()
numbers = [1, 2, 3, 4, 5]
string_numbers = list(map(str, numbers))
print(string_numbers)

#Extract the first character of each word using map()
words = ["hello", "world", "python"]
first_chars = list(map(lambda word: word[0], words))
print(first_chars)

#filter()
#**Filter only even numbers from a list using `filter()`.**
l = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, l))
print(result)

#Filter out words longer than 5 letters.
num=["apple","banana","cherry","kiwi"]
word=list(filter(lambda num: len(num) <= 5,num))
print(word)

#**Filter numbers that are divisible by 3.**
#Input: `[3, 6, 8, 9, 11, 12]
number=[3,6,8,9,11,12]
div_3=list(filter(lambda x: x % 3 == 0, number))
print(div_3)

#reduce()
#**Find the sum of all numbers in a list using `reduce()`.**
#Input: `[1, 2, 3, 4]`
from functools import reduce
l = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, l)
print(result)

#Find the product of all numbers in a list using reduce().
from functools import reduce
l = [1, 2, 3, 4]
result = reduce(lambda x, y: x * y, l)
print(result)

