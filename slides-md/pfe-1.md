---
title: Python for Beginners
author: Pepe García
email: jgarciah@faculty.ie.edu
date: 2020-04-20
lang: en
---

# Python for Beginners, session 1

# About

## The Professor

Pepe García

. . . 

jgarciah\@faculty.ie.edu

. . .

Tech Lead @ 47deg

. . .

Ask me anything

---

# About

## The Course

- 7 sync sessions

. . . 

- 3 async sessions

---

# Learning Objectives

- Learn What's programming

. . . 

- Understand how computers execute programs

. . . 

- Learn the basics of Python

---

# Plan for this session

- Learn about software

. . .

- Understand what are algorithms

. . .

- Understand what are data structures

# Language

Throughout this course we will use Python as our programming language,
but there are many more!

# Language

There are several ways for categorizing programming languages.

## Language classification

Language     Paradigm          Execution     Purpose
------------ ----------------- ------------- ----------
Python       imperative        interpreted   general
Java         object oriented   compiled      general
Javascript   imperative        interpreted   general
Haskell      functional        compiled      general
SQL          declarative       interpreted   specific
HTML         declarative       interpreted   specific

# Language

## Python

Python is one of the most used languages right now.  Its applications
range from Data Science to Web servers

# How do we write code?

---

# How do we write code?

Coding is basically putting words together following a programming
language specification.

---

# How do we write code?

We can put these words directly in a text file and then execute it
as a program.

![](./img/code.jpg){height=300px}

---

# How do we write code?

Or we can feed these words directly into the programming language
console.

---

# Demo

## Spyder

Spyder is the editor we will use for writing Python code.

Let's open it and try some expressions in the console.

---

# Programs

---

# Programs

## What is a program?

A program is a piece of software with a specific
task.

. . .

This task can be something BIG, like handling a nuclear reactor, or
something small like Ctrl-c/Ctrl-v.

. . .

There are two main components of programs, **algorithms** & **data structures.**

---

# Algorithms

---

# Algorithms

## What is an algorithm?

. . .

An algorithm is a sequence of steps that guide the computer in how to
solve a problem

---

# Algorithms

![](./img/SFF-1.gif){ height=250px }

[link to the video](https://www.youtube.com/watch?v=k0xgjUhEG3U)

---

# Algorithms

What's wrong with this algorithm? why did Wolowitz needed to fix it?

. . .

There was an infinite loop, a **bug**

---

# Algorithms

![](./img/SFF-2.gif){ height=250px }


---

# Algorithms

## What other cases of bugs do we know?

---

# Algorithms

![](./img/knight.png)

[https://www.bloomberg.com/news/articles/2012-08-02/knight-shows-how-to-lose-440-million-in-30-minutes](https://www.bloomberg.com/news/articles/2012-08-02/knight-shows-how-to-lose-440-million-in-30-minutes)

---

# Checkpoint

Are there any questions/comments so far?

# 10 minutes break

---

# Python for Beginners, session 2

---

# Python for Beginners, session 2


## Plan for this session

- Python basic datatypes

. . .

-   variables

. . .

-   operators

# Datatypes

Datatypes tell Python how we want to use the data.  There are several
primitive data types in Python such as bool, int, str, float.

# Datatypes

## Integers

Integers (or ints) represent whole numbers without decimal parts.  We
create them by using their numeric representation directly

```python
1
234
432432
```

. . . 

## Demo

---

# Datatypes

## Floating point numbers

floats represent numbers that have a fractional part.  We use a dot to
separate the integer and fractional parts

```python
3.14
1.0
33.33
```

. . .

## Demo

---

# Datatypes

## Strings

Strings are used for textual representation. They can be created using
either double or simple quotes.

```python
'this is a string'
"this is another string"
```

. . .

## Demo

---

# Datatypes

## Booleans

Booleans represent truthiness. There are only two values in for the bool
type in Python: True and False

```python
True
False
```

. . .

## Demo

---

# Getting the type of a value

We can always ask ask a value for its type using the **type(value)**
function

```python
type("patata")
```

---

# Getting the type of a value

Inside Spyder, check what's the type of the following expressions:

```python
"there is some text here"
1
True
44.4
'true'
'False'
2
'33.3'
```

## Does someone want to do it?

---

# Operators

Operators are symbols in the language that perform different kinds of
computations on values

They're binary

# Arithmetic Operators

  symbol   meaning
  -------- ------------------
  `+`       sum
  `-`       substraction
  `*`       multiplication
  `/`        division
  `**`     exponentiation
  `//`       floored division
  `%`       modulus

# Arithmetic Operators

## Rules of precedence

-   Parentheses
-   Exponentiation
-   Multiplication/Division
-   Sum/Substraction
-   when operators have the same precedence, evaluate left to right

. . .

## Demo

# String operators

sum and multiplication operators work on strings too.  They're used to
concatenate and multiply strings, respectively.

. . .

## Demo


# Variables

Variables are names that point to values in Python.

# Variables

## Naming variables

It's important to be as descriptive as possible when naming variables

There are some naming rules we should obey

# Variables

## Naming rules

-   variable names can't start with a number

. . .

-   variable names can't contain special characters such as `!`, `@`, `.`

. . .

-   Can't be one of the reserved words  

# Variables

## Reserved words

|            |           |          |            |         |
|------------|-----------|----------|------------|---------|
| `and`      | `del`     | `from`   | `None`     | `True`  |
| `as`       | `elif`    | `global` | `nonlocal` | `try`   |
| `assert`   | `else`    | `if`     | `not`      | `while` |
| `break`    | `except`  | `import` | `or`       | `with`  |
| `class`    | `False`   | `in`     | `pass`     | `yield` |
| `continue` | `finally` | `is`     | `raise`    |         |
| `def`      | `for`     | `lambda` | `return`   |         |

# Variables

## Mutability

In Python variables are mutable. This means that we can change their
value at any time

```python
name = "Pepe"
print(name)

name = "Jose"
print(name)
```

# Converting values

There are some times when we need to convert a value from one type to
another.

We use the **int()**, **bool()**, **str()**, and **float()** functions for that

. . .

```python
int('23')
bool(1)
bool(0)
str(True)
float("3.2")
```

# Printing output

One can print output using the **print()** function

# User input

There is a handy function **input()** that allows us to capture input
from the user

```python
name = input("Tell me your name: ")

print("hello, " + name)
```

# Recap

>- Datatypes (int, float, bool, str)
>- Variables (naming, mutability)
>- Operators (arithmetic, precedence, string operators)
>- Converting values
>- User input

# Exercises for the Async session

1. Create a program that calculates the total number of seconds in an hour
   and prints it afterwards.

. . .

2. How does the following expression evaluate?
   2 + (3 + 4) + (5 * 33 ** 34)

. . .

3. Create a program that asks the user for their age and their mother's 
   age and calculate the age difference

. . .

4. Make the following expressions work (use Python console for this one)

```
3 + "3"
'there are ' + 4 ' dogs barking'
```

# Reading for the async session

**What Is Code** is a great essay by Paul Ford.  It's from 2015 but has aged
(and will age) very well.

[[https://www.bloomberg.com/graphics/2015-paul-ford-what-is-code/]{style="font-size:0.7em"}](https://www.bloomberg.com/graphics/2015-paul-ford-what-is-code/)