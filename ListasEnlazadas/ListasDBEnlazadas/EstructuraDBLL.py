# Aqui se encontrara la estructura de las listas doblemente enlazadas, con sus respectivas funciones para agregar, eliminar, buscar, etc.
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    @property
    def data(self):
        return self.__data
    
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, new_next):
        if new_next is not None and not isinstance(new_next, Node):
            raise TypeError("El siguiente Valor debe ser un objeto de tipo Node o None.")
        self.__next = new_next

    @property
    def prev(self):
        return self.__prev
    
    @prev.setter
    def prev(self, new_prev):
        if new_prev is not None and not isinstance(new_prev, Node):
            raise TypeError("El anterior Valor debe ser un objeto de tipo Node o None.")
        self.__prev = new_prev

    @data.setter
    def data(self, new_data):
        if new_data is None:
            raise TypeError("El valor de data debe ser un número o una cadena.")
        self.__data = new_data

class DoubleLinkedList:

    __slots__=['__head', '__size', '__tail']
    def __init__(self):
        self.__head=None
        self.__size=0
        self.__tail=None

    @property
    def head(self):
        return self.__head
    
    @property
    def size(self): 
        return self.__size
    
    @property
    def tail(self):
        return self.__tail
    
    @head.setter
    def head(self, new_head):
        if new_head is not None and not isinstance(new_head, Node):
            raise TypeError("El valor de head debe ser un objeto de tipo Node o None.")
        self.__head = new_head

    @tail.setter
    def tail(self, new_tail):
        if new_tail is not None and not isinstance(new_tail, Node):
            raise TypeError("El valor de tail debe ser un objeto de tipo Node o None.")
        self.__tail = new_tail

    def __iter__(self):
        current_node=self.__head
        while current_node is not None:
            yield current_node.data
            current_node=current_node.next

    def __str__(self):
        result = [str(node) for node in self]
        return " <---> ".join(result)
    
    def prepend(self, new_data):
        new_node = Node(new_data)
        if self.__head is None: 
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head.prev = new_node
            self.__head = new_node
        self.__size += 1

    def append(self, new_data):
        new_node=Node(new_data)
        if self.__tail is None:
            self.__head=new_node
            self.__tail=new_node
        else:
            self.__tail.next=new_node
            new_node.prev = self.__tail
            self.__tail=new_node
        self.__size += 1

    def get_by_index(self, index):
        if index < -1 or index > self.__size - 1:
            raise ValueError("Índice fuera de rango.")
        
        if index == -1:
            return self.__tail
        
        current_index = 0
        current_node = self.__head

        while current_node is not None:
            if index == current_index:
                return current_node
            
            current_index += 1
            current_node = current_node.next

    def insert_at_index(self,index, new_data):
        if index < -1 or index > self.__size - 1:
            raise ValueError("Índice fuera de rango.")
        
        if index == 0:
            self.prepend(new_data)
            
        elif index == -1 or index == self.__size:
            self.append(new_data)

        else:
            new_node = Node(new_data)
            prev_node = self.get_by_index(index - 1)
            next_node = prev_node.next
            new_node.next = next_node
            new_node.prev = prev_node
            prev_node.next = new_node
            if next_node:
                next_node.prev = new_node
            self.__size += 1
        
    def search_value(self, value):
        for current_node in self:
            if current_node == value:
                return True
        return False

    #def set_new_value(self, new_data):

    def remove_first(self):
        if self.__head is None:
            print("La lista está vacía.")
            return None
        
        if self.__size == 1:
            removed_node = self.__head
            self.__head = None
            self.__tail = None
            self.__size -= 1
            return removed_node
        
        else:
            removed_node = self.__head
            self.__head = self.__head.next
            self.__head.prev = None
            self.__size -= 1
            removed_node.next = None
            return removed_node
        
    def remove_last(self):
        if self.head is None:
            print("La lista está vacía.")
            return None
        if self.__size == 1:
            removed_node = self.__head
            self.__head = None
            self.__tail = None
            self.__size -= 1
            return removed_node
        else:
            removed_node = self.__tail
            self.__tail = self.__tail.prev
            self.__tail.next = None
            self.__size -= 1
            removed_node.prev = None
            return removed_node
        
    def clear(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    print("Lista después de append:", dll)
    dll.prepend(0)
    print("Lista después de prepend:", dll)
    dll.insert_at_index(2, 1.5)
    print("Lista después de insertar en índice 2:", dll)
    dll.remove_first()
    print("Lista después de remove_first:", dll)
    dll.remove_last()
    print("Lista después de remove_last:", dll)
    print("Tamaño:", dll.size)