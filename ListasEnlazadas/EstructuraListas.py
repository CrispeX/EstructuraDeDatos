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
    









node1 = Node(10)
node2 = Node(20)

print(node1)
print(node2)
node1.next = node2