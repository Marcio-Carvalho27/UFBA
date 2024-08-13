class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data

class Queue():
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        return self.head == None
    
    def append(self, node):
        if not self.is_empty():
            aux = self.head
            while aux.next:
                aux = aux.next
            aux.next = node
        else:
            self.head = node

        self.size += 1

    def pop(self):
        if not self.is_empty():
            self.head = self.head.next
            self.size -= 1

def main():
    queue = Queue()
    #in
    operations, max = [int(x) for x in input().split()]

    #run
    for n in range(operations):
        case1, case2 = input().split()

        if case1 == "A":
            if max > queue.size:
                queue.append(Node(case2))

        elif case1 == "F":
            for _ in range(int(case2)):
                print(queue.head.get_data())
                queue.pop()

        elif case1 == "M":
            max = int(case2)

main()