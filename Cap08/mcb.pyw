#! /usr/bin/python
# mcb.pyw - salva e carrega conteúdo para o clipboard
# uso:  python mcb.pyw save <keyword> - salva o conteúdo da clipboard como a palavra-chave
#       python mcb.pyw <keyword> - carrega o conteúdo da palavra-chave para a clipboard
#       python mcb.pyw list - lista todas as palavra-chave que foram salvas

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
arguments = sys.argv
usage = '''
# uso:  python mcb.pyw save <keyword> - salva o conteúdo da clipboard como a palavra-chave
#       python mcb.pyw <keyword> - carrega o conteúdo da palavra-chave para a clipboard
#       python mcb.pyw list - lista todas as palavra-chave que foram salvas
'''

if len(arguments) == 3 and arguments[1].lower() == 'save':      # caso tenham 3 argumentos e sintaxe correta
    keyword = arguments[2]
    content = pyperclip.paste()
    mcbShelf[keyword] = pyperclip.paste()
    message = 'conteudo copiado: {}'
    print(message.format(content))
elif len(arguments) == 2 and arguments[1].lower() == 'list':    # caso tenham 2 argumentos e o seguindo seja list
    keywords = list(mcbShelf.keys())
    for keyword in keywords:
        print('chave encontrada: {}'.format(keyword))
elif len(arguments) == 2 and arguments[1] in mcbShelf.keys():   # caso tenham 2 argumentos e o seguindo seja uma palavra-chave
    keyword = arguments[1]
    pyperclip.copy(mcbShelf[keyword])
    message = 'o conteudo da chave {} foi carregado no clipboard'
    print(message.format(keyword))
else:
    print(usage)

mcbShelf.close()