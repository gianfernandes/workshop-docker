import streamlit as st

def mensagem_saudacao():
    return "Olá turma de dados! Aula de Docker"

def main():
    st.write(mensagem_saudacao())

if __name__ == "__main__":
    main()