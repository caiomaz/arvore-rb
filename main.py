import matplotlib.pyplot as plt # Importa a biblioteca Matplotlib para plotar a árvore
import networkx as nx # Importa a biblioteca NetworkX para criar o grafo da árvore

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

class RedBlackTree:
    def __init__(self):
        """
        Inicializa a árvore Rubro-Negra com um nó nil como a raiz.
        """
        self.nil = Node(None, color="Black")  # Cria um nó nil com valor None e cor preta
        self.root = self.nil  # Define o nó nil como a raiz da árvore

    def transplant(self, u, v):
        """
        Substitui a subárvore enraizada no nó 'u' pela subárvore enraizada no nó 'v'.
        """
        if u.parent == self.nil: # Verifica se o pai de u é o nó nil (u é a raiz)
            self.root = v  # Define v como a nova raiz da árvore
        elif u == u.parent.left: # Verifica se u é o filho esquerdo de seu pai
            u.parent.left = v  # Define v como o novo filho esquerdo do pai de u
        else:
            u.parent.right = v  # Define v como o novo filho direito do pai de u
        v.parent = u.parent  # Define o pai de v como o pai de u

    def left_rotate(self, x):
        """
        Realiza uma rotação para a esquerda em torno do nó 'x'.
        """
        y = x.right  # Armazena o filho direito de x em y
        x.right = y.left  # Define o filho esquerdo de y como o filho direito de x
        if y.left != self.nil:  # Verifica se o filho esquerdo de y não é o nó nil
            y.left.parent = x  # Define o pai do filho esquerdo de y como x
        y.parent = x.parent  # Define o pai de y como o pai de x
        if x.parent == self.nil:  # Verifica se o pai de x é o nó nil (x é a raiz)
            self.root = y  # Define y como a nova raiz da árvore
        elif x == x.parent.left:  # Verifica se x é o filho esquerdo de seu pai
            x.parent.left = y  # Define y como o novo filho esquerdo do pai de x
        else:
            x.parent.right = y  # Define y como o novo filho direito do pai de x
        y.left = x  # Define x como o filho esquerdo de y
        x.parent = y  # Define y como o novo pai de x

    def right_rotate(self, x):
        """
        Realiza uma rotação para a direita em torno do nó 'x'.
        """
        y = x.left  # Armazena o filho esquerdo de x em y
        x.left = y.right  # Define o filho direito de y como o novo filho esquerdo de x
        if y.right != self.nil:  # Verifica se o filho direito de y não é o nó nil
            y.right.parent = x  # Define o pai do filho direito de y como x
        y.parent = x.parent  # Define o pai de y como o pai de x
        if x.parent == self.nil:  # Verifica se o pai de x é o nó nil (x é a raiz)
            self.root = y  # Define y como a nova raiz da árvore
        elif x == x.parent.right:  # Verifica se x é o filho direito de seu pai
            x.parent.right = y  # Define y como o novo filho direito do pai de x
        else:
            x.parent.left = y  # Define y como o novo filho esquerdo do pai de x
        y.right = x  # Define x como o filho direito de y
        x.parent = y  # Define y como o novo pai de x

    def insert_fixup(self, z):
        """
        Corrige quaisquer violações das propriedades da árvore Rubro-Negra após a inserção do nó 'z'.
        """
        while z.parent.color == "Red": # Enquanto a cor do pai de z for vermelha
            if z.parent == z.parent.parent.left: # Se o pai de z for o filho esquerdo do avô de z
                y = z.parent.parent.right # y recebe o irmão do pai de z
                if y.color == "Red": # Se a cor de y for vermelha
                    z.parent.color = "Black" # Define a cor do pai de z como preta
                    y.color = "Black" # Define a cor de y como preta
                    z.parent.parent.color = "Red" # Define a cor do avô de z como vermelha
                    z = z.parent.parent # Move z para o avô de z
                else: # Se a cor de y for preta                  
                    if z == z.parent.right: # Se z for o filho direito do pai de z               
                        z = z.parent # Move z para o pai de z                  
                        self.left_rotate(z) # Realiza uma rotação para a esquerda em torno de z                
                    z.parent.color = "Black" # Define a cor do pai de z como preta                   
                    z.parent.parent.color = "Red" # Define a cor do avô de z como vermelha                   
                    self.right_rotate(z.parent.parent) # Realiza uma rotação para a direita em torno do avô de z
            else: # Se o pai de z for o filho direito do avô de z        
                y = z.parent.parent.left # y recebe o irmão do pai de z     
                if y.color == "Red": # Se a cor de y for vermelha     
                    z.parent.color = "Black" # Define a cor do pai de z como preta        
                    y.color = "Black" # Define a cor de y como preta
                    z.parent.parent.color = "Red" # Define a cor do avô de z como vermelha
                    z = z.parent.parent # Move z para o avô de z
                else: # Se a cor de y for preta
                    if z == z.parent.left: # Se z for o filho esquerdo do pai de z
                        z = z.parent # Move z para o pai de z
                        self.right_rotate(z) # Realiza uma rotação para a direita em torno de z
                    z.parent.color = "Black" # Define a cor do pai de z como preta            
                    z.parent.parent.color = "Red" # Define a cor do avô de z como vermelha                  
                    self.left_rotate(z.parent.parent) # Realiza uma rotação para a esquerda em torno do avô de z
        self.root.color = "Black" # Define a cor da raiz como preta

    def insert(self, key):
        """
        Insere um novo nó com a chave 'key' na árvore, garantindo que não haja inserção de chaves duplicadas.
        """
        if self.search(key) != self.nil:  # Verifica se a chave já existe na árvore
            print(f"A chave {key} já existe na árvore. Inserção cancelada.")  # Informa ao usuário que a chave já existe
            return  # Retorna sem fazer a inserção

        z = Node(key)  # Cria um novo nó 'z' com a chave 'key'
        y = self.nil  # Inicializa 'y' como o nó nil
        x = self.root  # Inicializa 'x' como a raiz da árvore
        while x != self.nil:  # Enquanto 'x' não for o nó nil
            y = x  # Define 'y' como 'x'
            if z.key < x.key:  # Se a chave de 'z' for menor que a chave de 'x'
                x = x.left  # 'x' se move para o filho esquerdo
            else:
                x = x.right  # 'x' se move para o filho direito
        z.parent = y  # Define o pai de 'z' como 'y'
        if y == self.nil:  # Se 'y' for o nó nil (árvore vazia)
            self.root = z  # 'z' se torna a nova raiz da árvore
        elif z.key < y.key:  # Se a chave de 'z' for menor que a chave de 'y'
            y.left = z  # 'z' se torna o filho esquerdo de 'y'
        else:
            y.right = z  # 'z' se torna o filho direito de 'y'
        z.left = self.nil  # Define o filho esquerdo de 'z' como o nó nil
        z.right = self.nil  # Define o filho direito de 'z' como o nó nil
        z.color = "Red"  # Define a cor de 'z' como vermelha
        self.insert_fixup(z)  # Chama o método 'insert_fixup' para corrigir as propriedades da árvore Rubro-Negra após a inserção de 'z'

        def transplant(self, u, v):
            """
            Substitui a subárvore enraizada no nó 'u' pela subárvore enraizada no nó 'v'.
            """
            if u.parent == self.nil: # Verifica se o pai de u é o nó nil (u é a raiz)
                self.root = v  # Define v como a nova raiz da árvore
            elif u == u.parent.left: # Verifica se u é o filho esquerdo de seu pai
                u.parent.left = v  # Define v como o novo filho esquerdo do pai de u
            else:
                u.parent.right = v  # Define v como o novo filho direito do pai de u
            v.parent = u.parent  # Define o pai de v como o pai de u

    def delete_fixup(self, x):
        """
        Corrige quaisquer violações das propriedades da árvore Rubro-Negra após a remoção do nó 'x'.
        """
        while x != self.root and x.color == "Black":  # Enquanto x não for a raiz e a cor de x for preta
            if x == x.parent.left:  # Se x for o filho esquerdo de seu pai
                w = x.parent.right  # w recebe o irmão direito de x
                if w.color == "Red":  # Se a cor de w for vermelha
                    w.color = "Black"  # Define a cor de w como preta
                    x.parent.color = "Red"  # Define a cor do pai de x como vermelha
                    self.left_rotate(x.parent)  # Realiza uma rotação para a esquerda em torno do pai de x
                    w = x.parent.right  # Atualiza o valor de w para o novo irmão direito de x
                if w.left.color == "Black" and w.right.color == "Black":  # Se a cor do filho esquerdo de w e a cor do filho direito de w forem pretas
                    w.color = "Red"  # Define a cor de w como vermelha
                    x = x.parent  # Atualiza o valor de x para o pai de x
                else:
                    if w.right.color == "Black":  # Se a cor do filho direito de w for preta
                        w.left.color = "Black"  # Define a cor do filho esquerdo de w como preta
                        w.color = "Red"  # Define a cor de w como vermelha
                        self.right_rotate(w)  # Realiza uma rotação para a direita em torno de w
                        w = x.parent.right  # Atualiza o valor de w para o novo irmão direito de x
                    w.color = x.parent.color  # Define a cor de w como a cor do pai de x
                    x.parent.color = "Black"  # Define a cor do pai de x como preta
                    w.right.color = "Black"  # Define a cor do filho direito de w como preta
                    self.left_rotate(x.parent)  # Realiza uma rotação para a esquerda em torno do pai de x
                    x = self.root  # Atualiza o valor de x para a raiz da árvore
            else:
                w = x.parent.left  # w recebe o irmão esquerdo de x
                if w.color == "Red":  # Se a cor de w for vermelha
                    w.color = "Black"  # Define a cor de w como preta
                    x.parent.color = "Red"  # Define a cor do pai de x como vermelha
                    self.right_rotate(x.parent)  # Realiza uma rotação para a direita em torno do pai de x
                    w = x.parent.left  # Atualiza o valor de w para o novo irmão esquerdo de x
                if w.right.color == "Black" and w.left.color == "Black":  # Se a cor do filho direito de w e a cor do filho esquerdo de w forem pretas
                    w.color = "Red"  # Define a cor de w como vermelha
                    x = x.parent  # Atualiza o valor de x para o pai de x
                else:
                    if w.left.color == "Black":  # Se a cor do filho esquerdo de w for preta
                        w.right.color = "Black"  # Define a cor do filho direito de w como preta
                        w.color = "Red"  # Define a cor de w como vermelha
                        self.left_rotate(w)  # Realiza uma rotação para a esquerda em torno de w
                        w = x.parent.left  # Atualiza o valor de w para o novo irmão esquerdo de x
                    w.color = x.parent.color  # Define a cor de w como a cor do pai de x
                    x.parent.color = "Black"  # Define a cor do pai de x como preta
                    w.left.color = "Black"  # Define a cor do filho esquerdo de w como preta
                    self.right_rotate(x.parent)  # Realiza uma rotação para a direita em torno do pai de x
                    x = self.root  # Atualiza o valor de x para a raiz da árvore
        x.color = "Black"  # Define a cor de x como preta

    def minimum(self, x):
        """
        Retorna o nó com a menor chave na subárvore enraizada no nó 'x'.
        """
        while x.left != self.nil: # Enquanto existir um filho esquerdo de x que não seja o nó nil
            x = x.left  # Atualiza o valor de x para o filho esquerdo de x
        return x  # Retorna o nó com a menor chave na subárvore enraizada em x

    def remove(self, key):
        """
        Remove o nó com a chave 'key' da árvore.
        """
        z = self.search(key)  # Procura o nó com a chave 'key' na árvore
        if z == self.nil:  # Se o nó não for encontrado, retorna
            return
        y = z  # Define 'y' como 'z'
        y_original_color = y.color  # Armazena a cor original de 'y'
        if z.left == self.nil:  # Se o filho esquerdo de 'z' for o nó nil
            x = z.right  # Define 'x' como o filho direito de 'z'
            self.transplant(z, z.right)  # Substitui a subárvore enraizada em 'z' pela subárvore enraizada em 'z.right'
        elif z.right == self.nil:  # Se o filho direito de 'z' for o nó nil
            x = z.left  # Define 'x' como o filho esquerdo de 'z'
            self.transplant(z, z.left)  # Substitui a subárvore enraizada em 'z' pela subárvore enraizada em 'z.left'
        else:
            y = self.minimum(z.right)  # Encontra o nó com a menor chave na subárvore enraizada em 'z.right' e define 'y' como esse nó
            y_original_color = y.color  # Armazena a cor original de 'y'
            x = y.right  # Define 'x' como o filho direito de 'y'
            if y.parent == z:  # Se o pai de 'y' for 'z'
                x.parent = y  # Define o pai de 'x' como 'y'
            else:
                self.transplant(y, y.right)  # Substitui a subárvore enraizada em 'y' pela subárvore enraizada em 'y.right'
                y.right = z.right  # Define o filho direito de 'y' como o filho direito de 'z'
                y.right.parent = y  # Define o pai do filho direito de 'y' como 'y'
            self.transplant(z, y)  # Substitui a subárvore enraizada em 'z' pela subárvore enraizada em 'y'
            y.left = z.left  # Define o filho esquerdo de 'y' como o filho esquerdo de 'z'
            y.left.parent = y  # Define o pai do filho esquerdo de 'y' como 'y'
            y.color = z.color  # Define a cor de 'y' como a cor de 'z'
        if y_original_color == "Black":  # Se a cor original de 'y' for preta
            self.delete_fixup(x)  # Chama o método 'delete_fixup' para corrigir as propriedades da árvore Rubro-Negra após a remoção de 'x'

    def search(self, key):
        """
        Procura e retorna o nó com a chave 'key' na árvore.
        """
        x = self.root  # Inicializa 'x' como a raiz da árvore
        while x != self.nil and key != x.key:  # Enquanto 'x' não for o nó nil e a chave não for igual à chave de 'x'
            if key < x.key:  # Se a chave for menor que a chave de 'x'
                x = x.left  # 'x' se move para o filho esquerdo
            else:
                x = x.right  # 'x' se move para o filho direito
        return x  # Retorna o nó encontrado ou o nó nil se a chave não for encontrada

    def inorder(self, node):
        """
        Realiza um percurso em ordem na árvore, imprimindo as chaves dos nós e suas cores.
        """
        if node != self.nil:  # Verifica se o nó não é o nó nil
            self.inorder(node.left)  # Realiza um percurso em ordem no filho esquerdo do nó
            print(node.key, node.color)  # Imprime a chave e a cor do nó
            self.inorder(node.right)  # Realiza um percurso em ordem no filho direito do nó

    def check_balanced(self):
        """
        Verifica se a árvore está balanceada, garantindo que todos os caminhos da raiz até as folhas contenham o mesmo número de nós pretos.
        """
        if self.root == self.nil:  # Verifica se a raiz é o nó nil
            return True  # Retorna True se a árvore estiver vazia
        black_count = 0  # Contador para o número de nós pretos em um caminho da raiz até as folhas

        def is_balanced_util(node, black_count, current_count):
            if node.color == "Black":  # Verifica se o nó é preto
                current_count += 1  # Incrementa o contador de nós pretos no caminho atual
            if node == self.nil:  # Verifica se o nó é o nó nil
                if black_count == 0:  # Se o contador de nós pretos for zero
                    black_count = current_count  # Define o contador de nós pretos como o contador atual
                else:
                    if black_count != current_count:  # Se o contador de nós pretos for diferente do contador atual
                        return False  # Retorna False, pois os caminhos não têm o mesmo número de nós pretos
            if node.left != self.nil:  # Verifica se há um filho esquerdo do nó
                if not is_balanced_util(node.left, black_count, current_count):  # Chama recursivamente a função para o filho esquerdo
                    return False  # Retorna False se o filho esquerdo não estiver balanceado
            if node.right != self.nil:  # Verifica se há um filho direito do nó
                if not is_balanced_util(node.right, black_count, current_count):  # Chama recursivamente a função para o filho direito
                    return False  # Retorna False se o filho direito não estiver balanceado
            return True  # Retorna True se todos os caminhos da raiz até as folhas tiverem o mesmo número de nós pretos

        return is_balanced_util(self.root, black_count, 0)  # Chama a função auxiliar para verificar se a árvore está balanceada

def plot(tree):
    """
    Função para plotar a árvore Rubro-Negra usando o NetworkX e o Matplotlib.
    """
    # Cria um grafo direcionado
    G = nx.DiGraph()

    # Função para adicionar as arestas do grafo com base na árvore
    def add_edges(node):
        if node != tree.nil:  # Verifica se o nó não é um nó nil
            if node.left != tree.nil:
                # Adiciona uma aresta entre o nó e seu filho esquerdo
                G.add_edge(node.key, node.left.key)
                # Chama recursivamente a função para o filho esquerdo
                add_edges(node.left)
            if node.right != tree.nil:
                # Adiciona uma aresta entre o nó e seu filho direito
                G.add_edge(node.key, node.right.key)
                # Chama recursivamente a função para o filho direito
                add_edges(node.right)

    # Chama a função add_edges para adicionar todas as arestas da árvore ao grafo
    add_edges(tree.root)

    # Função para calcular a altura máxima da árvore
    def max_depth(node):
        if node == tree.nil:  # Se o nó for nil, a altura é 0
            return 0
        # Retorna a altura máxima entre o filho esquerdo e o filho direito, mais 1
        return max(max_depth(node.left), max_depth(node.right)) + 1

    # Calcula a altura máxima da árvore
    max_height = max_depth(tree.root)

    # Calcula a posição de cada nó com base em sua profundidade na árvore
    pos = {}  # Dicionário para armazenar as posições dos nós
    depth = {tree.nil: 0}  # Dicionário para armazenar as profundidades dos nós

    def compute_position(node, x=0, y=0, level=1):
        if node != tree.nil:  # Verifica se o nó não é um nó nil
            if level not in depth:
                depth[level] = 0
            # Define a posição do nó com base em sua profundidade
            pos[node.key] = (x, -y)
            depth[level] += 1
            # Calcula o deslocamento horizontal com base na altura máxima e no nível atual
            dx = 2 ** (max_height - level + 1)
            # Chama recursivamente a função para os filhos esquerdo e direito
            compute_position(node.left, x - dx, y + 1, level + 1)
            compute_position(node.right, x + dx, y + 1, level + 1)

    # Calcula as posições dos nós na árvore
    compute_position(tree.root)

    # Função para obter a cor de um nó da árvore
    def get_node_color(node):
        if node.color == "Red":  # Se o nó for vermelho, retorna "red"
            return "red"
        else:
            return "black"  # Caso contrário, retorna "black"

    # Lista para armazenar as cores dos nós da árvore
    node_colors = []

    # Função para coletar as cores dos nós da árvore
    def collect_node_colors(node):
        if node != tree.nil:  # Verifica se o nó não é um nó nil
            # Adiciona a cor do nó à lista de cores
            node_colors.append(get_node_color(node))
            # Chama recursivamente a função para os filhos esquerdo e direito
            collect_node_colors(node.left)
            collect_node_colors(node.right)

    # Coleta as cores dos nós da árvore
    collect_node_colors(tree.root)

    # Tamanho dos nós na plotagem
    node_size = 500
    # Cor das bordas dos nós na plotagem
    node_edge_color = "black"
    # Plota a árvore usando o NetworkX
    nx.draw_networkx(G, pos, node_size=node_size, with_labels=True, font_color='white', edgecolors=node_edge_color, node_color=node_colors)
    # Define o título da plotagem
    plt.title("Árvore Rubro-Negra")
    # Exibe a plotagem
    plt.show()

def interface():
    """
    Função para interagir com a árvore Rubro-Negra, permitindo ao usuário inserir e remover nós, verificar se a árvore está balanceada e plotar a árvore.
    """
    rb_tree = RedBlackTree()  # Cria uma nova instância da classe RedBlackTree
    while True:  # Loop infinito
        print("\nÁrvore Rubro-Negra:")
        rb_tree.inorder(rb_tree.root)  # Realiza um percurso em ordem na árvore e imprime as chaves e cores dos nós
        print("\n1 - Inserir nó")
        print("2 - Remover nó")
        print("3 - Verificar se a árvore está balanceada")
        print("4 - Plotar a árvore Rubro-Negra")
        print("5 - Sair")
        option = input("Escolha uma opção: ")  # Solicita ao usuário que escolha uma opção
        if option == "1":  # Se a opção escolhida for inserir um nó
            key = int(input("Digite a chave do nó a ser inserido: "))  # Solicita ao usuário que digite a chave do nó a ser inserido
            rb_tree.insert(key)  # Insere o nó com a chave digitada na árvore
        elif option == "2":  # Se a opção escolhida for remover um nó
            key = int(input("Digite a chave do nó a ser removido: "))  # Solicita ao usuário que digite a chave do nó a ser removido
            rb_tree.remove(key)  # Remove o nó com a chave digitada da árvore
        elif option == "3":  # Se a opção escolhida for verificar se a árvore está balanceada
            print("A árvore está balanceada:", rb_tree.check_balanced())  # Verifica se a árvore está balanceada e imprime o resultado
        elif option == "4":  # Se a opção escolhida for plotar a árvore Rubro-Negra
            plot(rb_tree)  # Chama a função para plotar a árvore
        elif option == "5":  # Se a opção escolhida for sair
            break  # Sai do loop
        else:
            print("Opção inválida. Tente novamente.")  # Imprime uma mensagem de erro se a opção escolhida for inválida

interface()  # Chama a função 'interface' para iniciar a interação com a árvore Rubro-Negra