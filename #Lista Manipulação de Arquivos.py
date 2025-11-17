#Lista Manipulação de Arquivos

#1 # Cria e escreve a saudação no arquivo
with open("saudacao.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Olá, mundo da programação!")



 #2 

itens = ["Arroz", "Leite", "Banana"]

# Cria e escreve cada item em uma nova linha
with open("compras.txt", "w", encoding="utf-8") as arquivo:
    for item in itens:
        arquivo.write(item + "\n")   



#3 
try:
    with open("compras.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo de compras.txt:")
        print(conteudo)
except FileNotFoundError:
    print("O arquivo compras.txt não foi encontrado.")




#4
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

with open("perfil.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(nome + "\n")
    arquivo.write(idade + "\n")

print("Informações salvas em perfil.txt.")


#5
try:
    with open("perfil.txt", "r", encoding="utf-8") as arquivo:
        nome = arquivo.readline().strip()
        idade = arquivo.readline().strip()
    print(f"Seu nome é {nome} e você tem {idade} anos.")
except FileNotFoundError:
    print("O arquivo perfil.txt não foi encontrado.")



#6
lembrete = input("Digite um novo lembrete: ")

with open("lembretes.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(lembrete + "\n")

print("Lembrete adicionado com sucesso.")


#7 
from datetime import datetime

entrada = input("Escreva sua entrada de diário: ")
data = datetime.now().strftime("%d/%m/%Y %H:%M")

with open("diario.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"[{data}] {entrada}\n")

print("entrada de diário registrada.")



#8
with open('lembretes.txt', 'r') as arquivo:
    primeira_linha = arquivo.readline()
    print(primeira_linha.strip())
 


 #9
 with open('diario.txt', 'r') as arquivo:
    entradas = arquivo.readlines()
    lista_diario = [linha.strip() for linha in entradas]
    print(lista_diario)



#10
with open('compras.txt', 'r') as arquivo:
    itens = arquivo.readlines()
    for item in itens:
        print(f"{item.strip()} (concluído)")


#11

with open('saudacao.txt', 'w') as arquivo:
    arquivo.write("Olá! Seja bem-vindo ao nosso programa.")



#12 

nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")

with open('cadastro.csv', 'w') as arquivo:
    arquivo.write(f"{nome},{email}\n")



#13
 vendas = ['produto A, 100', 'produto B, 250']

with open('vendas.txt', 'w') as arquivo:
    for item in vendas:
        arquivo.write(item + '\n')


#14

total = 0

with open('vendas.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha.strip())
        partes = linha.strip().split(', ')
        valor = int(partes[1])
        total += valor

print(f"Total de vendas: R$ {total}")
