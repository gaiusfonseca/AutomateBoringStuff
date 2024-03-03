# AutomateBoringStuff
Exercícios de programação do livro "Automate the Boring Stuff"

<h1>Primitive Data Types</h1>
primitive data types: int, float, string, boolean (True and False)

aritmethic operators: always evaluate to a numeric value
** exponent
* multiplication
/ division
// intrger division
% module
+ sum
- difference

string operators: always evaluate to a string
+ concatenation
* repetition
obs: can not apply these operators directly to a number, must convert the number to a string first

comparison operators: always evaluate to a boolean value. Used mostly to compare values.
== equals (any data type)
!= not equals (any data type)
> greater than
< less than
>= greater than or equal to
<= less than or equal to

boolean operators: always evaluate to a boolean value
not - operates over one boolean value and evaluates to the opposite of this value.
and - is true only if both values are true
or - is true if at least one of the values are true

Attention:
== is different of =
== equa to
= assignment

Flow control statement = condition + clause
condition: an expression that evaluates to a boolean value
clause: a block of code that executes, according the statement used, if the condition is true

statements:
if - executes a clause if it's true or another clause if it's false

if age > 18:
    print('you are responsible for yourself')
elif < 18:
    print('your parents are responsible for you')
else:
    print('you are responsible for yourself from now on')

while - repeats the clause while the condition is true

while (condition):
    clasue

break - jumps out of the block. Usually used to jump out of a loop.

continue - jumps back to the start of the loop. skips the following code.

for - while a specific number of times was not reached (condition), keeps executing the clause.

for x in range(y):
    clasue

range(start, stop, step)
start - indicates with which value the count will start
stop - indicates to which value the count will stop. The clause will not be executed when the stopping value is reached
stepstep - indicates how much the value will be increased at each interaction

range(start, stop) - step = 1.

range(stop) - start = 0, step = 1.

import moduleName[, anotherModules]
form moduleName import functionName

import random
for i in range(5):
    print(random.randint(1, 10))

from random import * - can be used to call the functions without the module name, but should be avoided

sys.exit() - terminates a program. must be imported before use.

CHAPTER 3 - FUNCTIONS

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

