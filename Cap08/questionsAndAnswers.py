#! /usr/bin/python

import random
import os

def setDefaultDirectory():
    defaultDirectory = os.path.join(os.sep, 'home', 'gaiusfonseca', 'Projetos', 'AutomateBoringStuff', 'Cap08', 'quizz')
    
    if not os.path.exists(defaultDirectory):
        os.makedirs(defaultDirectory)

    os.chdir(defaultDirectory)

capitals = {
    "AC": "Rio Branco",
    "AM": "Manaus",
    "RR": "Boa Vista",
    "RO": "Porto Velho",
    "AP": "Macapá",
    "PA": "Belém",
    "TO": "Palmas",
    "MA": "São Luís",
    "PI": "Teresina",
    "CE": "Fortaleza",
    "RN": "Natal",
    "PB": "João Pessoa",
    "PE": "Recife",
    "AL": "Maceió",
    "SE": "Aracaju",
    "MS": "Cuiabá",
    "MT": "Campo Grande",
    "GO": "Goiânia",
    "DF": "Brasília",
    "SP": "São Paulo",
    "RJ": "Rio de Janeiro",
    "ES": "Vitória",
    "MG": "Belo Horizonte",
    "RS": "Porto Alegre",
    "SC": "Floarianópolis",
    "PR": "Curitiba",
}

setDefaultDirectory()

# cria 27 arquivos 
for quizNum in range(27):
    # TODO: Create the quiz and answer quiz files
    quizz = 'quizz_{:02d}.txt'.format(quizNum + 1)
    answer = 'answers_{:02d}.txt'.format(quizNum + 1)
    
    quizz = open(quizz, 'w')
    answer = open(answer, 'w')

    # TODO: Write out the header for the quiz
    quizz.write('teste tipo {}\n'.format(quizNum))
    quizz.write("nome do estudante: \n")
    quizz.write('data: \n')
    quizz.write('série: \n\n\n')

    # TODO: Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    # TODO: Loops through all states and make a question for each
    for questionNum in range(len(states)):
        correctAnswer = capitals.get(states[questionNum])
        
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)

        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        quizz.write('{}. Qual a capital do {}?\n'.format(questionNum + 1, states[questionNum]))

        for i in range(4):
            quizz.write('\t{}. {}\n'.format('ABCD'[i], answerOptions[i]))
        quizz.write('\n')

        answer.write('{}. {}\n'.format(questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

    quizz.close()
    answer.close()