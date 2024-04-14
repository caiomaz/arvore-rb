# Árvore Rubro-Negra

Este repositório contém uma implementação da estrutura de dados Árvore Rubro-Negra em Python. A Árvore Rubro-Negra é uma estrutura de dados de árvore binária de busca balanceada que garante operações de inserção, remoção e busca em tempo logarítmico no pior caso.

## Estrutura do Projeto

- **.gitignore**: Este arquivo é usado para especificar quais arquivos ou diretórios o Git deve ignorar.
- **main.py**: Este arquivo contém a implementação da Árvore Rubro-Negra, incluindo a definição das classes `Node` e `RedBlackTree`, métodos para inserção, remoção, busca, e verificação do balanceamento da árvore, bem como uma função para interação com o usuário e uma função para plotar a árvore.
- **readme.md**: Este arquivo contém informações sobre o projeto, incluindo uma visão geral da estrutura de diretórios, descrição dos arquivos e uma explicação detalhada do código contido em `main.py`.
- **requirements.txt**: Este arquivo contém as dependências do projeto, que deverão ser instaladas no ambiente virtual.

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

## Detalhes da Implementação em 'main.py'

### Importação de Bibliotecas

```python
import matplotlib.pyplot as plt
import networkx as nx
```

Essas linhas de código importam as bibliotecas Matplotlib e NetworkX, necessárias para plotar a árvore Rubro-Negra.

### Definição da Classe Node

```python
class Node:
    def __init__(self, key, parent=None, color="Red"):
        """
        Cria um novo nó com uma chave, um pai e uma cor.
        """
        self.key = key  # Atribui o valor da chave ao nó
        self.parent = parent  # Atribui o nó pai
        self.left = None  # Inicializa o nó filho esquerdo como None
        self.right = None  # Inicializa o nó filho direito como None
        self.color = color  # Atribui a cor do nó (padrão é "Red")
```

Esta classe define um nó da Árvore Rubro-Negra. Cada nó contém uma chave, uma referência para o nó pai, referências para os nós filhos esquerdo e direito, e uma cor (vermelho ou preto).

### Definição da Classe RedBlackTree

```python
class RedBlackTree:
    def __init__(self):
        """
        Inicializa a árvore Rubro-Negra com um nó nil como a raiz.
        """
        self.nil = Node(None, color="Black")  # Cria um nó nil com valor None e cor preta
        self.root = self.nil  # Define o nó nil como a raiz da árvore
```

Esta classe define a estrutura da Árvore Rubro-Negra. O construtor inicializa a árvore com um nó nil como raiz.
A classe `RedBlackTree` possui os seguintes métodos:

- init: Inicializa a árvore com um nó nil como raiz.
- transplant: Substitui a subárvore enraizada no nó u pela subárvore enraizada no nó v.
- left_rotate: Realiza uma rotação para a esquerda em torno de um nó x.
- right_rotate: Realiza uma rotação para a direita em torno de um nó x.
- insert_fixup: Corrige violações das propriedades da árvore após a inserção de um nó.
- insert: Insere um novo nó na árvore.
- delete_fixup: Corrige violações das propriedades da árvore após a remoção de um nó.
- minimum: Retorna o nó com a menor chave na subárvore enraizada em um determinado nó.
- remove: Remove um nó da árvore.
- search: Procura e retorna um nó com uma chave específica na árvore.
- inorder: Realiza um percurso em ordem na árvore, imprimindo as chaves dos nós e suas cores.
- check_balanced: Verifica se a árvore está balanceada, garantindo que todos os caminhos da raiz até as folhas contenham o mesmo número de nós pretos.

### Definição da Função plot(tree)

A função plot(tree) permite visualizar graficamente a estrutura de uma Árvore Rubro-Negra usando as bibliotecas NetworkX e Matplotlib em Python.

- Criação do Grafo: Um grafo direcionado é criado para representar a estrutura da árvore.
- Adição de Arestas: A função add_edges é utilizada para adicionar as arestas do grafo com base na estrutura da árvore.
- Cálculo da Altura Máxima: A altura máxima da árvore é calculada para posicionar os nós adequadamente na plotagem.
- Cálculo das Posições dos Nós: A função compute_position é responsável por calcular as posições dos nós na plotagem com base na profundidade na árvore.
- Coleta das Cores dos Nós: As cores dos nós (vermelho ou preto) são coletadas para atribuir cores aos nós na plotagem.
- Plotagem da Árvore: Finalmente, a função nx.draw_networkx é usada para plotar a árvore, com os nós coloridos de acordo com sua cor na árvore Rubro-Negra.

### Definição da Função interface()

A função interface() permite interagir com uma Árvore Rubro-Negra, oferecendo as seguintes funcionalidades:

```python
    print("\n1 - Inserir nó")
    print("2 - Remover nó")
    print("3 - Verificar se a árvore está balanceada")
    print("4 - Plotar a árvore Rubro-Negra")
    print("5 - Sair")
    option = input("Escolha uma opção: ")
    if option == "1": 
        key = int(input("Digite a chave do nó a ser inserido: "))
        rb_tree.insert(key)
    elif option == "2":
        key = int(input("Digite a chave do nó a ser removido: "))
        rb_tree.remove(key)
    elif option == "3":
        print("A árvore está balanceada:", rb_tree.check_balanced())
    elif option == "4":
        plot(rb_tree)
    elif option == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")
```

- Inserir Nó: Permite ao usuário inserir um nó na árvore, solicitando a chave do nó a ser inserido e realizando a inserção.
- Remover Nó: Permite ao usuário remover um nó da árvore, solicitando a chave do nó a ser removido e realizando a remoção.
- Verificar Balanceamento: Permite ao usuário verificar se a árvore está balanceada, exibindo o resultado da verificação.
- Plotar a Árvore: Permite ao usuário visualizar graficamente a estrutura da árvore Rubro-Negra por meio de uma plotagem.
- Sair: Encerra a interação com a árvore.