import streamlit as st
import pandas as pd


if "turmas" not in st.session_state:
    st.session_state.turmas = []

if "alunos" not in st.session_state:
    st.session_state.alunos = []


st.title("📚 Sistema de Gerenciamento de Alunos")

menu = st.sidebar.radio("Menu", ["Cadastrar Turma", "Cadastrar Aluno", "Listar Alunos", "Análises"])

# Cadastro de Turma 
if menu == "Cadastrar Turma":
    st.header("Cadastrar Nova Turma")
    turma_nome = st.text_input("Nome da Turma")
    if st.button("Salvar Turma"):
        if turma_nome and turma_nome not in st.session_state.turmas:
            st.session_state.turmas.append(turma_nome)
            st.success(f"Turma '{turma_nome}' cadastrada com sucesso!")
        else:
            st.warning("Digite um nome válido ou a turma já existe.")

#  Cadastro de Aluno
elif menu == "Cadastrar Aluno":
    st.header("Cadastrar Novo Aluno")

    nome = st.text_input("Nome")
    idade = st.number_input("Idade", min_value=1, step=1)
    email = st.text_input("Email")
    telefone = st.text_input("Telefone")

    if st.session_state.turmas:
        turma = st.selectbox("Turma", st.session_state.turmas)
    else:
        st.warning("Cadastre uma turma primeiro!")
        turma = None

    materia = st.text_input("Matéria")
    notas = st.text_area("Notas (separadas por vírgula)", placeholder="Ex: 8, 7.5, 9")

    if st.button("Salvar Aluno"):
        if nome and turma:
            notas_lista = [float(n.strip()) for n in notas.split(",") if n.strip()]
            aluno = {
                "Nome": nome,
                "Idade": idade,
                "Email": email,
                "Telefone": telefone,
                "Turma": turma,
                "Matéria": materia,
                "Notas": notas_lista
            }
            st.session_state.alunos.append(aluno)
            st.success(f"Aluno '{nome}' cadastrado com sucesso!")
        else:
            st.warning("Preencha os campos obrigatórios.")

#  Listar Alunos 
elif menu == "Listar Alunos":
    st.header("Lista de Alunos")
    if st.session_state.alunos:
        df = pd.DataFrame(st.session_state.alunos)
        st.dataframe (df)
    else:
        st.info("Nenhum aluno foi cadastrado ainda.")

# Análises 
elif menu == "Análises":
    st.header("📊 Análises de Dados")
    if st.session_state.alunos:
        df = pd.DataFrame(st.session_state.alunos)

        # Média de idades
        media_idades = df["Idade"].mean()

        # Média de notas aluno
        medias_notas = df["Notas"].apply(lambda x: sum(x)/len(x) if len(x) > 0 else 0)
        df["Média Notas"] = medias_notas
        media_geral_notas = medias_notas.mean()

        st.metric("Média de Idade", f"{media_idades:.2f} anos")
        st.metric("Média Geral de Notas", f"{media_geral_notas:.2f}")

        st.subheader("Tabela com Médias de Notas")
        st.dataframe(df[["Nome", "Turma", "Matéria", "Média Notas"]])
    else:
        st.info("Nenhum dado disppnível para análise.")