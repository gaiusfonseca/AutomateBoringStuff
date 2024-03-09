#! /usr/bin/python
# bulletPointAdder.py - adds bullet point to the beginning of each line.

import pyperclip

# simulates copying a list
baseString = '\n'.join(['List of animals', 'List of aquarium life',  'List of biologists', 'List of cultivars'])
pyperclip.copy(baseString)

# paste the content to a variable and converts the string to a list of strings
items = pyperclip.paste()
items = items.split('\n')

# adds the bullet points
for i in range(len(items)):
    items[i] = '* ' + items[i]

# copies the modified list to the clipboard
pyperclip.copy('\n'.join(items))

# shows the modified list
print('showing the modified list: ')
for item in items:
    print(item)
