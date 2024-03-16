#! /usr/bin/python

import pyperclip, re

# cria uma regex capaz de encotnrar números de telefone (padrão brasileiro)
phonePattern = r'''
(\d{2}|\(\d{2}\))?      # código de área, com um sem parênteses
[\s\-]                  # um separador
(\d?\d{4}               # um grupo de 4 ou 5 números
[\s\-]                  # um separador
\d{4})                  # um grupo de 4
'''

phoneRegex = re.compile(phonePattern, re.VERBOSE)

# cria uma regex capaz de encotnrar emails
emailPattern = r'''
[a-zA-Z0-9._%+-]+     # alias
@                     # arroba
[a-zA-Z0-9._]+        # domínio
\.[a-zA-Z]{2,4}       # extensão
'''

emailRegex = re.compile(emailPattern, re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    if groups[0] == '':
        phoneNumber = groups[1]
    else:
        phoneNumber = ' '.join([groups[0], groups[1]])
    matches.append(phoneNumber)

for groups in emailRegex.findall(text):
    matches.append(groups)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('content copied to the clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')