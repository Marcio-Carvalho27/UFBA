class Node:
    def __init__(self, pos):
        self.pos = pos
        self.children = []

class Tree:
    def __init__(self):
        self.nodes = {}
        self.root = None

    def insert(self, boss, pos):
        if pos not in self.nodes:
            self.nodes[pos] = Node(pos)
        if boss not in self.nodes:
            self.nodes[boss] = Node(boss)
        
        self.nodes[boss].children.append(self.nodes[pos])
        
        if self.root is None:
            self.root = self.nodes[1]

    def dfs(self, node):
        count = 0
        for child in node.children:
            count += self.dfs(child) + 1
        return count

    def count_subordinates(self):
        
        subordinate_counts = {}
        for pos in self.nodes:
            subordinate_counts[pos] = self.dfs(self.nodes[pos])
        return subordinate_counts

def main():

    n = int(input())
    
    tree = Tree()
    

    bossitions = list(map(int, input().strip().split()))
    for i, boss in enumerate(bossitions, start=2):
        tree.insert(boss, i)
    

    subordinate_counts = tree.count_subordinates()

    print(' '.join(str(subordinate_counts.get(i, 0)) for i in range(1, n + 1)))

main()
