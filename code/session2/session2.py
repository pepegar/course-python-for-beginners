#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 12:13:01 2020

@author: pepe
"""


#%% 
# Calling functions

print()
print("hello", "world")
input("tell me your name: ")
str(3)
int("32")

#%%
# declaring functions

def calculate_area_triangle(base, height):
    print(base * height / 2)

area = calculate_area_triangle(4, 23)

print("the area is " + str(area))


#%%
# returning values from functions

def calculate_area_triangle_with_output(base, height):
    return base * height / 2

area = calculate_area_triangle_with_output(4, 2)

print("the area is " + str(area))

#%%
# Boolean operators - comparision

print("Hello" == "Hello")
print("Hello" == "hello")
print("Hello" != "hello")

#%%

print(6 > 7)
print(6 > 6)
print(6 >= 6)

#%%

age = 27
brothers_age = 26

print(age > brothers_age)

#%%
# boolean operators - logical

# and

print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

#%%
# or

print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

#%%
# not

print(not True) # False
print(not False) # True


#%%
# if statement

age = input("how old are you? ")
accompanied_by_adult = True

if int(age) >= 18:
    print("you can drive!")
else:
    if int(age) >= 16 and accompanied_by_adult:
        print("you can drive, as long as you're with an adult")
    else:
        print("go home kiddo")

#%%
# elif

age = input("how old are you? ")
accompanied_by_adult = True
user_with_brother = False

if int(age) >= 18:
    print("you can drive!")
elif int(age) >= 16 and accompanied_by_adult:
    print("you can drive as long as you're with an adult")
elif user_with_brother:
    print("you can drive as long as you're with an adult")
else:
    print("go home kiddo!")

#%%
# Practice time!Let’s do some practice. We have to create a functioncalculate_area_triangle_rectanglethat can calculate the area ofeither a triangle or a rectangle.

def calculate_area_triangle_or_rectangle(base, height, shape):
    if shape == "triangle":
        return base * height / 2
    elif shape == "rectangle":
        return base * height
    else:
        print("not today good person")

print(calculate_area_triangle_or_rectangle(5, 2, "triangle"))
print(calculate_area_triangle_or_rectangle(5, 2, "rectangle"))
print(calculate_area_triangle_or_rectangle(5, 2, "circle"))






































