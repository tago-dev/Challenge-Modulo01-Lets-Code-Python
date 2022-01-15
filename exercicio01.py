""" 
1. Faça um programa que peça um valor monetário e diminua-o em 15%. 
    Seu programa deve imprimir a mensagem “O novo valor é [valor]”.
"""

value = float(input("Digite um valor: "))
new_value = (value * 0.85)
print(f'o novo valor é: R$ {new_value:.2f}')
