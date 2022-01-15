""" 
4. Faça um programa que imprima a tabuada do 9 (de 9*1 a 9*10) usando loops.
"""

tab = 9
for count in range(10):
    print("%d x %d = %d" % (tab, count+1, tab*(count+1)))
