# Aqui se encontrara la estructura de las listas enlazadas, con sus respectivas funciones para agregar, eliminar, buscar, etc.
class Node:
    
    __slots__ = ("__value", "__next")
    def __init__(self, value):
        
        self.__value = value
        self.__next = None
    
    @property
    def value(self):
        return self.__value

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, new_next):
        if new_next is not None and not isinstance(new_next, Node):
            raise TypeError("El siguiente nodo debe ser una instancia de Node o None")
        self.__next = new_next

    @value.setter
    def value(self, new_value):
        if new_value is None:
            raise ValueError("El valor del nodo no puede ser null o None")
        self.__value = new_value
    
    def __str__(self):
        return str(self.__value)

class LinkedList:
    
    __slots__ = ("__head", "__tail", "__size")
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    @property
    def head(self):
        return self.__head
    
    @property
    def tail(self):
        return self.__tail
    
    @property
    def size(self):
        return self.__size
    
    def __iter__(self):
        current_node = self.__head
        while current_node is not None:
            yield current_node
            current_node = current_node.next

    def __str__(self):
        result = [str(node) for node in self]
        return ' --> '.join(result)
    
    def prepend(self, new_value):
        new_node = Node(new_value)

        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node

            
        else:
            new_node.next = self.__head
            self.__head = new_node

        self.__size += 1

        def append(self, new_value):
            new_node = Node(new_value)

            if self.__head is None:
                self.__head = new_node
                self.__tail = new_node

                
            else:
                self.__tail.next = new_node
                self.__tail = new_node

            self.__size += 1

customLL = LinkedList()
customLL.prepend(50)
print("Despues del primer prepend", customLL)
print("customLL.head --> ", customLL.head)
print("customLL.tail --> ", customLL.tail)





node1 = Node(10)
node2 = Node(20)

print(node1)
print(node2)
node1.next = node2