#Assignment 1: Tuple Creation
a=()
print(a)
b=(100)
print(b)
c=(1,2,3,4,5)
print(c)

#Assignment 2: Indexing and Slicing
t = (10, 20, 30, 40, 50)
print("First element:", t[0])
print("Last element:", t[-1])
print("Slice from index 1 to 3:", t[1:4])

#Pack values 5, 10, 15, 20 into a tuple, then unpack them into variables a, b, c, d and print each variable.
t = (5, 10, 15, 20)
a, b, c, d = t
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

#Assignment 4: Use of len()
t=(1,2,3,4,5,6,7,8,9)
print(len(t))

# Assignment 5: Use of count()
t = (1, 2, 3, 1, 4, 1, 5)
print(t.count(1))

#Assignment 6: Use of index()
t = (10, 20, 30, 10, 40)
print(t.index(20))

# Assignment 7: Sorting a Tuple
t = (40, 10, 30, 20)
t1=sorted(t)
print(t1)

# Assignment 8: Min and Max
t = (5, 2, 9, 1, 7)
print(min(t))
print(max(t))

#Assignment 9: Convert List to Tuple
l = [10, 20, 30, 40]
t=tuple(l)
print("Tuples:",t)

# Assignment 10: Tuple from Range
even_tuple = tuple(range(2, 21, 2))
print("Even numbers tuple:", even_tuple)

