# Execução do Código da Árvore Rubro-Negra

## Preparar Ambiente de Execução

1. Execute o comando abaixo para gerar um ambiente virtual:
    ```
    py -m venv .venv
    ```

2. Ative o ambiente virtual:
    - No Windows:
        - Navegue até o diretório de scripts do ambiente virtual:
            ```
            cd .venv\Scripts
            ```
        - Execute o comando `activate`:
            ```
            activate
            ```
    - No Linux/macOS:
        - Navegue até o diretório de scripts do ambiente virtual:
            ```
            source .venv/bin/activate
            ```

3. Volte para o diretório raiz do projeto:
    ```
    cd ../..
    ```

4. Instale as dependências do projeto no ambiente virtual:
    ```
    pip install -r requirements.txt
    ```

## Executar o Código

Execute o seguinte comando para executar o código da Árvore Rubro-Negra:
```
py main.py
```
Isso iniciará a execução do código, e uma janela será aberta exibindo a plotagem da Árvore Rubro-Negra.