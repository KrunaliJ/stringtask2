#python-modify strings:Python has a set of built-in methods that you can use on strings.

#upper Case:The upper() method returns the string in upper case

a="python"
print(a.upper())

#lower case:the lower() method returns the string in lower case

b="Hello World"
print(b.lower())

#remove whitespace:Whitespace is the space before and/or after the actual text, and very often you want to remove this space
#for removing the whitespace from the beginning or from the end we have to use strip() method

c="python is a programming language "
print(c.strip())

#replace string:The replace() method replaces a string with another string

d='hello,world!'
print(d.replace("l",'J'))

#split string:The split() method returns a list where the text between the specified separator becomes the list items
#The split() method splits the string into substrings if it finds instances of the separator

print(d.split('o')) #['hell', ',w', 'rld!']

#string Concatenation:To concatenate, or combine, two strings you can use the + operator
#Merge variable a with variable b into variable c

e=a+c
print(e) #pythonpython is a programming language 

#to add space between them add a " ":
e=a+" "+c
print(e)

#pyhton-format-strongs
#string format:we can combine strings and numbers by using f-strings or the format() method!
'''
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
'''
age=35
txt=f'my name is joy,i am {age}'
print(txt)

#placeholders and modifiers:A placeholder can contain variables, operations, functions, and modifiers to format the value.

price=78
txt=f'the price is {price} dollars'
print(txt)

'''
A placeholder can include a modifier to format the value.
A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals
'''
vegprice=34
veg=f'the price of vegs is {vegprice:.2f} dollars '
print(veg)