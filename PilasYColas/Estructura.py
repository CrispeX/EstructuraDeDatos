# Estructura de datos para pilas y colas
import random

class Node:
  __slots__ = ('__value','__next')

  def __init__(self,value):
    self.__value = value
    self.__next = None

  def __str__(self):
    return str(self.__value)

  @property
  def next(self):
    return self.__next

  @next.setter
  def next(self,node):
    if node is not None and not isinstance(node,Node):
      raise TypeError("next debe ser un objeto tipo nodo ó None")
    self.__next = node

  @property
  def value(self):
    return self.__value

  @value.setter
  def value(self,newValue):
    if newValue is None:
      raise TypeError("el nuevo valor debe ser diferente de None")
    self.__value = newValue

class LinkedList:

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

  @head.setter
  def head(self,node):
    if node is not None and not isinstance(node,Node):
      raise TypeError("Head debe ser un objeto tipo nodo ó None")
    self.__head = node

  @tail.setter
  def tail(self,node):
    if node is not None and not isinstance(node,Node):
      raise TypeError("Tail debe ser un objeto tipo nodo ó None")
    self.__tail = node

  @size.setter
  def size(self,num):
    self.__size = num

  def __str__(self):
    result = [str(nodo.value) for nodo in self]
    return ' <--> '.join(result)

  def print(self):
    for nodo in self:
      print(str(nodo.value))

  def __iter__(self):
    current = self.__head
    while current is not None:
      yield current
      current = current.next

  def append(self,value): # Adicionar al final
    newnode = Node(value)
    if self.__head is None:
      self.__head = newnode
      self.__tail = newnode
    else:
      self.__tail.next = newnode #enlazo nuevo nodo
      self.__tail = newnode
    self.__size += 1


  def popfirst(self):
    tempNode = self.__head
    if self.__head is None:
      return False
    elif self.__size == 1:
      self.__head = None
      self.__tail = None
      self.__size = 0
    else:
      self.__head = self.__head.next
      self.__size -= 1

    tempNode.next = None  #limpiar la referencia al segundo nodo, ahora nueva cabeza
    return tempNode

class ColaNodo:
  __slots__ = ('dato','next')

  def __init__(self, dato):
    self.dato = dato
    self.next = None


class Queue:

  def __init__(self):
    self.head = None
    self.tail = None
    self._size = 0

  def encolar(self, elemento):
    nodo = ColaNodo(elemento)
    if self.tail is None: 
      self.head = nodo
      self.tail = nodo
    else:
      self.tail.next = nodo
      self.tail = nodo
    self._size += 1

  def desencolar(self):
    if self.head is None:
      return None
    nodo = self.head
    self.head = nodo.next
    if self.head is None:
      self.tail = None
    self._size -= 1
    return nodo.dato

  def esta_vacia(self):
    return self._size == 0

  def tamano(self):
    return self._size

  
  def enqueue(self, e):
    return self.encolar(e)

  def dequeue(self):
    return self.desencolar()

  def is_empty(self):
    return self.esta_vacia()

  def len(self):
    return self.tamano()

  def __str__(self):
    result = []
    current = self.head
    while current is not None:
      result.append(str(current.dato))
      current = current.next
    return ' -- '.join(result)
