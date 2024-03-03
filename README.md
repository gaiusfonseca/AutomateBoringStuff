# AutomateBoringStuff
Exercícios de programação do livro "Automate the Boring Stuff"

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




