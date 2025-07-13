# 🛒 Classificação Mercadológica de Produtos

Aplicação web interativa para classificar produtos de supermercado em uma **estrutura hierárquica mercadológica**, com base em modelos de machine learning treinados previamente.

Desenvolvido em Python com **Streamlit**, utiliza modelos `.pkl` armazenados no **Google Drive** e carregados automaticamente.

---

## ✅ Funcionalidades

- Classificação hierárquica:
  - **Departamento**
  - **Categoria**
  - **Subcategoria**
  - **Segmento**
- Input de produto por texto
- Visualização dos resultados na tela
- Gráficos interativos com **Plotly**
- Download automático dos modelos (não estão no GitHub)

---

## 🧠 Tecnologias

- `Python 3.11+`
- `Streamlit`
- `Scikit-learn`
- `Plotly`
- `gdown`
- `joblib`
- `pandas`

---

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/SEU_USUARIO/Classificacao_Mercadologica.git
cd Classificacao_Mercadologica
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

---

## 🚀 Executando o App

```bash
streamlit run app.py
```

> O Streamlit abrirá no navegador. Os modelos `.pkl` serão baixados automaticamente na primeira execução.

---

## 📁 Estrutura do Projeto

```
Classificacao_Mercadologica/
├── modelos.py             # Função para baixar/carregar modelos
├── app.py                 # Página principal de classificação
├── pages/
│   └── Graficos.py        # Página de visualização com gráficos
├── modelos/               # Armazena modelos baixados
├── requirements.txt
└── README.md
```

---

## 📤 Modelos e Vetorizadores

Os arquivos `.pkl` dos modelos e vetorizadores estão **armazenados no Google Drive** e são **baixados automaticamente** via `gdown` com base no dicionário em `modelos.py`.

> Não é necessário fazer o download manual.

---

## 📱 Compatibilidade

O aplicativo é compatível com:

- Desktop
- Celulares e tablets
- Hospedagem no [Streamlit Cloud](https://streamlit.io/cloud)

---

## 🧠 Autor

**Hélio da Silva Paiva Júnior**  
[LinkedIn](https://www.linkedin.com/in/heliospjunior) | [GitHub](https://github.com/heliospjunior)# Classificacao_Mercadologica
