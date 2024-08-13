class Node:
    def __init__(self, data):
        self.data = data
        self.before = None
    
    def get_data(self):
        return self.data
    
class Stack:
    def __init__(self):
        self.botton = None
        self.size = 0
        self.buffer = 0

    def is_empty(self):
        return self.botton == None

    def append(self, node):
        if not self.is_empty():
            node.before = self.botton
            self.botton = node
            self.buffer *= node.get_data()
        else:
            self.botton = node
            self.buffer = node.get_data()
        
        
        self.size += 1
    
    def pop(self):
        if not self.is_empty():
            if self.size > 1:
                aux = self.botton
                self.botton = aux.before

                self.buffer = self.buffer // aux.get_data()

            elif self.size == 1:
                self.botton = None
                self.buffer = 0

            self.size -= 1
            

def add_on_for(stack):
    if not stack.is_empty():
        if stack.size > 1:
            return stack.buffer
        elif stack.size == 1:
            return stack.botton.get_data()


def main():
    #variables
    buffer = 0
    stack = Stack()

    #in
    N, K = [int(x) for x in input().split()]

    #process + in
    for _ in range(N):
        aux = input()
        if aux == "ADD":
            if stack.size == 0:
                buffer += 1
            else:
                buffer += add_on_for(stack) 
        elif aux == "END":
            stack.pop()
        else:
            _, loop = aux.split()
            stack.append(Node(int(loop)))
    
    #out
    if buffer > K:
        print("OVERFLOW")
    else:
        print(buffer)
    
main()