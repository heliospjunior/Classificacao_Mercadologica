import os
import joblib
import gdown
import streamlit as st

# Dicionário com todos os arquivos a serem carregados
ARQUIVOS = {
    "model_dep": {
        "arquivo": "modelos/model_dep.pkl",
        "url": "https://drive.google.com/uc?id=1qcT9E777IAyQMbmGidBE-5X8osQVAVU4"
    },
    "model_cat": {
        "arquivo": "modelos/model_cat.pkl",
        "url": "https://drive.google.com/uc?id=1z6Jd3nOjAivHj0L2IKVQ-dTAwqXbVY8t"
    },
    "model_subcat": {
        "arquivo": "modelos/model_subcat.pkl",
        "url": "https://drive.google.com/uc?id=1PJ6Jg3aH_qFli7QeZDTuy0WSMnzYtu_F"
    },
    "model_seg": {
        "arquivo": "modelos/model_seg.pkl",
        "url": "https://drive.google.com/uc?id=1Vy_Wj6Rz6afMxZTl50jGVxQ26KU5iFVw"
    },
    "vectorizer_dep": {
        "arquivo": "modelos/vectorizer_dep.pkl",
        "url": "https://drive.google.com/uc?id=1GkKIZow8e59PzJ6SLqJz0g7Yo3fZ4ysz"
    },
    "vectorizer_cat": {
        "arquivo": "modelos/vectorizer_cat.pkl",
        "url": "https://drive.google.com/uc?id=1gD-1Qm1qUHS-ecOaQDYa8W2U_7Vu1jGY"
    },
    "vectorizer_subcat": {
        "arquivo": "modelos/vectorizer_subcat.pkl",
        "url": "https://drive.google.com/uc?id=16tMNrWFqyUge62yWrpLxcthmHKT9A1FW"
    },
    "vectorizer_seg": {
        "arquivo": "modelos/vectorizer_seg.pkl",
        "url": "https://drive.google.com/uc?id=1WsFgl7GJnyeZnJyxhWablkB7Mq362Ry9"
    },
    "departamento_dict": {
        "arquivo": "modelos/departamento_dict.pkl",
        "url": "https://drive.google.com/uc?id=1jrf_RRJhXa07-d2gdos8G3JhCI53qMFI"
    },
    "categoria_dict": {
        "arquivo": "modelos/categoria_dict.pkl",
        "url": "https://drive.google.com/uc?id=1J82EZWVGSyDnSVKwjlny1HjA43oaWgGE"
    },
    "subcategoria_dict": {
        "arquivo": "modelos/subcategoria_dict.pkl",
        "url": "https://drive.google.com/uc?id=14vTWLq9CeKtIifTDqm3C3sXm3de8nJHV"
    },
    "segmento_dict": {
        "arquivo": "modelos/segmento_dict.pkl",
        "url": "https://drive.google.com/uc?id=1_M5NeOcEuLvKgE4I_a1U1zuayMTFPz1C"
    },
}

@st.cache_resource
def carregar_arquivo(nome):
    """Baixa e carrega o arquivo especificado, se necessário."""
    info = ARQUIVOS[nome]
    caminho = info["arquivo"]
    url = info["url"]

    os.makedirs(os.path.dirname(caminho), exist_ok=True)

    if not os.path.exists(caminho):
        with st.spinner(f"🔄 Baixando {nome}..."):
            gdown.download(url, caminho, quiet=False)

    return joblib.load(caminho)
