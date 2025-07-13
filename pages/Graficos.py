import streamlit as st
import plotly.express as px
import pandas as pd

# Carregar os dados (ajuste o caminho se necessário)
produtos = pd.read_csv("produto633.csv")
hierarquia = pd.read_csv("hierarquia633.csv")

# ----------------------------------
# PRÉ-PROCESSAMENTO
# ----------------------------------

# Tamanho das descrições
produtos["desc_len"] = produtos["descricao"].astype(str).str.len()

# Merge com nomes da hierarquia
prod_hierarquia = produtos.merge(
    hierarquia[
        ["departamento_id", "descricao_departamento_id",
         "categoria_id", "descricao_categoria_id",
         "sub_categoria_id", "descricao_sub_categoria_id"]
    ].drop_duplicates(),
    on=["departamento_id", "categoria_id", "sub_categoria_id"],
    how="left"
)

# ----------------------------------
# INÍCIO DO APP
# ----------------------------------

st.set_page_config(layout="wide")
st.title("📊 Análise Visual da Estrutura Mercadológica de Produtos")


## ----------------------------------
# Top 10 Departamentos por número de Produtos
## ----------------------------------
st.header("📈 Top 10 Departamentos por Número de Produtos"
        )

# Garantir que não haja duplicidade no mapeamento
mapa_dept = hierarquia[['departamento_id', 'descricao_departamento_id']].dropna().drop_duplicates()

# Agrupar produtos por departamento_id
contagem = produtos['departamento_id'].value_counts().reset_index()
contagem.columns = ['departamento_id', 'quantidade']

# Juntar com o nome dos departamentos
contagem = contagem.merge(mapa_dept, on='departamento_id', how='left')

# Pegar os top 10
top10 = contagem.nlargest(10, 'quantidade')

# Gráfico interativo com Plotly
fig = px.bar(
    top10,
    x='descricao_departamento_id',
    y='quantidade',
    title='Top 10 Departamentos por Número de Produtos',
    labels={'descricao_departamento_id': 'Departamento', 'quantidade': 'Número de Produtos'}
)
st.plotly_chart(fig, use_container_width=True)


# ----------------------------------
# Treemap
# ----------------------------------
st.header("🗂️ Treemap da Hierarquia Mercadológica")

treemap_data = prod_hierarquia.groupby([
    "descricao_departamento_id",
    "descricao_categoria_id",
    "descricao_sub_categoria_id"
]).size().reset_index(name="quantidade")

fig_treemap = px.treemap(
    treemap_data,
    path=["descricao_departamento_id", "descricao_categoria_id", "descricao_sub_categoria_id"],
    values="quantidade",
)
st.plotly_chart(fig_treemap, use_container_width=True)

# ----------------------------------
# Boxplot
# ----------------------------------
st.header("📦 Comprimento das Descrições por Departamento")

prod_dept = produtos.merge(
    hierarquia[["departamento_id", "descricao_departamento_id"]].drop_duplicates(),
    on="departamento_id",
    how="left"
)

fig_box = px.box(
    prod_dept,
    x="descricao_departamento_id",
    y="desc_len",
    labels={"descricao_departamento_id": "Departamento", "desc_len": "Tamanho da Descrição"},
)
fig_box.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig_box, use_container_width=True)


# ----------------------------------
# Sunburst
# ----------------------------------
st.header("🌞 Sunburst (Hierarquia Completa)")

fig_sunburst = px.sunburst(
    treemap_data,
    path=["descricao_departamento_id", "descricao_categoria_id", "descricao_sub_categoria_id"],
    values="quantidade"
)
st.plotly_chart(fig_sunburst, use_container_width=True)
