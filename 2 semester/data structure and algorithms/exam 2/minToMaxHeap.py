class Element:
    def __init__(self, key):
        self.key = key

        self.next = None
        self.before = None

    def getKey(self):
        return self.key

class Line:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def append(self, node):
        node = Element(node)
        self.size += 1

        if self.head:
            node.before = self.tail
            self.tail.next = node
        else:
            self.haed = node
        
        self.tail = node

    def pop(self):
        if self.head:
            self.size -= 1

            aux = self.head
            self.head = aux.next
            return aux.getKey()
        
    def out(self):
        buffer = 1
        aux = 1

        while aux <= (self.size + 1):
            if 2**buffer == aux:
                buffer += 1
                print("")
            
            print(f"{self.head.getKey().getKey()}", end=" ")

            if not self.head.next:
                self.head = self.head.next
            
            aux += 1

        print("")

class Node:
    def __init__(self, key):
        self.key = key

        self.left = None
        self.right = None
        self.parent = None

        self.locate = 1

    def getKey(self):
        return self.key

class Heap:
    def __init__(self):
        self.root = None
        self.last = None

        self.size = 0

    def insert(self, node):
        node = Node(node)
        self.size += 1

        if self.root:
            self.insert_Subtree(self.root, node)
        else:
            self.last = node
            self.root = node
            node.locate = self.size

    def insert_Subtree(self, base, node):
        line = Line()
        line.append(base)

        while line.head:
            aux = line.pop()
            if aux.left:
                line.append(aux.left)
                if aux.right:
                    line.append(aux.right)
                else:
                    aux.right = node
                    node.parent = aux
                    node.locate = self.size
                    self.last = node
                    self.fix_up(aux.right)
                    line.head = None
            else:
                aux.left = node
                node.parent = aux
                node.locate = self.size
                self.fix_up(aux.left)
                line.head = None

    def fix_up(self, base):
        if base.parent:
            if base.parent.getKey() >= base.getKey():
                aux = base.getKey()
                base.key = base.parent.getKey()
                base.parent.key = aux
                self.fix_up(base.parent)
        else:
            self.root = base
    
    def fix_down(self, base, select):
        if base.left and base.right:
            if select == "min":
                if base.left.getKey() < base.right.getKey():
                    if base.left.getKey() < base.getKey():
                        aux = base.getKey()
                        base.key = base.left.getKey()
                        base.left.key = aux
                        self.fix_down(base.left, "min")
                else:
                    if base.right.getKey() < base.getKey():
                        aux = base.getKey()
                        base.key = base.right.getKey()
                        base.left.key = aux
                        self.fix_down(base.left, "min")
        
            elif select == "max":
                if base.left.getKey() > base.right.getKey():
                    if base.left.getKey() > base.getKey():
                        aux = base.getKey()
                        base.key = base.left.getKey()
                        base.left.key = aux
                        self.fix_down(base.left, "max")
                else:
                    if base.right.getKey() > base.getKey():
                        aux = base.getKey()
                        base.key = base.right.getKey()
                        base.left.key = aux
                        self.fix_down(base.left, "max")

        elif base.left and not base.right:
            if select == "min":
                if base.left.getKey() < base.getKey():
                    aux = base.getKey()
                    base.key = base.left.getKey()
                    base.left.key = aux
                    self.fix_down(base.left, "min")
            elif select == "max":
                if base.left.getKey() > base.getKey():
                    aux = base.getKey()
                    base.key = base.left.getKey()
                    base.left.key = aux
                    self.fix_down(base.left, "max")

    def find_last(self, base):
        if base:
            if base.locate == self.size:
                return base
            else:
                self.find_last(base.right)
                self.find_last(base.left)

    def min_to_max(self):
        auxline = Line()
        line = Line()

        auxline.append(self.root)
        while auxline.head:
            aux = auxline.pop()
            line.append(aux)

            if aux.left:
                auxline.append(aux.left)
                if aux.right:
                    auxline.append(aux.right)
        
        aux = line.head
        if line.size > 1:
            while aux.next.key.left:
                aux = aux.next
            while aux:
                self.fix_down(aux.key, "max")
                aux = aux.before

        auxline = Line()
        line = Line()

        auxline.append(self.root)
        while auxline.head:
            aux = auxline.pop()
            line.append(aux)

            if aux.left:
                auxline.append(aux.left)
                if aux.right:
                    auxline.append(aux.right)
        
        return line

    def pop(self):
        aux = self.root.getKey()
        last = self.last

        if self.size > 1:
            if last.parent.right == last:
                last.parent.right = None
            else:
                last.parent.left = None

            if self.root.right:
                last.right = self.root.right
                self.right.parent = last
            if self.root.left:
                last.left = self.root.left
                self.left.parent = last

            
            self.last.parent = None
            self.locate = 1

            self.fix_down(self.root, "min")

            self.size -= 1
            self.last = self.find_last(self.root)

        elif self.size == 1:
            self.root = None
            self.last = None

            self.size -= 1

        return aux
    
def main():
    heap = Heap()
    line = Line()
    N = int(input())

    for _ in range(N):
        C, I = input().split(" ")
        I = int(I)

        if C == "I":
            heap.insert(I)
        else:
            for _ in range(I):
                print(f"{heap.pop()}", end=" ")
            print()

    line = heap.min_to_max()
    line.out(line.head)

main()
    