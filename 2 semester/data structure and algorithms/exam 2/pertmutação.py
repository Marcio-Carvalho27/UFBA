class Element():
    def __init__(self, key):
        self.key = key
        self.next = None

    def getKey(self):
        return self.key

class Line():
    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head:
            aux = self.head
            while aux.next:
                aux = aux.next
            aux.next = node
        else:
            self.head = node

    def pop(self):
        if self.head:
            aux = self.head
            self.head = aux.next
            return aux

    def out(self):
        if self.head:
            aux = self.head
            while aux:
                print(aux.getKey())
                aux = aux.next

class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class Heap():
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, node):
        self.size += 1
        if self.root is None:
            self.root = node
        else:
            self.insert_subtree(self.root, node)

    def fix(self, node):
        if node.parent:
            if node.parent.key > node.key:
                aux = node.parent.key
                node.parent.key = node.key
                node.key = aux
                self.fix(node.parent)

    def insert_subtree(self, base, node):
        line = Line()
        line.append(Element(base))
        while line.head:
            aux = line.pop().key
            if aux.left:
                line.append(Element(aux.left))
                if aux.right:
                    line.append(Element(aux.right))
                else:
                    aux.right = node
                    node.parent = aux
                    self.fix(node)
                    line.head = None
            else:
                aux.left = node
                node.parent = aux
                self.fix(node)
                line.head = None

    def out(self):
        line = Line()
        if self.root:
            line.append(Element(self.root))
            while line.head:
                aux = line.pop().key
                print(aux.key)
                if aux.left:
                    line.append(Element(aux.left))
                if aux.right:
                    line.append(Element(aux.right))

    def pop(self):
        if self.root is None:
            return None  # The heap is empty

        # Remove the root
        removed_root = self.root

        if self.size == 1:
            self.root = None
            self.size -= 1
            return removed_root

        # Get the last node
        last_node = self.get_last_node()

        # Replace the root with the last node
        self.root.key = last_node.key

        # Remove the last node
        if last_node.parent.left == last_node:
            last_node.parent.left = None
        else:
            last_node.parent.right = None
        
        self.size -= 1

        # Restore the heap property
        self.heapify(self.root)
        
        return removed_root

    def get_last_node(self):
        if not self.root:
            return None
        
        # Level order traversal to find the last node
        line = Line()
        line.append(Element(self.root))
        last_node = None
        
        while line.head:
            last_node = line.pop().key
            if last_node.left:
                line.append(Element(last_node.left))
            if last_node.right:
                line.append(Element(last_node.right))
        
        return last_node

    def heapify(self, node):
        smallest = node
        if node.left and node.left.key < smallest.key:
            smallest = node.left
        if node.right and node.right.key < smallest.key:
            smallest = node.right
        
        if smallest != node:
            # Swap keys
            node.key, smallest.key = smallest.key, node.key
            # Recursively heapify the affected subtree
            self.heapify(smallest)

def main():
  heap = Heap()

  N, K = input().split(" ")

  N = int(N)
  K = int(K)

  aux = input().split(" ")

  for n in range(N):
    if heap.size < K:
        heap.insert(Node(int(aux[n])))
    else:
        if int(aux[n]) > heap.root.key:
            heap.pop()
            heap.insert(Node(int(aux[n])))
    if n >= K-1:
      print(heap.root.key)
  
main()