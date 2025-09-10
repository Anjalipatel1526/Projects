#membership operator
def contains_all_vowels(sentence):
    sentence = sentence.lower()
    vowels = 'aeiou'
    for vowel in vowels:
        if vowel not in sentence:
            return False
    return True
sentence = input("Enter a sentence: ")
if contains_all_vowels(sentence):
    print("All vowels are present.")
else:
    print("Not all vowels are present.")


scores = {"Ram": 88, "Anu": 75, "Zara": 95}
if "Zara" in scores and scores["Zara"] > 90:
    print("Zara score is greater than 90.")
else:
    print(" Zara score is not greater than 90.")


cart = ["pen", "notebook", "eraser"]
if "scale" not in cart:
    print(cart.append("scale"))
else:
    print(cart.remove("scale"))
print(cart)

#identity operator
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)
print(list1 is list2)

x = 256
y = 256
z = 300
w = 300
print(x is y)
print(z is w)

def check_none(value):
    if value is None:
        print("No input")
    else:
        print("Receviced input")
check_none(None)

num = 8
num *=2
num -=6
num **=2
print("final result",num)

num = 100
num //=4
num %=6
num +=2
print("final result:",num)

count = 0
for i in range(1, 11):
    if i % 2 == 0:
        count += i
print("Sum of even numbers from 1 to 10:", count)