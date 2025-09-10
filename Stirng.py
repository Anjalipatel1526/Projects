name = "Anjanikumar"
reversed = name[::-1]
print("Original String:", name)
print("Reversed String:", reversed)

name = "Learning Python is very Easy"
reversed = " ".join(name.split()[::-1])
print("Original String:", name)
print("Reversed String:", reversed)

name = "Python is easy"
word=name.split()
reversed = " ".join(word[::-1] for word in word)
print("Original String:", name)
print("Original String:", name)
print("Reversed String:", reversed)

s = input("Enter a string: ")
odd_chars = s[0::2]
even_chars = s[1::2]
print("Characters at odd positions:", odd_chars)
print("Characters at even positions:", even_chars)


s = "B4A1D3"
result = "".join(sorted(s, key=lambda ch: (ch.isdigit(), ch)))
print("Sorted String:", result)

s = "a4b3c2"
result = "".join(s[i] * int(s[i+1]) for i in range(0, len(s), 2))
print("program required:",result)


s = "ABCDABBCDABBBCCCDDEEEF"
print("removed duplicate:","".join(dict.fromkeys(s)))

word="ABCABCABBCDE"
print("occurrences of each character :",','.join(f"{c}-{s.count(c)}" for c in sorted(set(s), key=s.index)))

