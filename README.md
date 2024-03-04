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
> When checking for multiple conditions it is very important to consider the order in whcih the checks will be done.

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
while age < 20:                     //this is the condition
    //this block is a clause
    print('another year passes')
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

### continue
continue - jumps back to the start of the loop. skips the following code.

### for
for - while a specific number of times was not reached (condition), keeps executing the clause.

for x in range(y):
    clasue

range(start, stop, step)
start - indicates with which value the count will start
stop - indicates to which value the count will stop. The clause will not be executed when the stopping value is reached
stepstep - indicates how much the value will be increased at each interaction

range(start, stop) - step = 1.

range(stop) - start = 0, step = 1.

### importing modules

import moduleName[, anotherModules]
form moduleName import functionName

import random
for i in range(5):
    print(random.randint(1, 10))

from random import * - can be used to call the functions without the module name, but should be avoided

sys.exit() - terminates a program. must be imported before use.

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