from typing import Optional




# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode() # inicialize one node
        tail = dummy_node

        """
        Iteramos sobre los nodos de ambas listas (list1 y list2 solo son los nodos iniciales)
        Agregamos a nuestra linked list el menor nodo de ambas listas
        No nos saltamos posiciones de ninguno
        (Osea si el nodo0 de lista1 es menor que el nodo0 de lista2, 
        Se agrega a dummy el nodo0 de lista1 pero en la siguiente iteracion compararemos
        el nodo1 de lista1 con el nodo0 de lista2)

        Luego de agregar a dummy (tail) el nodo menor pasamos con next al siguiente nodo de la lista agregada
        Luego vamos el siguiente nodo de la tail para la siguiente iteracion.
        """


        while list1 and list2: #Mientras ambas tengan elementos
            
            if list1.val < list2.val: #Ver el menor valor de ambos nodos
                print(232)
                tail.next = list1       # Asignar a nuestra lista dummy el siguiente nodo (el menor)
                list1 = list1.next      # Ir al siguiente nodo de la lista1
            
            else:                       #Ver el menor valor de ambos nodos
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next 

        
        if list1 and not list2: # Si list2 no tiene mas elementos solo agregar los de list2
            tail.next = list1
        
        elif not list1 and list2: # Si list1 no tiene mas elementos solo agregar los de list1
            tail.next = list2


        return dummy_node.next





def create_linked_list(values):
    """Create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def print_linked_list(head):
    """Print a linked list as a list of values."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)
      
            

list1 = ListNode([1,2,4])
list2 = ListNode([1,3,4])


list1_values = [1, 2, 4]  
list2_values = [1, 3, 4]  


list1 = create_linked_list(list1_values)
list2 = create_linked_list(list2_values)


solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)


print_linked_list(merged_list)
