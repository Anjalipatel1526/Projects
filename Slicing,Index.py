name="Python programming"
first=name[0]
last=name[-1]
last_elment=name[7:]
print("first character:",first)
print("last character:",last)
print("last element:",last_elment)

#reverse the string
data="data science"
resverse=data[::-1]
print("reverse data:",resverse)

a="Machine learning"
seconnd_element=a[::2]
print("seconnd element:",seconnd_element)

#negative indexing
code="python"
last_char=code[-4:]
print("last character:",last_char)

#silicing plus concatenation
text = "I love Python"
new_text = text[:2] + "Java" + text[6:]
print(new_text)

#slice extract
word="Frontend developer"
element=word[9:]
print("Extract:",element)


#Print the first 5 characters and last 5 characters of "Data Analysis".
data="Data Analysis"
first_char=data[:5]
last_char=data[-5:]
print("First character:",first_char)
print("Last character:",last_char)

#Get a substring from "Full Stack Developer" that starts from index 5 to the end
word="Full Stack Developer"
text=word[5:]
print("Text:",text)

#Slice "Artificial Intelligence" to get "Intel"
text="Artifical Intelligence"
word=text[10:15]
print("Text:",word)

