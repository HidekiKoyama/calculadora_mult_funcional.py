import os
import time

print("Seja bem-vindo à minha calculadora\nAqui você poderá usar e calcular diversos tipos de operações")

#O que será possível de fazer com esta calculadora?
#Operações básicas(De forma que o sistema guarde a informação e possa ser calculado com outro número)

while True:
    escolha_geral = input(
"\n__________Escolha o tipo de calculo de deseja realizar!__________" +
"\n\nCalculo simples: Soma, divisão, Multiplicação e Subtração." +
"\n\nCalculo de converções: Quilometros em metros, Metros em Centimetros, Regra de Três, descontos em porcentagem." +
"\n\nEscolha entre as opções" +
"\n\n\n\t|Calculo Simples = simples" + 
"\n\t|Calculo de Converção = conversão" +
"\n\n\nQual destas aplicações você deseja ultilizar? ")

#-------------------Listas---------------------
    conversao = {"conversao", "Conversão", "conversão","c", "C"}
    simplee = {"simples", "Simples", "S"}
    nao_para_td = {"S","s","sim","Sim"}
#---------Opção que foi escolhida é válida?----------------

    if escolha_geral not in conversao or simplee:
        print("Tem certeza que escolheu uma opção viável? ")

    if escolha_geral in conversao or simplee:
        break

#Transiçao
os.system('cls') or None
time.sleep(1)

if escolha_geral in simplee:
    #Transiçao
    os.system('cls') or None
    print(" \t\t\t\tCarregando")
    time.sleep(1)
    os.system("cls") or None

    while True:
        op_S_numero1 = int(input("Primero número: "))
        op_S_operador = input("Operador: ")
        op_S_numero2 = int(input("Segundo número: "))

        time.sleep(1)
        print ("Calculando")

        if op_S_operador == "/":
            print(op_S_numero1 / op_S_numero2)
        elif op_S_operador == "-":
            print(op_S_numero1 - op_S_numero2)
        elif op_S_operador == "+":
            print(op_S_numero1 + op_S_numero2)
        elif op_S_operador == "*":
            print(op_S_numero1 * op_S_numero2)

        if input("Deseja finalizar programa, sim ou não? ") in nao_para_td:
            break

#-----------Escolha de Conversores e Ferramentas--------------------------
if escolha_geral in conversao: 
    #Transiçao
    os.system('cls') or None
    print(" \t\t\t\tCarregando")
    time.sleep(1)
    os.system("cls") or None

    print("-----------(Bem-vindo ao ambiente Mais Ferramentas)------------")
    ferraments = input ("Escolha uma das opções abaixo:"+
    "\n[1] -- |Conversor de metros em centimeetros"+
    "\n[2] -- |Descobrir Watts com Amperes e Volts"+
    "\n[3] -- |Regra de Três"+
    "\n[4] -- |Calculo com salário e seus descontos(Em breve)"+
    "\n\nDigite aqui sua opção: ")

#:::::::::::::::Conversor de Metros em cm:::::::::::::::::
if ferraments == "1":
    #Transiçao
    os.system('cls') or None
    print(" \t\t\t\tCarregando")
    time.sleep(1)
    os.system("cls") or None

    while True:
        if ferraments == "1":
            mtros = int(input("Digite em metros: "))
            centi_convert = mtros * 100
            print (mtros, " em centimetros temos ", centi_convert,"cm")

        if input("Deseja finalizar programa, sim ou não? ") in nao_para_td:
            break

#::::::::::::::::::::Conversor de Watts:::::::::::::::::::::
if ferraments == "2":
    #Transiçao
    os.system('cls') or None
    print(" \t\t\t\tCarregando")
    time.sleep(1)
    os.system("cls") or None

    while True:
        if ferraments == "2":
            valor_em_amperes = int(input("\nDigite:\nAmperes = "))
            valor_em_volts = int(input("Volts = "))

#                       Animaçãozinha básica                       

            time.sleep(1)
            print("Calculando")
    
            watts = valor_em_volts * valor_em_amperes
            print("Em Watts os valor fica", watts, "W")
            if input("Deseja finalizar programa, sim ou não? ") in nao_para_td:
                break

#:::::::::::::::::::Regra de Três::::::::::::::::
if ferraments == "3":
    #Transiçao
    os.system('cls') or None
    print(" \t\t\t\tCarregando")
    time.sleep(1)
    os.system("cls") or None

    print("\t\t\tAmbiente Regra de Três")
    while True:
        print("Abaixo um exemplo de como nossa Caculadora de Regra de Três funciona\n"+
        "\n[Número 1] estará para [Número 2]"+
        "\n[Número 3] estará para [Seu resultado]")
        regra3_num1 = int(input("Escolha seu [Número 1]"))
        regra3_num2 = int(input("Escolha seu [Número 2]"))
        regra3_num3 = int(input("Escolha seu [Número 3]"))

        calcu_regra3_result = (regra3_num3 * regra3_num2) / regra3_num1
        print("Assim como", regra3_num1, "está para", regra3_num2, "\n", regra3_num3, "está para", calcu_regra3_result )

        if input("Deseja finalizar programa, sim ou não? ") in nao_para_td:
            break

# Descontos do Salário, calculo liquido

if ferraments == '4':
  print("Recurso disponível em breve")
  input()
