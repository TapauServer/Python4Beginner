#!/bin/python3


#variable and Methods

quote = "You stupid little script kitty"

print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #titlecase

print(len(quote)) #lengthcharacter


#typeofdata

name = "Tapau"
age = 20
gpa = 3.7

print(str(name)) #string
print(int(age)) #integer
print(float(gpa)) #float

print("My name is " + name + " ,I am " + str(age) + " years old and my pointer is " + str(gpa))


#changingvariablevalue

age += 5 #tambah
print(age)

age -= 5 #tolak
print(age)

age *= 5 #darab
print(age)

age /= 5 #bahagi
print(age)


#changing value by adding variable

zamandulu = 1960
age += zamandulu
print(int(age))
