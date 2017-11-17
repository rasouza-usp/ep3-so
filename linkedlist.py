class Node(object):

    def __init__(self, data, inicio, tamanho, next_node):
        self.data = data           # L se eh um noh livre e P se tem processo
        self.inicio = int(inicio)       # Em que posicao comeca
        self.tamanho = int(tamanho)     # Tamanho ocupado
        self.next_node = next_node # Proximo noh
        self.previous_node = None #No anterior

    def get_data(self):
        return self.data
        
    def get_inicio(self):
        return self.inicio
        
    def get_tamanho(self):
        return self.tamanho
        
    def get_next(self):
        return self.next_node
        
    def get_previous(self):
        return self.previous_node

    def set_data(self, data):
        self.data = data
    
    def set_inicio(self, inicio):
        self.inicio = inicio
        
    def set_tamanho(self, tam):
        self.tamanho = tam
        
    def set_previous(self, new_previous):
        self.previous_node = new_previous
        
    def set_next(self, new_next):
        self.next_node = new_next
        
    def show(self):
        print "Data: =", self.data, "| Inicio =", self.inicio, "| Tamanho =", self.tamanho, "\n"

class LinkedList(object):
    #Inicia uma lista ligada com 1 unico noh do tamanho total disponivel
    def __init__(self, data, inicio, tamanho, next_node=None):
        new_node = Node(data, inicio, tamanho, next_node=None)
        self.head = new_node

	#insere um elemento na lista : Parece errado!!!
    def insert(self, data, inicio, tamanho, next_node=None):
        new_node = Node(data, inicio, tamanho, next_node=None)
        new_node.set_next(self.head)
        self.head = new_node
        
    def get_head(self):
        return self.head

    def set_head(self, node):
        self.head = node
    
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            print count 
            current = current.get_next()
        return count
       
    #mostra a lista ligada inteira 
    def show(self):
        current = self.head
        while current:
            print "Data: =", current.data, "| Inicio =", current.inicio, "| Tamanho =", current.tamanho, "\n"
            current = current.get_next()

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current
        
    #atualizar os tamanho no caso de dois espacos livres seguidos
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
