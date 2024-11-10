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
    streamlit run app.py
    ```

## Estrutura do Projeto

- `app.py`: Script principal que contém a interface interativa e gráficos.
- `books_review.py`: Script que exibe detalhes e resenhas dos livros.
- `dataset/`: Diretório contendo os arquivos CSV com os dados dos livros e resenhas.