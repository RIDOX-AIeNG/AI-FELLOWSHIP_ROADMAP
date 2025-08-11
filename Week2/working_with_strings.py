# Single qoutes
name = 'Ada'
print(name)

#Double Quotes
greeting = "Hello"
print(greeting)

# Triple Qoutes (for multi_line strings)
story = '''Once upon a time,
there was a coder named Ada'''
print(story)

#String with numbers and symbols
password = "p@ssword123"
print(password)

#Indexing
word = "python"
print(word[0]) #p
print(word[-1]) #n

#slicing 
word = "python"
print(word[0:4]) # pyth
print(word[2:]) # thon
print(word[:3]) # pyt
print(word[::2]) # Pto
print(word[::-1])

#String Concatenation $ Repetition
# Concatenation
a = "Hello"
b = "World"
print(a + " " + b) #Hello World

#Repetition
word = "Hi! "
print(word * 3) #prints the word 3 times

#String Searching $ Checking
#Mmembership
text = "Python Programming"
print("Pyhton" in text) #true
print("Java" not in text) #true

#find() / rfind()- find and remove

text = "Hello World"
print(text.find("o")) #4
print(text.rfind("o")) #7

#index() / rindex()
text ="Hello World"
print(text.index("World"))

#startswith() / endswith()
filename = "data.csv"
print(filename.startswith("data")) #True
print(filename.endswith(".csv")) #True