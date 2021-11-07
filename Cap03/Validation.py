value = 0
while value != -1:
    try:
        value = int(input())
    except ValueError:
        print('Erro: era esperado um valor inteiro.')