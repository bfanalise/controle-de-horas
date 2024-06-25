import streamlit as st
from datetime import datetime, timedelta

def calcular_horas(entrada, almoco, retorno, saida):
    # Convertendo os horários para datetime
    hoje = datetime.today()
    entrada_dt = datetime.combine(hoje, entrada)
    almoco_dt = datetime.combine(hoje, almoco)
    retorno_dt = datetime.combine(hoje, retorno)
    saida_dt = datetime.combine(hoje, saida)

    # Calculando o tempo de trabalho antes e depois do almoço
    periodo1 = almoco_dt - entrada_dt
    periodo2 = saida_dt - retorno_dt

    # Somando os períodos de trabalho
    total_trabalho = periodo1 + periodo2

    # Jornada diária padrão (8 horas e 48 minutos)
    jornada_padrao = timedelta(hours=8, minutes=48)

    # Calculando horas extras
    horas_extras = total_trabalho - jornada_padrao

    return total_trabalho, horas_extras
    # Rodando no navegador -> Streamlit para formulário
with st.form(key='Jornada'):
    entrada = st.time_input(label='Início da jornada')
    almoco = st.time_input(label='Saída para almoço')
    retorno = st.time_input(label='Retorno do Almoço')
    saida = st.time_input(label='Fim da jornada')
    botao = st.form_submit_button('Calcular Horas')
    if botao:
        total_trabalho, horas_extras = calcular_horas(entrada, almoco, retorno, saida)
        st.write(f'Total de horas trabalhadas: {total_trabalho}')
        st.write(f'Horas extras: {horas_extras}')
