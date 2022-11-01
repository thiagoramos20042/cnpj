import streamlit as st
from PIL import Image
import requests
import json
import webbrowser
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pprint import pprint
from brfinance import CVMAsyncBackend
from datetime import datetime, date
from flatten_json import flatten


# Def com múltiplas páginas
def main_page():
    st.sidebar.markdown("# Consultar CNPJ")
    # Adicionando a logo
    foto = Image.open('logo-data-marketplace-500x85-1.png')
    st.image(foto,
             use_column_width=False)

    # Escrevendo um título na página
    st.title('APLICAÇÃO DE CONSULTA CNPJ')

    # Input do usuário

    input_num = st.text_input(
        'Escreva os números do CNPJ (somente dados númericos)',
        value=00000000)
    st.write('O número digitado foi: ', input_num)

    # Consulta api

    def consulta_cnpj(cnpj):
        url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
        querystring = {"token": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX", "cnpj": "", "plugin": "RF"}

        response = requests.request("GET", url, params=querystring)
        resp = json.loads(response.text)
        print(resp)
        # return resp['nome'], resp['logradouro'], resp['telefone'], resp['data_situacao'], resp['matriz'],

        # Salvando em um arquivo json
        out_file = open("consulta_cnpj.json", "w")

        json.dump(resp, out_file, ensure_ascii=False)

        out_file.close()

    # Chamando a função
    consulta_cnpj(input_num)

    # Lendo o arquivo consulta_cnpj.json
    with open("consulta_cnpj.json") as file:
        data = json.load(file)
    pprint(data)

    # Função flatten para criar o dataframe pandas
    def flatten(d):
        out = {}
        for key, val in d.items():
            if isinstance(val, dict):
                val = [val]
            if isinstance(val, list):
                for subdict in val:
                    deeper = flatten(subdict).items()
                    out.update({key + '_' + key2: val2 for key2, val2 in deeper})
            else:
                out[key] = val
        return out

    # Chamando a função e normalizando dados para o pandas
    df = flatten(data)
    df2 = pd.json_normalize(df)

    # Apresentando os dados
    st.dataframe(df2)

    # Botão download
    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df(df2)

    st.header("Download CSV")
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='dados_cnpj.csv',
        mime='text/csv',
    )

    # Documentação Api
    st.header("Rate Limits")
    st.write(
        "Esta API permite 3 consultas por minuto. No caso do limite ser excedido, o código HTTP retornado é o 429.")

    st.header("Timeouts")
    st.write(
        "Nesta API Pública não há resolução de consultas que precisam dados em tempo real. Os dados são retornados "
        "apenas para consultas realizadas no banco de dados. Outras consultas retornam o código HTTP 504 indicando "
        "timeout.")

    st.header("ReceitaWS API")
    st.write("Método para recuperar as informações de uma empresa brasileira através do seu CNPJ, "
             "as informações são exatamente as mesmas informações retornadas pelo site da Receita Federal Brasileira.")


#def page2():
    # Adicionando a logo
#    foto = Image.open('logo-data-marketplace-500x85-1.png')
#    st.image(foto,use_column_width=False)
#    st.title("Consulta de protesto")
#    st.sidebar.markdown("Cartório de protesto")
#    url = 'https://site.cenprotnacional.org.br/'
#    if st.button('Clique Aqui'):
#        webbrowser.open_new_tab(url)



#Chamando as funções de cada página
page_names_to_funcs = {
    "Consultar CNPJ": main_page,
    #"Cartório de protesto": page2,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()



