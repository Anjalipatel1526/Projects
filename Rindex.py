text = "hello world hello"
result = text.rindex("o")
print(result)


text = "banana"
last_index= text.rindex("a")
print(last_index)


text = "example"
try:
    last_index = text.rindex("x")
    print(last_index)
except ValueError:
    print("'x' not found in the string.")
