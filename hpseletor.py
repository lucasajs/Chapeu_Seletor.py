from random import choice
from time import sleep
print(f'{" CHAPÉU SELETOR HOGWARTS ":=^50}'), sleep(0.25)
print('Olá, seja bem vindo(a) a Hogwarts! '), sleep(1)
nome= str(input('Diga o seu nome para o chapéu seletor decidir qual será a sua casa: '))
sleep(1)
casa= ['Corvinal', 'Grifinória', 'Lufa-lufa', 'Sonserina']
chapéu= choice(casa)
print('um instante, o chapéu seletor está decidindo...'),sleep(1)
print('...'),sleep(1)
if chapéu in casa[0]:
    print('\033[1:34m...'), sleep(1)
    print('~='*20)
    print(f'{"CORVINAL!":^40}')
    print()
    print(f'seja bem vindo(a) a Corvinal, {nome}!','''
As principais caracteristicas de um aluno da
Corvinal são a inteligencia, perspicácia  e um 
alto poder de sociabilização! 
''' )
elif chapéu in casa[1]:
    print('\033[1:31m...'), sleep(1)
    print('~=' * 20)
    print(f'{"GRIFINÓRIA!":^40}')
    print()
    print(f'seja bem vindo(a) a Grifinória, {nome}!','''
As principais caracteristicas de um aluno da
Grifinória são: lealdade, coragem, liderança e bravura!''')
elif chapéu in casa[2]:
    print('\033[1:33m...'), sleep(1)
    print('~=' * 20)
    print(f'{"LUFA-LUFA!":^40}')
    print()
    print(f'seja bem vindo(a) a Lufa-lufa, {nome}!','''
As principais caracteristicas de um aluno da
Lufa-lufa são o esforço, a paciência e a justiça!
''')
elif chapéu in casa[3]:
    print('\033[1:32m...'), sleep(1)
    print('~=' * 20)
    print(f'{"SONSERINA!":^40}')
    print()
    print(f'seja bem vindo(a) a Sonserina, {nome}!','''
As principais caracteristicas de um aluno da
Sonserina são a ambição e a determinação!
''')



