#alguns projetos feitos em sala
import datetime
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
#Aula 4
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
    x = int(input("Digite o ano de nascimento\n"))
    d = int(input("Digite o dia do nascimento\n"))
    m = int(input("Digite o Mês de nascimento\n"))
    y = datetime.datetime.now()
    if d <= y.day:
        if m <= y.month:
            z = y.year-x
        else:
            z = (y.year-x)-1
    else:
            z = (y.year-x)-1

    print("A pessoa que nasceu em",x,"Esta em",y.year,"com",z,"Anos")
    if z>=16:
        print("A pessoa pode votar em",y.year,"pois ela tem",z,"anos")
    else:
        print("A pessoa não pode votar pois em",y.year,"ela tem",z,"anos")
    if z>=18:
        print("A pessoa pode tirar CNH em",y.year,"pois ela tem",z,"anos")
    else:
        print("A pessoa não pode tirar CNH pois em",y.year,"ela tem",z,"anos")

idade()