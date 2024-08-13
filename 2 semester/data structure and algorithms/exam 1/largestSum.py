import numpy as np

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data
    
class List:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def free_list(self):
        self.head = None

    def append(self, node):
        if not self.is_empty():
            aux = self.head
            while aux.next:
                aux = aux.next
            aux.next = node
        else:
            self.head = node

    def insert(self, node, position):
        if not position == 0:
            count = 0
            aux = self.head
            while count < position - 1 and aux:
                aux = aux.next
                count += 1
            node.next = aux.next
            aux.next = node
        else:
            node.next = self.head
            self.head = node

    def remove(self):
        if not self.is_empty():
            aux = self.head
            self.head = self.head.next

    def display(self):
        aux = self.head
        while aux:
            print(f"{aux.get_data()} ", end="")
            aux = aux.next

    def get(self, position):
        count = 0
        aux = self.head
        while aux:
            if count == position:
                return aux.get_data()
            aux  = aux.next
            count += 1

def main():
    list = List()

    #in
    size = int(input())
    list_n = np.fromstring(input(),dtype=int, sep=' ')

    #run
    for n in range(size):

        #creat list
        if list.is_empty():
            list.head = Node(list_n[0])
            aux_creat = list.head
        else:
            aux_creat.next = Node(list_n[n])
            aux_creat = aux_creat.next
        #find the largest sublist
        if n == 0:
            max_sum = aux = list.head.get_data()
            list_aux = list.head 
        else:
            list_aux = list_aux.next
            node_value = list_aux.get_data()
            if node_value >= aux + node_value:
                aux = node_value
            else:
                aux += node_value

            if max_sum < aux:
                max_sum = aux

    #out
    return max_sum


print(main())