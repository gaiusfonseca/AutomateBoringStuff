#! /usr/bin/python
# emcb.pyw - salva e carrega conteúdo para o clipboard
# uso:  python emcb.pyw save <keyword> - salva o conteúdo da clipboard como a palavra-chave
#       python emcb.pyw <keyword> - carrega o conteúdo da palavra-chave para a clipboard
#       python emcb.pyw list - lista todas as palavra-chave que foram salvas
#       python emcb.pyw delete <keyword> - apaga a palavra-chave e seu conteúdo
#       python emcb.pyw delete - apaga todas as plavras-chave e conteúdos

import shelve, pyperclip, sys

mcbShelf = shelve.open('emcb')
arguments = sys.argv
usage = '''
# uso:  python emcb.pyw save <keyword> - salva o conteúdo da clipboard como a palavra-chave
#       python emcb.pyw <keyword> - carrega o conteúdo da palavra-chave para a clipboard
#       python emcb.pyw list - lista todas as palavra-chave que foram salvas
#       python emcb.pyw delete <keyword> - apaga a palavra-chave e seu conteúdo
#       python emcb.pyw delete - apaga todas as plavras-chave e conteúdos
'''

if len(arguments) == 3 and arguments[1].lower() == 'save':                                              # caso tenham 3 argumentos e o segundo seja save
    keyword = arguments[2]
    content = pyperclip.paste()
    mcbShelf[keyword] = pyperclip.paste()
    message = 'conteudo copiado: {}'
    print(message.format(content))
elif len(arguments) == 2 and arguments[1].lower() == 'list':                                            # caso tenham 2 argumentos e o segundo seja list
    keywords = list(mcbShelf.keys())
    for keyword in keywords:
        print('chave encontrada: {}'.format(keyword))
elif len(arguments) == 2 and arguments[1] in mcbShelf.keys():                                           # caso tenham 2 argumentos e o segundo seja uma palavra-chave
    keyword = arguments[1]
    pyperclip.copy(mcbShelf[keyword])
    message = 'o conteudo da chave {} foi carregado no clipboard'
    print(message.format(keyword))
elif len(arguments) == 3 and arguments[1].lower() == 'delete' and arguments[2] in mcbShelf.keys():     # caso tenham 3 argumentos e o segundo seja del
    keyword = arguments[2]
    del mcbShelf[keyword]
    message = 'conteudo de {} apagado'
    print(message.format(keyword))
elif len(arguments) == 2 and arguments[1].lower() == 'delete':                                            # caso tenham 2 argumentos e o segundo seja del
    keywords = list(mcbShelf.keys())
    for keyword in keywords:
        del mcbShelf[keyword]
        message = 'conteudo de {} apagado'
        print(message.format(keyword))
else:
    print(usage)

mcbShelf.close()