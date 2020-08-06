---
title: Python for Beginners, session 4
author: Pepe García
email: jgarciah@faculty.ie.edu
date: 2020-08-08
lang: en
---


# Plan for today

>- review last day exercises
>- learn about dictionaries
>- what's the path forward

# Last day exercises

\begin{exampleblock}{Alert}
That's an exampleblock
\end{exampleblock}

\begin{alertblock}{Alert}
That's an alertblock
\end{alertblock}

# Dictionaries


# Dictionaries

Dictionaries are another kind of collection in Python.  Dictionaries 
map keys to values.

# Creating dictionaries

We use curly brackets **{}** to declare dictionaries.

```python
translations = {
    "es": "Hola!",
    "it": "Ciao!",
    "en": "Hello!"
}
```

colon for separating key and value

comma for separating entries

# Creating dictionaries

We can also create empty dictionaries

```python
translations = {}
```

# Creating dictionaries

# Adding elements

We add elements to dictionaries given their specific index:

```python
translations = {}
translations["en"] = "Hello"
translations["it"] = "Ciao"
translations["es"] = "Hola"
```

# Updating elements

we always can change a value in the dictionary by re-assigning the key

```python
translations = {}
translations["en"] = "Hello"
translations["en"] = "WHATUP!"
```

# Updating elements

# Deleting elements

We can delete an element of the dictionary using the **pop** method

```python
translations = {}
translations["en"] = "Hello"
translations.pop("en")
```

# Deleting elements

# Getting all keys or values

We can allways get all **keys** or **values** from the dict as a list
using either the **.keys()** or **.values()** method

```python
users = {
  1: "Pepe",
  22: "Peter",
  44143: "Johnny",
  2: "Chuck"
}

users.keys()
users.values()
```

# Getting all keys or values

# for loops

In the same way we used **for** loops to iterate over elements of a
list, we can use them to iterate over elements of a dictionary.

 

The difference is that, with dictionaries, the **iteration variable**
will represent the **current key**, not the **current value**.

# for loops

```python
band = {
  "johnny": "plays drums",
  "joey": "plays guitar",
  "markee": "sings",
  "dee-dee": "plays bass-guitar"
}

for member in band:
  print(member + " " + band[member] + " in The Ramones")
```


# The path forward

from now you probably don't want

# Thank you all!

Any comments or suggestions are more than welcome :D

Pepe Garcia <jgarciah@faculty.ie.edu>
