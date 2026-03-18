import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from EstructuraDBLL import NodeD
from EstructuraDBLL import DoublyLinkedList

#Remover posicions pares de una lista doblemente enlazada, es decir, remover el primer nodo, el tercer nodo, el quinto nodo, etc. Devolver la nueva cabeza de la lista.
def remove_even_positions(l1):
    
    index = 0
    cur_node = l1.head
    
    while cur_node:

        next_node = cur_node.next
        print("next_node", next_node)

        if index % 2 == 0:
            if cur_node == l1.head:
                new_head = cur_node.next
                new_head.prev = None
            else:
                prev_node = cur_node.prev
                prev_node.next = next_node

                if next_node:
                    next_node.prev = prev_node
                
                cur_node.prev = None
                cur_node.next = None
            l1.size -= 1
        cur_node = next_node
        index += 1
    return new_head

#Historial de navegación
class BrowserHistory:
    def __init__(self, homepage: str):
        self.historial = DoublyLinkedList()
        self.historial.append(homepage)
        self.current = self.historial.head
    
    def __str__(self):
        result = []
        for nodo in self.historial:
            if nodo == self.current:
                result.append(f"[{nodo.value}]")
            else:                
                result.append(nodo.value)
        return ' <--> '.join(result)

    def visit(self, new_website: str) -> None:
        if self.current.next:
            self.current.next = None
            self.historial.tail = self.current
            self.historial.append(new_website)
        self.current = self.historial.tail

    def delete_page(self, website: str) -> None:
        while website:
            self.next_page = self.current.next
            cur_page_prev = None
            cur_page_next = None

            self.historial_size.size -= 1

            cur_page = self.next_page
    
    def reverse(self, steps: int) -> str:
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.value

    def next_page(self, steps: int) -> str:
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.value