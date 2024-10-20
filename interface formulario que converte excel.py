import pandas as pd
import streamlit as st

# Define perguntas e nomes das colunas
perguntas = {
    'Nome': 'Qual seu nome?',
    'cpf': 'Qual seu cpf?',
    'telefone': 'Qual número de telefone?',
    'genero': 'Qual seu gênero?'
}

# Captura as respostas dinamicamente
respostas = {coluna: st.text_input(pergunta) for coluna, pergunta in perguntas.items()}

# Cria DataFrame e salva o arquivo diretamente
if st.button('Enviar'):
    df = pd.DataFrame([respostas])
    df.to_excel('formularioautomatico.xlsx', index=False)
    
    st.success('Arquivo gerado com sucesso!')
    st.write("O arquivo foi salvo como `formularioautomatico.xlsx` no seu diretório de trabalho.")
