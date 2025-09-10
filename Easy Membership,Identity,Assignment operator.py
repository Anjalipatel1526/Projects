#membership
if "a" in "banana":
    print('"a" is in the string "banana".')
else:
    print('"a" is not in the string "banana".')

A=[1,2,3,4]
if A not in A:
    print("5 is not in list")
else:
    print("5 is in list")

colour=["red","blue","green"]
if "yellow" not in colour:
    print("Not found it")
else:
    print("found it")

#identity
a=10
b=10
print(a is b)

a=[1,2,3]
b=a
c=[1,2,3]
print(a is b)
print(a is c)

def check_none(value):
    if value is None:
        print("Input is None")
    else:
        print("Input is not None")
check_none(None)

#assignment
x = 5
x += 3
print(x)

num = 4
num *= 2
print(num)


value = 15
value %= 4
print(value)

