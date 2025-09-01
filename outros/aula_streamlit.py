import streamlit as st

def soma(num1, num2):
    return num1 + num2
def subtracao(num1,num2):
    return num1 - num2
def multiplicacao(num1,num2):
    return num1 * num2
def divisao(num1,num2):
        if num2 != 0:       
            return num1 / num2
st.title("Calculadora Senai")
num1 = st.number_input("Selecione o primeiro numero", value = 0.0, step = 1.0)
num2 = st.number_input("Selecione o segundo numero", value = 0.0, step = 1.0)
operacoes = ["soma","subtração", "multiplicação", "divisão"]
operacao = st.selectbox("Escolha a operacao", operacoes)

resultado = 0
if operacao == "soma":
    resultado = soma(num1, num2)
elif operacao == "subtração":
    resultado = subtracao(num1, num2)
elif operacao == "multiplicação":
    resultado = multiplicacao(num1, num2)
elif operacao == "divisão":
    resultado = divisao(num1, num2)
if num2 == 0 and operacao == "divisão":
    st.error("É impossivel dividir um numero por 0")
else:
    if st.button("Gerar resultado"):
        st.success(f"Resultado da {operacao} é {resultado} ")

