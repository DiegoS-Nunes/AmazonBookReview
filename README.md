# Amazon Book Review

Este repositório contém um projeto de análise de dados de resenhas de livros da Amazon, utilizando a biblioteca Streamlit para criar uma interface interativa. O projeto permite visualizar e filtrar informações sobre os livros mais populares e suas respectivas resenhas.

## Funcionalidades

- **Visualização de Livros Populares**: Exibe uma lista dos 100 livros mais populares, permitindo filtrar por preço.
- **Detalhes do Livro**: Mostra detalhes como título, gênero, preço, classificação e ano de publicação de um livro selecionado.
- **Resenhas de Clientes**: Exibe resenhas de clientes para o livro selecionado.
- **Gráficos Interativos**: Inclui gráficos interativos para análise de dados, como distribuição de preços e publicações por ano.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Streamlit**: Biblioteca para criação de aplicações web interativas.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **Plotly**: Biblioteca para criação de gráficos interativos.

## Como Executar

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/amazon-book-review.git
    ```
2. Navegue até o diretório do projeto:
    ```sh
    cd amazon-book-review
    ```
3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```
4. Execute a aplicação:
    ```sh
    streamlit run pages/books_review.py
    ```

## Estrutura do Projeto

- `pages/books_review.py`: Script principal que contém a interface interativa, gráficos e exibe detalhes e resenhas dos livros.
- `dataset/`: Diretório contendo os arquivos CSV com os dados dos livros e resenhas.

---

# Amazon Book Review

This repository contains a data analysis project of Amazon book reviews, using the Streamlit library to create an interactive interface. The project allows you to view and filter information about the most popular books and their respective reviews.

## Features

- **Popular Books Visualization**: Displays a list of the top 100 most popular books, allowing filtering by price.
- **Book Details**: Shows details such as title, genre, price, rating, and publication year of a selected book.
- **Customer Reviews**: Displays customer reviews for the selected book.
- **Interactive Charts**: Includes interactive charts for data analysis, such as price distribution and publications by year.

## Technologies Used

- **Python**: Main programming language.
- **Streamlit**: Library for creating interactive web applications.
- **Pandas**: Library for data manipulation and analysis.
- **Plotly**: Library for creating interactive charts.

## How to Run

1. Clone the repository:
    ```sh
    git clone https://github.com/seu-usuario/amazon-book-review.git
    ```
2. Navigate to the project directory:
    ```sh
    cd amazon-book-review
    ```
3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Run the application:
    ```sh
    streamlit run pages/books_review.py
    ```

## Project Structure

- `pages/books_review.py`: Main script containing the interactive interface, charts, and displays book details and reviews.
- `dataset/`: Directory containing the CSV files with book and review data.