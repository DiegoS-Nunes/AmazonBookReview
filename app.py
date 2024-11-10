import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("dataset/customer reviews.csv")
df_top100_books = pd.read_csv("dataset/Top-100 Trending Books.csv")

preco_maximo = df_top100_books["book price"].max()
preco_minimo = df_top100_books["book price"].min()

preco = st.sidebar.slider("Selecione o preço do livro:",preco_minimo,preco_maximo,preco_maximo)

df_books = df_top100_books[df_top100_books["book price"]<=preco]

df_books

fig = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])

col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)