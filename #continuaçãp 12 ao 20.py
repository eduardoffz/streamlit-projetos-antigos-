  #continuaçãp 12 ao 20


  
# 12. Geração de Relatório com Finalização
-
def gerar_relatorio():
    try:
        resultado = int("abc")  # Simulação de erro
    except Exception as e:
        print(f"Erro capturado: {e}")
    finally:
        print("Processo de relatório finalizado, com ou sem erros.")


# 13. Download de Arquivo Simulado

def simular_download():
    try:
        print("Baixando arquivo...")
        raise FileNotFoundError("Arquivo não encontrado.")
    except FileNotFoundError:
        print("Falha no download!")
    else:
        print("Download concluído com sucesso!")
    finally:
        print("Limpando recursos.")


# 14. Processamento de Dados com Log

def processamento_dados():
    try:
        numero = float(input("Digite um número para dividir 100: "))
        resultado = 100 / numero
    except ZeroDivisionError:
        print("LOG: Tentativa de divisão por zero!")
    else:
        print(f"Resultado: {resultado}")
    finally:
        print("Processamento de dados encerrado.")


# 15. Conversão Múltipla com Mensagem Única

def conversao_multipla():
    entrada = input("Digite um número: ")
    try:
        numero_int = int(entrada)
        numero_float = float(numero_int)
    except ValueError:
        print("Não foi possível converter para número.")
    else:
        print(f"Número convertido: {numero_float}")


# 16. Função obter_numero_inteiro_seguro()

def obter_numero_inteiro_seguro():
    while True:
        try:
            numero = int(input("Digite um número inteiro válido: "))
            return numero
        except ValueError:
            print("Entrada inválida. Tente novamente.")


# 17. Busca Segura em Dicionário com Função

def buscar_info_aluno(dicionario_aluno, chave_info):
    try:
        return dicionario_aluno[chave_info]
    except KeyError:
        return f"Informação '{chave_info}' não encontrada."


# 18. Calculadora Robusta com Função

def fazer_operacao(num1, num2, operacao):
    if operacao == "soma":
        return num1 + num2
    elif operacao == "divisao":
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Erro: divisão por zero."
    else:
        return "Operação inválida."


# 19. Loop de Login com Tentativas Limitadas

def login_com_tentativas():
    usuario_correto = "admin"
    senha_correta = "1234"
    tentativas = 0

    while tentativas < 3:
        try:
            usuario = input("Usuário: ")
            senha = input("Senha: ")
        except Exception:
            print("Erro inesperado na entrada.")
            continue

        if usuario == usuario_correto and senha == senha_correta:
            print("Login bem-sucedido!")
            return
        else:
            print("Usuário ou senha incorretos.")
            tentativas += 1

    print("Login bloqueado.")


# 20. Leitura de Lista de Nomes (linha a linha, segura)

def ler_nomes_do_arquivo(nome_arquivo):
    nomes = []
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nomes.append(linha.strip())
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    return nomes


# Programa Principal

if __name__ == "__main__":
    print("\n--- Execução dos Exercícios 12 a 20 ---\n")

    print("\n[12] Relatório com Finalização:")
    gerar_relatorio()

    print("\n[13] Download Simulado:")
    simular_download()

    print("\n[14] Processamento de Dados com Log:")
    processamento_dados()

    print("\n[15] Conversão Múltipla:")
    conversao_multipla()

    print("\n[16] Número Inteiro Seguro:")
    numero_seguro = obter_numero_inteiro_seguro()
    print(f"Número obtido: {numero_seguro}")

    print("\n[17] Busca em Dicionário:")
    aluno = {"nome": "Carlos", "idade": 17, "nota": 8.5}
    print(buscar_info_aluno(aluno, "nome"))
    print(buscar_info_aluno(aluno, "endereco"))

    print("\n[18] Calculadora Robusta:")
    resultado_soma = fazer_operacao(10, 5, "soma")
    resultado_divisao = fazer_operacao(10, 0, "divisao")
    print("Soma:", resultado_soma)
    print("Divisão:", resultado_divisao)

    print("\n[19] Login com Tentativas:")
    login_com_tentativas()

    print("\n[20] Leitura de nomes do arquivo:")
    nomes = ler_nomes_do_arquivo("nomes.txt")
    print("Nomes lidos:", nomes)