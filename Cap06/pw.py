#! /usr/bin/python

# this program is supposed to be a password manager, once an account name is passed as an argument it copies the password to the clipboard
import sys
import pyperclip

passwords = {
    'email': 'myEmailPassword',
    'blog': 'mySecret',
    'luggage': '12345'
}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    print('finishing the program')
    sys.exit(1)

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords.get(account))
    print('password for ' + account + ' copied to the clipboard.')
else:
    print("there is no account name named '" + account + "'.")