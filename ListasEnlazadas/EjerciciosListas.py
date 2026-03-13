from .EstructuraListas import Node
from .EstructuraListas import LinkedList
import random
#Reversar una lista enlazada sin utilizar estructuras auxiliares

def reversedL(l1):

    prev_node = None
    current_node = l1.head

    while current_node:
        next_node = current_node.next
        current_node.next = prev_node

        #Para la siguiente iteracion
        prev_node = current_node
        current_node = next_node
    
    return l1.tail, l1.head

def reorderbyposition(l1):

    odd_node = l1.head
    even_node = l1.head.next

    head_even_nodes = even_node

    while even_node:
        
        print("odd none : ", odd_node)
        print("even none: "), even_node
        print("even_node.next :", odd_node.next)
        odd_node.next = even_node.next
        odd_node = odd_node.next

        even_node.next = odd_node.next
        
        if even_node.next is None:
            new_tail = even_node
        even_node = even_node.next

        odd_node.next = head_even_nodes

# Cree una funcion que reciba dos listas enlazadas y determine si las dos listas se interceptan, la funcion debe retornar el nodo
# de interseccion.

def add_same_nodes(l1, l2, num, min, max):

    for _ in range(num):
        new_node = Node(random.randint(min, max))

        l1.tail.next = new_node
        l1.tail = new_node
        l1.size += 1
        
        l2.tail.next = new_node
        l2.tail = new_node
        l2.size += 1
    
def search_intersention_nodes(l1, l2):

    if l1.tail is not l2.tail:
        return "Las listas no se intersectan"
    
    longesll = l1 if l1.size > l2.size else l2
    shortesll = l2 if l1.size > l2.size else l1

    print("longesll: ", longesll)
    print("shortesll: ", shortesll)

    dif = longesll.siza - shortesll.size

    currentll = longesll.head
    currentl = shortesll.head

    print("Currentll: ", currentll)
    print("Currentl: ", currentl)

    for _ in range(dif):
        currentll = currentll.next
    
    while currentll is not currentl:
        currentll = currentll.next
        currentl = currentl.next
    
# Cree una funcion que reciba dos listas enlazadas representandos numeros. Devuelva unas lista enlazada representando la suma de los numeros

def sumll(l1, l2):

    result = LinkedList()
    carry = 0

    currentl1 = l1.head
    currentl2 = l2.head

    while currentl1 or currentl2:
        
        sum = int(currentl1.value) + int(currentl2.value) + carry
        result.append(sum % 10)
        carry = sum // 10
        currentl1 = currentl1.next
        currentl2 = currentl2.next

    result.append(carry) if carry > 0 else None
    
    return result