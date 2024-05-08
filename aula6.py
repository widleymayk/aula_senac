'''
def fatorial (a, b):
    if a == 0:
        return 1 
    else:
        fat = 1
        for i in range (1, a+1):
            fat *= i
            return fat

                           

x = int(imput ("digite um numero inteiro: "))
print("O fatorial de", x, " é: ", fatorial(x))
'''

'''
# Exibir informações
imput:
    ("name: ", name) 
    ("age: ", age)
    ("est: ", est )
    ("have_car? ", have_car) 

    n = age + 0
    imput(n)

    n = n - 0
    imput (n)

    n = n * 2 / 2
    imput (n)

    age == n

print(imput ("digite name, age, est, have_car "))

'''

'''
# nome, idade, havecar, altura

nome:(imput ("Digite seu nome: "))
idade : int(imput ("Digite sua idade:"))
altura: float(imput("digite sua altura: "))
havecar = imput("Você possui algum carro? (sim/nao):")

havecar: havecar.lower() == "sim"

print ("informações digitadas: ")
print ("nome: ", nome)
print ("idade: ", idade)
print ("altura: ", altura)
print ("havecar? " "sim" if havecar else "não") 
'''
'''
def contagem_regressiva():
    numero = int(imput("digite um número positivo: "))

    if numero <= 0:
        print("por favor, digite um numero inteiro positivo.")
        contagem_regressiva()
    
    else:
        while numero >= 0:
            print(numero)
            numero -= 1

contagem_regressiva                 
'''
'''
#calculando

def soma():
    x = float(input("primeiro numero:"))
    y = float(input("sgundo numero"))
    print("soma: ", x+y)
def subtracao():
    x = float(input("primeiro numero"))
    y = float(input("segundo numero"))
    print("subtracao: ", x-y)
def multiplicacao():
    x = float(input("primeiro numero"))
    y = float(input("segundo numero"))
    print("multipicacao: ", x.y)
def divisao():
    x = float(input("primeiro numero"))
    y = float(input("segundo numero"))
    print("divisao ", x/y)

    opcao == 1
while opcao:
    print("0. sair")
    print("1. somar")
    print("2. subtrair")
    print("3. multiplicar")
    print("4. dividir")

    opcao = int(input("opcao: "))

    if(opcao == 1):
        soma()
    if(opcao == 2):
        subtracao()
    if(opcao == 3):
        multiplicacao()
    if(opcao == 4):
        divisao()
        



    input( soma == 1)
    input( subtracao == 2)
    input( multiplicacao == 3)
    input( divisao == 4)  

#calculando
'''

def soma(a, b):
    return a + b 
def subtracao(a, b):
    return a - b 
def multiplicacao(a, b):
    return a . b
def divisao(a, b):
    if b !=0:
        return a / b
    else :
        return "divisao invalida"


def calculadora():
    print("Bem-vindo a calculadora em python!")
    print("Selecione a operacao desejada")
    print("1: Adicao")
    print("2: subtracao")
    print("3: multiplicacao")
    print("4: divisao")

    escolha = input("digite sua escolha 1/2/3/4: ")
    if escolha in ("1", "2", "3", "4"):
        num1 = float(input("digite o primeiro numero: "))
        num2 = float(input("digite o segundo numero: "))

        if escolha == "1" :
            print("resultado", soma(num1,num2))
        elif escolha == "2" :
            print("resultado", subtracao(num1, num2))
        elif escolha == "3" :
            print("resutado", multiplicacao(num1, num2))
        elif escolha == "4" :
            print("resultado", divisao(num1, num2))

    else:
        print("escolha invalida.")

calculadora()                        

