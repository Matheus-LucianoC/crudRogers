import json
import random
import os

with open('nomesSAVE.json', 'r', encoding='utf-8') as N:
    data = json.load(N)


nomes = data["nomesSAVE"]

with open('senhasSAVE.json', 'r', encoding='utf-8') as N:
    data = json.load(N)


senhas = data["senhasSAVE"]

with open('produtosSAVE.json', 'r', encoding='utf-8') as I:
    data = json.load(I)


produtos = data["produtosSAVE"]

with open('precosSAVE.json', 'r', encoding='utf-8') as P:
    data = json.load(P)


precos = data["precosSAVE"]

with open('saldoSAVE.json', 'r', encoding='utf-8') as P:
    data = json.load(P)


saldo = data["saldoSAVE"]

produtos = []
nomes = []
senhas = []
saldo = []

def sistema_base(nomes, senhas):
 while True:
    print("Bem vindo ao Roger's, oque deseja fazer?")
    print("Insira 1 para criar uma conta")
    print("Insira 2 para listar todas as contas")
    print("Insira 3 para consultar os dados da sua conta") 
    print("Insira 4 para comprar produtos")
    print("Insira 5 para DELETAR a conta") 
    print("Insira 6 para alterar os valores da conta (senha e nome)") 
    print("Insira 7 para APOSTAR!!") 
    print("Insira 8 para sair")
    escolhasistemabase =  input("Escreva a opção desejada: ")
    escolhasistemabase = int(escolhasistemabase)
    if escolhasistemabase == 1:
       criarconta(nomes, senhas)
    elif escolhasistemabase ==2:
       listarcontas(nomes)
    elif escolhasistemabase ==3:
       consultardados(nomes,senhas,saldo) 
    elif escolhasistemabase == 4:
       comprar(nomes,saldo)
    elif escolhasistemabase == 5:
       deletarconta(nomes,senhas,saldo)
    elif escolhasistemabase == 6:
       alterarconta(nomes,senhas)
    elif escolhasistemabase == 7:
       apostas(nomes,saldo)
    elif escolhasistemabase == 8:
       break
    
def criarconta(nomes,senhas):
    global nome_contacriar 
    global senha_contacriar
    nome_contacriar = input("Qual será o nome da sua conta? (você irá começar com 1000 reais!!) ")
    nomes.append(nome_contacriar)
    senha_contacriar = input("Qual será a senha da sua conta? ")
    senhas.append(senha_contacriar)
    saldo.append(1000)
    print("Sua conta "+nome_contacriar+ " foi criada com sucesso!\n")
    
def listarcontas(nomes):
    for i in range(len(nomes)):
        print(nomes[i])
    print("")

def consultardados(nomes,senhas,saldo):
    acessar_conta = input("Digite o nome da sua conta: ")
    if acessar_conta in nomes:
        index = nomes.index(acessar_conta)  
        senha = input("Digite a senha da sua conta: ")
        if senhas[index] == senha:  
            print("Dados da sua conta: ")
            print("Nome: " + acessar_conta)
            print("Senha: " + senha)  
            print("Saldo: " + str(saldo[index]) + " R$")
            print("")
        else:
            print("ERRO!! A senha está errada!")
            print("")
    else:
        print("ERRO!! O nome da conta não foi encontrado!")
        print("")
    
def comprar(nomes,saldo):
    print("FAZER AINDA!!!")

def deletarconta(nomes,senhas,saldo):
    acessar_conta = input("Digite o nome da sua conta: ")
    if acessar_conta in nomes:
        index = nomes.index(acessar_conta)  
        senha = input("Digite a senha da sua conta: ")
        if senhas[index] == senha:  
            areyousure = input("Tem certeza? Digite 1 para DELETAR e 0 para cancelar: ")
            areyousure = int(areyousure)
            if areyousure == 1:
                nomes.pop(index)
                senhas.pop(index)
                saldo.pop(index)
                print("Conta deletada com sucesso!")
                print("")
            elif areyousure == 0:
                print("A conta não foi deletada!")
                print("")
            else:
                print("Opção inválida! A conta não foi deletada.")
                print("")
        else:
            print("ERRO!! A senha está errada!")
            print("")
    else:
        print("ERRO!! O nome da conta não foi encontrado!") 
        print("")

def alterarconta(nomes,senhas):
    acessar_conta = input("Digite o nome da sua conta: ") 
    if acessar_conta in nomes:
        acessarcontabool = 1
        index = nomes.index(acessar_conta)  
    else:
        print("Valor inválido!")
        print("")
        return  
    senha = input("Digite a senha da sua conta: ")
    if senhas[index] == senha:  
        senhabool = 1
    else:
        print("Valor inválido!")
        print("")
        return  
    novo_nome = input("Qual será o nome da sua conta? ")
    nova_senha = input("Qual será a senha da sua conta? ")

    nomes[index] = novo_nome
    senhas[index] = nova_senha
    print("Conta atualizada com sucesso!")

def apostas(nomes,saldo):
    print("FAZER AINDA!!!")
sistema_base(nomes, senhas)
