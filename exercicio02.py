"""

2. Faça um programa que leia a validade das informações:

    a. Idade: entre 0 e 150;
    b. Salário: maior que 0;
    c. Sexo: M, F ou Outro;

O programa deve imprimir uma mensagem de erro para cada informação
inválida.

"""
idade = int(input("Qual a sua idade? "))

if(idade < 0 and idade > 150):
    print('valor errado!')

# /===============================================\

salario = int(input("Qual o seu Sálario? "))

if(salario < 0):
    print('valor errado')

# /===============================================\

sexo = str(input("Qual é o seu sexo? (M, F ou OUTRO) ")).upper()
print(sexo)
if(sexo != "M" and sexo != "F" and sexo != "OUTRO"):
    print('sexo errado.')
