def parametro(inicio, final, passo):
    print(f'Contagem de {inicio} até {final} ao passo {passo}:')
    for i in range(inicio, final, passo):
        print(i,'\t', end='')
parametro(1, 10, 1)
parametro(10, 0, 2)
print('Contagem Personalizada:')
inicio = int(input('Insira o número de início:'))
final = int(input('Insira o número final:'))
passo = int(input('Insira o número de contagem de cada sequência:'))
parametro(inicio, final, passo)