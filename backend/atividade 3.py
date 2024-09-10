import math
import statistics
def real():
    contador = 0
    soma = 0
    vinte = 0
    while contador <= 10:
        numero=float(input("Digite um numero real\nDigite 00 para parar\n"))
        soma+= numero
        if numero > 20:
            vinte += 1
        if numero == 00:
            break
        contador += 1
    media=soma/contador
    print("Foram digitados",contador,"numero\nA soma de todos os valores:",soma,"\nA media aritimetica:",media,"\nNumeros que são maiores que 20:",vinte)

def notas():
    contador=1
    aprovado=0
    reprovado=0
    alunos=int(input("Digite o numero de alunos na sala\n"))
    while contador<=alunos:
        nota=float(input("Digite o a nota do aluno\n"))
        if nota >= 5.0:
            aprovado+=1
        else:
            reprovado+=1
        contador+=1
    print("A quantidade de alunos que fizeram a prova",alunos,"\ntendo",aprovado,"Alunos aprovados\n",reprovado,"Aluno reprovado")

def mediaIP():
    par=0
    impar=0
    pares=[]
    impares=[]
    contador=0
    while contador<10:
        numero=int(input("Digite um número\nDigite 0 para sair da operação\n"))
        resultado=numero%2
        if resultado==0:
            par+=1
            pares.append(numero)
        else:
            impar+=1
            impares.append(numero)
        if numero==0:
            break
        contador+=1
    ptotal = statistics.mean(pares)
    itotal = statistics.mean(impares)
    print("A media aritimetica dos valores pares =",ptotal,"\n tendo",par,"numeros pares")
    print("A media aritimetica dos valores impares =",itotal,"\n tendo",impar,"numeros impares\n e foram digitados",contador,"numeros")