word="elephant"
text=word.index("e")
print(text)

text = "hello"
try:
    result = text.index("x")
    print(result)
except ValueError:
    print("Character not found")

word="I love Java"
text=word.index("Java")
print(text)

