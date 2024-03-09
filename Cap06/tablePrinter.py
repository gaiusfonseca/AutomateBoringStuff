#! /usr/bin/python
# tablePrinter.py - prints an a square bidimensional array as a table

# given a list of lists, prints a right justified table
def printTable(listOfLists):
    rows = len(listOfLists[0])
    collumns = len(listOfLists)

    for row in range(rows):
        for collumn in range(collumns):
            width = getWidth(listOfLists[collumn])
            print(listOfLists[collumn][row].rjust(width), end = ' ')
        print()

# given a list, gets the maximun width
def getWidth(list):
    width = 0
    for i in range(len(list)):
        if width < len(list[i]):
            width = len(list[i])
    return width

tableData = [
    ['apples', 'oranges', 'cherries', 'bananas'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
    ]

printTable(tableData)