#! /usr/bin/python

import re

def strip(text, chars=None):

    spacePattern = r'^\s*(.*)\s*$'
    spaceRegex = re.compile(spacePattern)

    if chars == None:
        text = spaceRegex.match(text).group(1)

    if chars != None:
        replaceRegex = re.compile(chars)
        text = replaceRegex.sub('', text)

    return text

sampleString = '   batman   '

print('calling strip with no arguments: ')
print(strip(sampleString))

print('calling strip with \'man\': ')
print(strip(sampleString, 'man'))