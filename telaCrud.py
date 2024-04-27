import streamlit as st

st.title('Meu título')
st.write('Olá mundão!')

escolha = st.selectbox('Selecione o turno de interesse',
                       ['Manha', 'tarde', 'noite'])

# textos renderizados

if escolha:
    st.write(escolha)

radio= st.radio('Selecione uma opção', ['Manha', 'tarde', 'noite'])

texto = st.text_input('Digite seu nome')
numero = st.number_input('Digite um numero')
if texto and numero:
    st.write(texto, numero)

cpf = st.text_input("Digite seu CPF", placeholder="000.000.000-00")

btnCadastrar = st.button('Cadastrar')

st.write(btnCadastrar)

textolongo = st.text_area('Digite sua reclamação')