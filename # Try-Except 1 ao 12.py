#  Try-Except 1 ao 12

# --- Exercício 1: Conversor Seguro de Idade ---
print("--- Exercício 1: Conversor Seguro de Idade ---")
try:
    idade = int(input("Digite sua idade: "))
    print(f"Sua idade é: {idade}")
except ValueError:
    print("Idade inválida! Por favor, digite um número.")
print("-" * 30)

# --- Exercício 2: Calculadora de Soma à Prova de Erros ---
print("--- Exercício 2: Calculadora de Soma à Prova de Erros ---")
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(f"A soma é: {num1 + num2}")
except ValueError:
    print("Entrada inválida! Digite apenas números.")
print("-" * 30)

# --- Exercício 3: Conversor de Temperatura Robusto ---
print("--- Exercício 3: Conversor de Temperatura Robusto ---")
try:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"A temperatura em Fahrenheit é: {fahrenheit}")
except ValueError:
    print("Temperatura inválida!")
print("-" * 30)

# --- Exercício 4: Validador de Nota ---
print("--- Exercício 4: Validador de Nota ---")
try:
    nota = float(input("Digite uma nota de 0 a 10: "))
    if 0 <= nota <= 10:
        print(f"Nota válida: {nota}")
    else:
        print("Nota fora do intervalo válido!")
except ValueError:
    print("Entrada inválida! Digite apenas números.")
print("-" * 30)

# --- Exercício 5: Preço do Produto com Validação ---
print("--- Exercício 5: Preço do Produto com Validação ---")
try:
    preco = float(input("Digite o preço do produto: "))
    print(f"Preço registrado: R$ {preco:.2f}")
except ValueError:
    print("Preço inválido!")
print("-" * 30)

# --- Exercício 6: Divisor Seguro ---
print("--- Exercício 6: Divisor Seguro ---")
try:
    numerador = float(input("Digite o numerador: "))
    denominador = float(input("Digite o denominador: "))
    resultado = numerador / denominador
    print(f"O resultado da divisão é: {resultado}")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")
except ValueError:
    print("Entrada inválida! Digite apenas números.")
print("-" * 30)

# --- Exercício 7: Acessando Lista com Segurança ---
print("--- Exercício 7: Acessando Lista com Segurança ---")
frutas = ["Maçã", "Banana", "Uva"]
try:
    indice = int(input("Digite um índice para a lista de frutas (0, 1 ou 2): "))
    print(f"A fruta na posição {indice} é: {frutas[indice]}")
except IndexError:   
    print("Índice inválido! Essa posição não existe.")
except ValueError:
    print("Entrada inválida! Digite um número inteiro.")
print("-" * 30)

# --- Exercício 8: Buscando Chave no Dicionário ---
print("--- Exercício 8: Buscando Chave no Dicionário ---")
aluno = {"nome": "Leo", "idade": 17}
try:
    chave = input("Digite a chave que você quer buscar (ex: 'nome', 'cidade'): ")
    print(f"O valor da chave '{chave}' é: {aluno[chave]}")
except KeyError:
    print("Chave não encontrada!")
print("-" * 30)

# --- Exercício 9: Cálculo de Média Robusto ---
print("--- Exercício 9: Cálculo de Média Robusto ---")
notas = []
try:
    num_notas = int(input("Quantas notas você quer adicionar? "))
    for i in range(num_notas):
        try:
            nota = float(input(f"Digite a nota {i+1}: "))
            notas.append(nota)
        except ValueError:
            print("Entrada inválida! Apenas números serão adicionados.")
    media = sum(notas) / len(notas)
    print(f"A média das notas é: {media}")
except ZeroDivisionError:
    print("Erro: A lista de notas está vazia. Não é possível calcular a média.")
except ValueError:
    print("Número de notas inválido.")
print("-" * 30)

# --- Exercício 10: Acessando Caracteres de uma String Seguramente ---
print("--- Exercício 10: Acessando Caracteres de uma String Seguramente ---")
try:
    palavra = input("Digite uma palavra: ")
    indice = int(input(f"Digite um índice (0 a {len(palavra)-1}): "))
    print(f"O caractere na posição {indice} é: {palavra[indice]}")
except IndexError:
    print("Posição fora da palavra!")
except ValueError:
    print("Índice inválido! Digite um número.")
print("-" * 30)

# --- Exercício 11: Login com Boas-Vindas ---
print("--- Exercício 11: Login com Boas-Vindas ---")
try:
    usuario = input("Digite o nome de usuário: ")
    senha_str = input("Digite a senha: ")
    senha_int = int(senha_str)
except ValueError:
    print("Erro de login. A senha deve ser um número inteiro para este exemplo.")
else:
    print("Login bem-sucedido!")
print("-" * 30)

# --- Exercício 12: Geração de Relatório com Finalização ---
print("--- Exercício 12: Geração de Relatório com Finalização ---")
try:
    print("Gerando relatório...")
    # Simula um erro de propósito
    resultado = 10 / 0  
except ZeroDivisionError:
    print("ocorreu um erro ao gerar o relatório.")
finally:
    print("Processo de relatorio finalizado, com ou sem erros.")
print("-" * 30)

