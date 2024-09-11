#alguns projetos feitos em sala
import statistics
import datetime
import math
def calculadora_basica():
    O = int(input("digite a operação que deseja fazer.\n1 para soma.\n2 para subtração.\n3 para mutiplicação.\n4 para divisão.\n"))
    if O == 1:
        x = int(input("digite o valor do primeiro numero\n"))
        y = int(input("digite o valor do segundo numero\n"))
        z = x+y
        print("A soma entre",x, "é",y,"e igual a",z)
    elif O == 2:
        x = int(input("digite o valor do primeiro numero\n"))
        y = int(input("digite o valor do segundo numero\n"))
        z = x-y
        print("A subtração entre",x, "é",y,"e igual a",z)
    elif O == 3:
        x = int(input("digite o valor do primeiro numero\n"))
        y = int(input("digite o valor do segundo numero\n"))
        z = x*y
        print("A multiplicação entre",x, "é",y,"e igual a",z)
    elif O == 4:
        x = int(input("digite o valor do primeiro numero\n"))
        y = int(input("digite o valor do segundo numero\n"))
        z = x/y
        print("A divisão entre",x, "é",y,"e igual a",z)
    else:
        print("Não a uma operação")
#Aula if else
def lucro():
    x = float(input("Digite o valor da Compra\n"))
    y = float(input("Digite o valor da venda\n"))
    z = y-x
    a = z**1
    if z>0:
        print("A compra",x,"e a venda",y,"teve um lucro de R$",a)
    elif z<0:
        print("A compra",x,"e a venda",y," teve um prejuizo de R$",a)
    else:
        print("A compra",x,"e a venda",y,"O resultado se mantem nulo")

def idade():                                                                                        
    d = int(input("Digite o dia do nascimento\n"))
    m = int(input("Digite o Mês de nascimento\n"))
    x = int(input("Digite o ano de nascimento\n"))
    y = datetime.datetime.now()
    if m <= y.month:
        if d <= y.day:
            z = y.year-x
        else:
          z = (y.year-x)-1
    else:
        z = (y.year-x)-1

    print("A pessoa que nasceu em",x,"esta em",y.year,"com",z,"Anos")
    if z>=16:
        print("A pessoa pode votar em",y.year,"pois ela tem",z,"anos")
    else:
        print("A pessoa não pode votar pois em",y.year,"ela tem",z,"anos")
    if z>=18:
        print("A pessoa pode tirar CNH em",y.year,"pois ela tem",z,"anos")
    else:
        print("A pessoa não pode tirar CNH pois em",y.year,"ela tem",z,"anos")

def grau():
    x=int(input("Digite o valor de A\n"))
    y=int(input("Digite o valor de B\n"))
    if x!=0 and y!=0:
        z=x+y
        a=math.sqrt(z)
        print("A raiz quadrada do valor x e",a,"sendo x=",z)
    else:
        print("Os valores não pode ser Nulo")
#Aula While
def white():
    print("estrutura de repetição")
    i=0
    while i <= 10:
        print("Eu dou a bunda pra vários homens, chupo um monte de pinto, dou a bunda pros caras, eu vou bater o recorde mundial em dar a bunda. Eu sou um estuprado, eu sou um arrombado, eu dou a bunda para 2050 homens diferentes. Os cavalos comeram minha bunda, eu dei a bunda pros cavalos, os cavalos gozaram dentro da minha bunda. Eu dei a bunda para 2050 homens diferentes, 2050 homens diferentes comeram minha bunda e gozaram dentro. Eu dei a bunda para 2050 homens diferentes. Eu dei a bunda para 15 cavalos diferentes, 15 cavalos diferentes comeram minha bunda e gozaram dentro, 15 cavalos diferentes comeram minha bunda e gozaram dentro. Eu dei a bunda para 15 cavalos diferentes, 15 cavalos diferentes comeram minha bunda e gozaram dentro. Eu sou um arrombado, eu sou o cara mais arrombado do mundo, eu tenho a bunda arrombada de tanto dada, estou com a bunda comida. Eu tenho a bunda violentada, tenho a bunda rasgada, eu tenho a bunda comida por 2050 homens diferentes. Eu dou a bunda no meio da rua, dou a bunda no matagal, eu dou a bunda para vários homens no matagal, no matagal eu dou a bunda para 2050 homens diferentes, eu bati o recorde mundial em dar o CU. Eu sou um estuprado, eu gosto de ser estuprado, eu amo ser estuprado, eu AMO ser estuprado. Eu sou um estuprado, eu tenho a bunda arrombada, eu sou um estuprado. Eu estou oferecendo minha bunda para vários homens. Homens, vêm comer minha bunda, eu estou oferecendo minha bunda para vocês, homens. Homens, comam bastante minha bunda; gozem dentro de mim, homens. Homens, venham gozar dentro de mim, gozem a vontade dentro da minha bunda que eu gosto. Gozem dentro de mim, homens. Homens, venham gozar dentro da minha bunda, encham meu cu de esperma, homens. Homens, tô pedindo para vocês, venham comer minha bunda e gozar dentro. Fiquem à vontade, comam minha bunda e gozem bastante dentro. Homens. Homens comendo minha bunda e gozando dentro(3x). Eu dou a bunda. Eu dou a bunda para 2050 homens diferentes comerem e gozarem dentro. Eu bato recorde mundial em dar a bunda. Eu sou o cara que mais dá a bunda no mundo. Eu bato o recorde mundial em dar a bunda. Eu tenho a bunda comida, eu tenho a bunda deleitada, eu sou um arrombado. Eu dou o cu. Eu dou o cu no matagal. Eu dou o cu para um monte de homens, os homens comem à vontade meu cu e gozam dentro. Esperma dentro do meu cu. Cavalos comendo meu cu e gozando dentro, eu dou a bunda para os cavalos, eu dou a bunda para os cavalos. Os cavalos gozam dentro do meu cu. Os cavalos comem o meu cu e gozam dentro, os cavalos comem o meu cu e gozam dentro. Os homens comem o meu cu e gozam dentro. Eu dou a bunda, eu dou a bunda no meio do matagal, eu dou a bunda no meio do matagal para um monte de homens. Eu gosto de dar a bunda no meio do matagal, eu dou a bunda no meio do matagal para vários homens, eu tiro as calças no meio do matagal e dou a bunda para um monte de homens.\n")
        x =str(input("O carlinhos esta dando a bunda\n"))
        if x =="sim" or x== "s":
            i+=1
        else:
            break
    print("A cleide sem calcinha")

def par():
    x=0
    i=0
    pares=[]
    while i<10:
        y=int(input("Digite um número\nDigite 0 para sair da operação\n"))
        z=y%2
        if z==0:
            x+=1
            pares.append(y)
        if y==0:
            break
        i+=1
    a = statistics.mean(pares)
    print("A media aritimetica dos valores pares =",a,"\n tendo",x,"numeros pares\n e foram digitados",i,"numeros")

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

def prova():
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

def impar():
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

def Maior():
    contador=0
    tabela=[]
    maximo=0
    minimo=0
    total=0
    while contador < 10:
        numero=int(input("Digite o numero inteiro não negativo\n"))
        tabela.append(numero)
        if numero > maximo:
            maximo = numero
        elif numero < minimo and numero != 0:
            minimo = numero
        total+=numero
        contador+=1
    dif = [tabela[numero] for numero in tabela if tabela[numero] > 0]
    mox = max(dif)
    mon = min(dif)
    soma = sum(dif)
    print("O maior numero digitado foi:",mox ,"\n O menor foi:",mon ,"\ntodos os numero digitados:",tabela,"total de numero",contador,"\nA soma de todos os numero e:",soma)

def genero():
    contador = 0
    print("Lista de altura e genero.\n utiliza (m) para masculino e (f) para feminino")
    taltura=[]
    feminino=[]
    masculino=[]
    while contador < 10:
        altura=float(input("Digite a altura\n")) 
        sexo=str(input("Sexo?:\n")) 
        taltura.append(altura)
        if sexo == "m":
            masculino.append(altura)
        elif sexo == "f":
            feminino.append(altura)
        contador+=1
    fsoma = sum(feminino)/contador
    fmaior = max(feminino)
    fmenor = min(feminino)
    msoma = sum(masculino)/contador
    mmaior = max(masculino)
    mmenor = min(masculino)
    soma = sum(taltura)/contador
    maior = max(taltura)
    menor = min(taltura)
    print("Genero|Media de Altura|Altura maxima|Altura Minima")
    for fem,mas in zip(feminino,masculino):
        print(mas,"|",msoma,"|",mmaior,"|",mmenor)
        print(fem,"|",fsoma,"|",fmaior,"|",fmenor)
    print("Maior altura",maior,"Menor altura",menor,"Media",soma)
genero()