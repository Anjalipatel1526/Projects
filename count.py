text = "banana"
count_a = text.count("a")
print("Number of times 'a' appears:", count_a)

text = "This is a test. This is only a test"
count= text.count("is")
print("Number of times 'is' appears:", count)

text = "Hello world from Python"
count= text.count(" ")
print("Number of times spaces ' ' appears:", count)

text = "Python Python Python"
count= text.count("Python")
print("Number of times 'Python' appears:", count)

text = "Artificial Intelligence"
vowels = "aeiouAEIOU"
total_vowels = 0
for v in vowels:
    total_vowels += text.count(v)
print("Total vowels:", total_vowels)


