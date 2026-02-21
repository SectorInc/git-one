# #functions are used to perform a specific task. It is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
# print('to print a value')
# input('to take an input from user')
# #methods are functions that are associated with an object. They are called on an object and can access and modify the object's data. 
# print('to print a value'.upper()) #this is a method that converts the string to uppercase
# print('T OPRINT A VALUE'.lower()) #this is a method that converts the string to lowercase
# print('to print a value'.split()) #this is a method that splits the string into a li2st of words
# print('to print a value'.replace('print','display')) #this is a method that replaces a word in the string with another word
# #new functions
# print(abs(-5)) #this is a function that returns the absolute value of a number
# print(round(3.14159,2)) #this is a function that rounds a number
# print(max(1,2,3)) #this is a function that returns the maximum value from a list of numbers
# print(min(1,2,3)) #this is a function that returns the minimum value
# print(len('to print a value')) #this is a function that returns the length of a string  
a=int(input('enter the width of the triangle'))
b=int(input('enter the height of the triangle'))
c=((a**2)+(b**2))**0.5
print('the hypotenuse of the triangle is',round(c,2))
