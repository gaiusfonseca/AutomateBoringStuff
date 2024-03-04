# Automate Boring Stuff

## Chapter 1

### Primitive Data Types
- int
- float
- string
- boolean

### Aritmethic Operators
<!-- TODO: need to escape characters and put them in a table -->
Always evaluate to a value.
- \*\* exponent
- \* multiplication
- / division
- // integer division
- % module
- \+ sum
- \- difference

### String Operators
<!-- TODO: need to escape characters and put them in a table -->
Always evaluate to a String.
- \+ concatenation
- \* repetition
> [!IMPORTANT]
> Can not apply these operators directly to a number, must convert the number to a string first. Python does not implicity convert number to a String.

### Comparison Operators
<!-- TODO: need to escape characters and put them in a table -->
Always evaluate to a boolean.
- == equals (any data type)
- != not equals (any data type)
- \> greater than
- < less than
- \>= greater than or equal to
- <= less than or equal to

### Boolean Operators
Always evaluate to a boolean.
- not: operates over one boolean value and evaluates to the opposite of this value
- and: is true only if both values are true
- or: is true if at least one of the values are true

> [!WARNING]
> == equals to compares two values and let you know if they are equal or not, it always return a boolean value. = an assignment is used to put the value on the left into the variable at right. Do not confuse them.

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
if - may be used to decided which clause will be executed according to a condition a series of conditions. The else and elif block is optional. elif blocks may be used to check for more than one case.

minimun if:
```
if condition:
    clause
```

checking for something or else (at least one clause will be executed)
```
if conditionA:
    clauseA
else:
    clauseElse
```

checking for more than one case (one or none case is executed)
```
if conditionA:
    clauseA
elif conditionB:
    clauseB
elif conditionC:
    clauseC
```
> [!TIP]
> When checking for multiple conditions it is very important to consider the order in whcih the checks will be done.

checking for more than one case or else (at least one clause will be executed)
```
if conditionA:
    clauseA
elif conditionB:
    clauseB
elif conditionC:
    clauseC
else:
    clauseElse
```

### while
while - repeats the clause while the condition is true

while (condition):
    clasue

### break

break - jumps out of the block. Usually used to jump out of a loop.

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