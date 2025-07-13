import streamlit as st

st.title("Considerações Importantes")
st.markdown("""
***
            
## **Sobre o projeto:**
            
* Primeira versão do projeto de classificação mercadológica utilizando Machine Learning feito por Hélio Paiva Júnior - 11/07/2025)
* Este projeto visa classificar produtos em uma hierarquia mercadológica composta por quatro níveis: Departamento, Categoria, Subcategoria e Segmento.
            
***

## **Informações sobre as bases**

* As tabelas analisadas são reais e foram extraídas do banco de dados do Novo Avanço QAS, com foco nos registros da empresa com empresa_id = 633.
* Essa empresa está cadastrada como 'Demo Comercial', indicando tratar-se de uma base demonstrativa. No entanto, os CNPJs presentes são reais e, em sua maioria, pertencem à rede Kalu Supermercados.
* Foram utilizadas duas planilhas principais para treinar e validar os modelos:
    * produtos — com 26.332 registros
    * classificacao_mercadologica — com 10.310 registros

***
            
## **Considerações sobre as bases**

* **Não há um padrão universal de estrutura mercadológica**, portanto, os resultados apresentados são condizentes com o conteúdo das bases utilizadas, em todos os níveis da hierarquia mercadológica.
* As **descrições e classificações** utilizadas refletem exatamente o que está presente nas tabelas originais, incluindo os vínculos entre categorias.
* Os **dados estão significativamente desbalanceados**, como evidenciado nos gráficos, o que pode impactar negativamente o desempenho e a generalização dos modelos.
* A **qualidade e extensão das descrições** influenciam diretamente na precisão dos resultados — conforme esperado, descrições mais completas tendem a gerar classificações mais assertivas.

""")