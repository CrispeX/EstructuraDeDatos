from .EstructuraListas import Node
from .EstructuraListas import LinkedList
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