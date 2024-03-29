#! /usr/bin/python
# madLibs - substitui tokens específicos em uma frase.

import os

# solicita as entradas dos usarios
def getUserInput():
    prompt = 'Informe um {}:'
    inputs = []

    print(prompt.format('adjetivo'))
    inputs.append(input())

    print(prompt.format('substantivo'))
    inputs.append(input())

    print(prompt.format('verbo'))
    inputs.append(input())

    return inputs

# pega  amensagem contida no arquivo de entrada
def getMessage():
    filePath = os.path.join(os.getcwd(), 'Cap08', 'madLibsInput.txt')
    file = open(filePath)
    message = file.read()
    file.close()
    print('lendo do arquivo: {}'.format(message))
    return message

# substitui os tokens do arquivo pelos tokens fornecidos
def replaceTokens(message, values):
    tokens = ['ADJETIVO', 'SUBSTANTIVO', 'VERBO']

    for i in range(len(tokens)):
        message = message.replace(tokens[i], values[i])
    
    print('mensagem substituida: {}'.format(message))
    return message

# escreve a mensagem final no arquivo de saída
def writeToFile(message):
    filePath = os.path.join(os.getcwd(), 'Cap08', 'madLibsOutput.txt')
    file = open(filePath, 'w')
    file.write(message)
    print('mesagem escrita no arquivo destino: {}'.format(message))
    file.close()

inputs = getUserInput()
message = getMessage()
message = replaceTokens(message, inputs)
writeToFile(message)