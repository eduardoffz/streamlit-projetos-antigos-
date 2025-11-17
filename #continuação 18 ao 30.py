#continuação 18 ao 30

import random
import string


# 18. Calcular IMC

    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    imc = peso / (altura ** 2)
    return imc

#
# 19. Verificar Login
# 
def verificar_login(usuario_correto, senha_correta):
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    return usuario == usuario_correto and senha == senha_correta


# 21. Mensagens Diárias

def gerar_mensagens_diarias(lista_nomes):
    for nome in lista_nomes:
        print(f"Bom dia, {nome}! Tenha um ótimo dia!")


# 22. Adicionar Lembrete

def adicionar_lembrete(lista_lembretes):
    lembrete = input("Digite um novo lembrete: ")
    lista_lembretes.append(lembrete)


# 23. Jogo de Adivinhação

def jogar_adivinhacao(numero_secreto):
    while True:
        tentativa = input("Adivinhe o número ou digite 'sair': ")
        if tentativa.lower() == 'sair':
            return False
        elif int(tentativa) == numero_secreto:
            return True


# 26. Gerar Senha Aleatória

def gerar_senha(tamanho):
    caracteres = string.ascii_lowercase + string.digits
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


# 27. Gerenciador de Tarefas

def mostrar_tarefas(lista):
    print("Tarefas:")
    for i, tarefa in enumerate(lista):
        print(f"{i + 1}. {tarefa}")

def adicionar_tarefa(lista):
    tarefa = input("Digite a nova tarefa: ")
    lista.append(tarefa)

def remover_tarefa(lista):
    mostrar_tarefas(lista)
    indice = int(input("Digite o número da tarefa a remover: ")) - 1
    if 0 <= indice < len(lista):
        lista.pop(indice)


# 28. Operações Bancárias

def ver_saldo(saldo_atual):
    return saldo_atual

def depositar(saldo_atual, valor):
    return saldo_atual + valor

def sacar(saldo_atual, valor):
    if valor <= saldo_atual:
        return saldo_atual - valor
    else:
        print("Saldo insuficiente!")
        return saldo_atual


# 29. Jogo Par ou Ímpar

def jogar_par_ou_impar(escolha_jogador):
    numero_computador = random.randint(1, 10)
    numero_jogador = int(input("Digite um número de 1 a 10: "))
    soma = numero_computador + numero_jogador
    resultado = "par" if soma % 2 == 0 else "ímpar"
    print(f"Computador jogou {numero_computador}, soma = {soma} ({resultado})")
    if resultado == escolha_jogador:
        print("🎉 Você Ganhou!")
    else:
        print("😢 Você Perdeu!")


# 30. Sistema de Registro de Alunos

def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    notas = [float(input(f"Nota {i+1}: ")) for i in range(3)]
    return [nome] + notas

def calcular_media_aluno(lista_aluno):
    return sum(lista_aluno[1:]) / 3

def mostrar_boletim(lista_aluno, media):
    print(f"\n📘 Boletim de {lista_aluno[0]}")
    print("Notas:", lista_aluno[1:])
    print(f"Média: {media:.2f}")


# Programa Principal com Menu Geral

tarefas = []
lembretes = []
todos_os_alunos = []
saldo = 1000.0
usuario_correto = "admin"
senha_correta = "1234"

while True:
    print("\n=== MENU GERAL ===")
    print("1. Calcular IMC")
    print("2. Verificar Login")
    print("3. Mensagens Diárias")
    print("4. Adicionar Lembrete")
    print("5. Jogo de Adivinhação")
    print("6. Gerar Senha Aleatória")
    print("7. Gerenciar Tarefas")
    print("8. Operações Bancárias")
    print("9. Jogar Par ou Ímpar")
    print("10. Registro de Alunos")
    print("0. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        imc = calcular_imc()
        print(f"Seu IMC é: {imc:.2f}")

    elif opcao == "2":
        if verificar_login(usuario_correto, senha_correta):
            print("Login bem-sucedido!")
        else:
            print("Usuário ou senha incorretos!")

    elif opcao == "3":
        nomes = input("Digite nomes separados por vírgula: ").split(",")
        gerar_mensagens_diarias([nome.strip() for nome in nomes])

    elif opcao == "4":
        adicionar_lembrete(lembretes)
        print("Lembretes atuais:", lembretes)

    elif opcao == "5":
        numero_secreto = random.randint(1, 10)
        if jogar_adivinhacao(numero_secreto):
            print("Você venceu!")
        else:
            print("Que pena, você não acertou!")

    elif opcao == "6":
        tamanho = int(input("Tamanho da senha: "))
        print("Senha gerada:", gerar_senha(tamanho))

    elif opcao == "7":
        print("\n1. Mostrar tarefas\n2. Adicionar tarefa\n3. Remover tarefa")
        sub_opcao = input("Escolha: ")
        if sub_opcao == "1":
            mostrar_tarefas(tarefas)
        elif sub_opcao == "2":
            adicionar_tarefa(tarefas)
        elif sub_opcao == "3":
            remover_tarefa(tarefas)

    elif opcao == "8":
        print("\n1. Ver saldo\n2. Depositar\n3. Sacar")
        sub_opcao = input("Escolha: ")
        if sub_opcao == "1":
            print("Saldo atual:", ver_saldo(saldo))
        elif sub_opcao == "2":
            valor = float(input("Valor para depositar: "))
            saldo = depositar(saldo, valor)
        elif sub_opcao == "3":
            valor = float(input("Valor para sacar: "))
            saldo = sacar(saldo, valor)

    elif opcao == "9":
        escolha = input("Você escolhe 'par' ou 'ímpar'? ").lower()
        if escolha in ["par", "ímpar"]:
            jogar_par_ou_impar(escolha)
        else:
            print("Escolha inválida.")

    elif opcao == "10":
        print("\n1. Cadastrar aluno\n2. Mostrar boletins")
        sub_opcao = input("Escolha: ")
        if sub_opcao == "1":
            aluno = cadastrar_aluno()
            media = calcular_media_aluno(aluno)
            mostrar_boletim(aluno, media)
            todos_os_alunos.append(aluno)
        elif sub_opcao == "2":
            if not todos_os_alunos:
                print("Nenhum aluno cadastrado.")
            else:
                for aluno in todos_os_alunos:
                    media = calcular_media_aluno(aluno)
                    mostrar_boletim(aluno, media)

    elif opcao == "0":
        print("Encerrando o programa. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")