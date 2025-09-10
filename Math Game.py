import random
import operator
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}
# Randomly choose numbers and an operator
num1 = random.randint(1, 20)
num2 = random.randint(1, 20)
op = random.choice(list(ops.keys()))
answer = ops[op](num1, num2)

# Ask the question
user = float(input(f"What is {num1} {op} {num2}? "))

# Check the answer
if user == answer:
    print("✅ Correct!")
else:
    print(f"❌ Wrong! The answer is {answer}")
