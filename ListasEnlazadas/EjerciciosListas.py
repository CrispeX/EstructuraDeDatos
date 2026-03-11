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

