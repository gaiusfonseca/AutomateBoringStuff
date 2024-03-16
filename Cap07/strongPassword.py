#! /usr/bin/python
import re

def isStrogPassword(password):
    
    upperCasePattern = r'.*[A-Z]|[A-Z].*'
    upperCaseRegex = re.compile(upperCasePattern)

    lowerCasePattern = r'.*[a-z]|[a-z].*'
    lowerCaseRegex = re.compile(lowerCasePattern)

    numbersPattern = r'.*\d|\d.*'
    numbersRegex = re.compile(numbersPattern)
    
    if len(password) < 8:
        print('fraco: contém menos de 8 caracteres')
        return False
    elif upperCaseRegex.match(password) == None:
        print('fraco: não contém letras maiúsculas')
        return False
    elif lowerCaseRegex.match(password) == None:
        print('fraco: não contém letras minúsculas')
        return False
    elif numbersRegex.match(password) == None:
        print('fraco: não contém números') 
        return False
    
    return True

password = input()

if isStrogPassword(password):
    print('{0} é um password forte!'.format(password))