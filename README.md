# Automate Boring Stuff

## Chapter 1

### Primitive Data Types
- int
- float
- string
- boolean

### Aritmethic Operators
Always evaluate to a value.
| Symbol   | Meaning          |
| ---      | ---              |
| \*\*     | exponent         |
| \*       | multiplication   |
| /        | division         |
| //       | integer division |
| %        | module           |
| \+       | sum              |
| \-       | difference       |

### String Operators
Always evaluate to a String.
| Symbol   | Meaning          |
| ---      | ---              |
| \+       | concatenate      |
| \*       | replicate        |
> [!IMPORTANT]
> Can not apply these operators directly to a number, must convert the number to a string first. Python does not implicity convert number to a String.

### Comparison Operators
Always evaluate to a boolean.
| Symbol   | Meaning                  |
| ---      | ---                      |
| ==       | equals to                |
| !=       | not equals to            |
| \>       | greater than             |
| <        | less than                |
| \>=      | graeter than or equal to |
| <=       | less than or equal to    |
> [!WARNING]
> == equals to compares two values and let you know if they are equal or not, it always return a boolean value. = an assignment is used to put the value on the left into the variable at right. Do not confuse them.

### Boolean Operators
Always evaluate to a boolean.
| Symbol   | Meaning                      |
| ---      | ---                          |
| not      | evaluates to the opposite    |
| and      | True only if both are true   |
| or       | False only if both are false |

## Chapter 2

### Flow Control Statements
A Flow Control statement represent a behavior usually controlled by a condition and followed by a clause. A Condition is an expression that evaluates to a boolean value. The Clause is a block of code that executes, according to the behavior provided by the statement used.

### Common Statements
- if
- while
- for
- break
- continue

### If Statement
if - may be used to decide which clause will be executed according to a condition or a series of conditions. The else and elif block is optional. elif blocks may be used to check for more than one case.

minimun if:
```python
if name == 'Alice':
    print('this clause says: Hi Alice!')
```

checking for something or else (at least one clause will be executed)
```python
if name == 'Alice':
    print('this clause says: Hi Alice!')
else:
    print('this clause says: you are not Alice')
```

checking for more than one case (one or none case is executed)
```python
if age < 20:
    print('this clause says: you are under 20!')
elif age < 40:
    print('this clause says: you are under 40!')
elif age < 60:
    print('this clause says: you are under 60!')
```
> [!TIP]
> When checking for multiple conditions it is very important to consider the order in which the checks will be done.

checking for more than one case or else (at least one clause will be executed)
```python
if age < 20:
    print('this clause says: you are under 20!')
elif age < 40:
    print('this clause says: you are under 40!')
elif age < 60:
    print('this clause says: you are under 60!')
else:
    print('this clause says: you are over 59!')
```

### While Statement
While, also known as loop, repeats the clause while the condition is true.

traditional while loop
```python
while age < 20:                     #this is the condition
    print('another year passes')    #this block is a clause
    age = age + 1
```

infinite loop
```python
while True:
    print('this happens over and onver, forever!')
```
> [!IMPORTANT]
> Whenever you use a loop check for the possibility of an infinite loop, usualy it is not desirable. In case you want to use an infinite loop, make sure you check for a condition inside the clause and insert a break instruction.

### Break Statement
The Break statement jumps out of the block. Usually used to jump out of a loop.

Can use a break statement to jump out of an infinite loop checking for a condition
```python
while True:
    print('this could be the clause')
    if condition:
        print('do something then...')
        break
```

Can also be used to jump subsequent interactions in a for loop
```python
for x in range(100):
    if x == 10:
        print('when it reaches 10, skips all the following interactions')
        break
```

### Continue Statement
The Continue statement jumps back to the start of the loop (next iteration) and skips the following code.

Can use a continue statement to skip a portion of code when a certain condition is reached
```python

while True:
    print('what is your name?')
    name = input()
    if name = 'Alice':
        print('Alice is not welcome')
        continue
    print('hello ' + name + '!')        #this part is not executed when name == 'Alice' because continue jumps to the next interaction
```

### For Statement
The For statemnet is used when we want to execute a block of code (clause) a specific number of times. This statement consists of four parts:
1 - the start index
2 - the stop index
3 - the step index
4 - the clause

For statements are often used in conjunction whith the range function to specify the stop point, the increment after each interaction and the initial value.
```python
for x in range(5):          #x is the current element, 5 means it will loop from 0 to 4 (5 elements)
    print('do something')   #this is the clause
```

### Importing Modules

```python
# importing a single module
import random

# using an imported module
random.randint(1, 10)       # uses randint from random to generate a random number between 1 and 10
```

```python
# importing multiple modules
import random, sys, os, math
```

```python
# this allows to use the function without the module name, similar to import static from java
from random import *

# using the import
randint(1, 10)
```
> [!WARNING]
> importing with a from statement allows you to ommit the modulename prefix, but it is not considered a good practive and should be avoided. Using the prefix improve the code readability.

### Builtin Functions
sys.exit() - terminates a program. must be imported before use.
range()
The range function has two optional parameters (start, step).
```python
# when used this way, start and step are set to a default value
# default values: start = 0, step = 1
range(stop)

# when used this way, step is set to a default value
# default value: step = 1
range(start, stop)

# when used this way, all values are given by the user
range(start, stop, step)
```

input()
len(someString)
str(value)
int(string)
float(string)
print()

## Chapter 3

Functions can be used to avoid code repetition and improve mantainability. It aggregates a logical unit.

declaration

def functionName(arguments):
    body of the function
    return expression

call to a function

functionName(arguments)

None == null

in Python every function must evaluate to a value, so when no return statement is used or even an empty return statement, the function returns None.

Named arguments - it is possbile to pass arguments ignoring the order if you user named arguments.

print('Hello', end='!')
'> Hello!

print('Darksiders', 'Tomb Raider', 'Uncharted', sep='/')
'> Darksiders/Tomb Raider/Uncharted

Global Scope - it is everything that is not contained in a block of code. Local variables can not be accessed through the global scope.
Local Scope - it is everything that is contained in a block of code. Global variables can be acessed through a local scope. A Local Scope can not access another Local Scope.

It is a good practice to interact with the global scope only through the arguments and return values of a function.
You cna force a function to not create a local variable by declaring it with the global keyword.

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
'> spam

- if it is outside of any function, it is global
- if it is declared in a function local scope with global, then it is global
- if it is not assigned inside a function, it is global
- if it is assigned inside a function, it is local

variables inside a function will always be local or global, they can not be both.

Exception Handling

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Ivalid argument')


## Chapter 4

### List Data Type
A list is a value that contains multiple values in an ordered sequence. A list begins with an opening square bracket and finishes with a closing square bracket. It contains items and they are separated by a comma.

```python
# literal list
['item1', 'item2', 'item3',]

# empty list
[]

# lists can contain different data types items
[1, 2.54, 'hello']

# storing a list into a variable
myFavoriteThings = ['to study', 'to program', 'to improve', 'play games']

# accessing items through the index. indexes must be integer values
myFavoriteThings[0]     # evaluates to 'to study'
myFavoriteThings[1]     # evaluates to 'to program'
myFavoriteThings[2]     # evaluates to 'to improve'
myFavoriteThings[3]     # evaluates to 'play games'

# this line throwns an IndexError because you tried to access an index that does not exist
myFavoriteThings[4]

# can use negative indexes to access items in reverse order
myFavoriteThings[-1]     # evaluates to 'play games'
myFavoriteThings[-2]     # evaluates to 'to improve'


```

Lists can contain other lists.
```python
biDimensional = [['first', 'second', 'third'], [1, 2, 3]]

# accessing the first list
biDimensional[0]        # ['first', 'second', 'third']

# acessing the second list
biDimensional[0]        # [1, 2, 3]

# accessing items in the first list
biDimensional[0][0]     # ['first']
biDimensional[0][1]     # ['second']
biDimensional[0][2]     # ['third']

# accessing items in the second list
biDimensional[1][0]     # [1]
biDimensional[1][1]     # [2]
biDimensional[1][2]     # [3]
```

A **Slice** can get a sequence o items in a list in the form a new list. It is represented by a pair of square brackets within two indexes (the start and the end) inside, separated by a colon.
```python
items = ['item1', 'item2', 'item3', 'item4', 'item5']

# can get a part of the list with a slice
favorites = items[1:3]  # contain items from index 1 to index 2.

# slices can ommit the beginning
favorites = items[:3]   # contain items from index 0 to index 2.

# slices can ommit the end
favorites = items[1:]   # contain items from index 1 to the final index.
```

you can use the function len() to count the number of elements in a list
```python
items = ['item1', 'item2', 'item3', 'item4', 'item5']
len(items)              # 5
```

it is possible to concatenate lists and replicate them
```python
itemsA = ['element1', 'element2']
itemsB = ['something', 'anything']

# concatenate
itemsA + itemsB         # ['element1', 'element2', 'something', 'anything']

# replicate
itemsA * 3              # ['element1', 'element2', 'element1', 'element2', 'element1', 'element2']
```

Also, it is possible to remove elements with a **del** statement
```python
items = ['item1', 'item2', 'item3', 'item4', 'item5']

# removing the item at index 2
del items[2]            # ['item1', 'item2', 'item4', 'item5']
```

### Working with lists

you can add elements to a list concatenating lists:
```python
names = []

while True:
    print('type stop to stop, or type a name')
    name = input()
    if name == 'stop':
        break
    else:
        names = names + name    # adds an item

# accessing the items in the list sequentially
for name in names:
    print('hi ' + name)

# looping through the indexes and elements of a list
for i in range(len(names)):
    print('index is ' + str(i) ', item is ' + names[i])
```

Use the **in** and **not in** operators to check whether a list contains or not a certain item. These operators always evaluate to a boolean value.
```python
games = ['Megaman', 'Street Fighter', 'Resident Evil']

'Megaman' in games              # True
'Street Fighter' not in games   # False

'Blasphemous' in games          # False
'Banjo Kazooie' not in games    # True
```

### Multiple Assignment

It is possible to assign multiple variables from items in a list if the number of list items and the number of variables are the same.
```python
myData = ['Gaius', 34, 1.74]
name, age, height = myData
```

### Augmented Assignment Operators

Augmented assignment operators as a shortcut in expressions that uses variable which operates in itself.

| Expression 1 | Expression 2    |
|--------------|-----------------|
| spam += 1    | spam = spam + 1 |
| spam -= 1    | spam = spam - 1 |
| spam *= 1    | spam = spam * 1 |
| spam /= 1    | spam = spam / 1 |
| spam %= 1    | spam = spam % 1 |


