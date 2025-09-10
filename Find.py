#Find the first occurrence of "a" in "banana"
text = "banana"
char = text.index("a")
print("First occurrence:", char)

#Find the index of "Java" in "Python and JavaScript"
text = "Python and JavaScript"
char = text.index("Java")
print("index of java:", char)

text = "big data analytics"
result = text.find("data",5)
print(result)

text = "Python is good. Python is easy."
first = text.find("Python")
second = text.find("Python", first + 1)
print("First occurrence:", first)
print("Second occurrence:", second)

word="css and javasrcpit"
text=word.find("HTML")
if text==-1:
    print("1")
else:
    print(text)

