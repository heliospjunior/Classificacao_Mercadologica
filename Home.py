import streamlit as st
import numpy as np
import pandas as pd


import joblib

from modelos import carregar_arquivo

# Carregando modelos treinados
model_dep = carregar_arquivo("model_dep")
model_cat = carregar_arquivo("model_cat")
model_subcat = carregar_arquivo("model_subcat")
model_seg = carregar_arquivo("model_seg")

# Carregando vetorizadores TF-IDF treinados
vectorizer_dep = carregar_arquivo("vectorizer_dep")
vectorizer_cat = carregar_arquivo("vectorizer_cat")
vectorizer_subcat = carregar_arquivo("vectorizer_subcat")
vectorizer_seg = carregar_arquivo("vectorizer_seg")

# Carregando os dicionários com nomes
departamento_dict = carregar_arquivo("departamento_dict")
categoria_dict = carregar_arquivo("categoria_dict")
subcategoria_dict = carregar_arquivo("subcategoria_dict")
segmento_dict = carregar_arquivo("segmento_dict")


def mostrar_top3(probas, classes, dicionario):
    top3_idx = np.argsort(probas)[::-1][:3]
    resultados = []
    for i in top3_idx:
        classe = classes[i]
        prob = round(probas[i] * 100, 2)
        nome = dicionario.get(classe, "Desconhecido")
        resultados.append({"Código": classe, "Nome": nome, "Probabilidade (%)": prob})
    return resultados

def prever_classificacao_top3(descricao_produto):
    #print(f"\n Produto: {descricao_produto}")
    resultado = {}

    # ---------- Departamento ----------
    entrada_vec_dep = vectorizer_dep.transform([descricao_produto])
    probas_dep = model_dep.predict_proba(entrada_vec_dep)[0]
    top3_dep = mostrar_top3(probas_dep, model_dep.classes_, departamento_dict)
    pred_dep = top3_dep[0]["Código"]
    resultado["Departamento"] = top3_dep


      # ---------- Categoria ----------
    entrada_cat = f"{pred_dep} {descricao_produto}"
    entrada_vec_cat = vectorizer_cat.transform([entrada_cat])
    probas_cat = model_cat.predict_proba(entrada_vec_cat)[0]
    top3_cat = mostrar_top3(probas_cat, model_cat.classes_, categoria_dict)
    pred_cat = top3_cat[0]["Código"]
    resultado["Categoria"] = top3_cat

    
    # ---------- Subcategoria ----------
    entrada_subcat = f"{pred_dep} {pred_cat} {descricao_produto}"
    entrada_vec_subcat = vectorizer_subcat.transform([entrada_subcat])
    probas_subcat = model_subcat.predict_proba(entrada_vec_subcat)[0]
    top3_subcat = mostrar_top3(probas_subcat, model_subcat.classes_, subcategoria_dict)
    pred_subcat = top3_subcat[0]["Código"]
    resultado["Subcategoria"] = top3_subcat

    
    # ---------- Segmento ----------
    entrada_seg = f"{pred_dep} {pred_cat} {pred_subcat} {descricao_produto}"
    entrada_vec_seg = vectorizer_seg.transform([entrada_seg])
    probas_seg = model_seg.predict_proba(entrada_vec_seg)[0]
    top3_seg = mostrar_top3(probas_seg, model_seg.classes_, segmento_dict)
    resultado["Segmento"] = top3_seg

    
    return resultado

# -------------- Interface com Streamlit -----------------

st.set_page_config(page_title="Classificação de Produtos", layout="centered")
st.title("Classificação Mercadológica de Produtos")

st.markdown("""
Insira a descrição de um produto:**
""")

# Campo de entrada
descricao_input = st.text_input("Descrição do produto", placeholder="Ex: Batata Frita Congelada 1kg")

# Processamento
if descricao_input.strip():
    st.markdown("---")
    st.subheader("Resultado da Classificação")

    resultado = prever_classificacao_top3(descricao_input.strip())

    for nivel, top3 in resultado.items():
        st.markdown(f"### {nivel}")
        df = pd.DataFrame(top3)
        st.dataframe(df.style.format({"Probabilidade (%)": "{:.2f}"}), use_container_width=True)