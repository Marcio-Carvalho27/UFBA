class Node:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

        self.layer = None

        self.right = None
        self.left = None

    def getName(self):
        return self.name


class Tree:
    def __init__(self):
        self.root = None
        self.layer = 0

    def insert(self, node):
        if self.root is None:
            self.root = node
            return
        
        aux = 0
        current = self.root
        while True:
          if aux % 2 == 0:
            if node.age < current.age:
                if current.left is None:
                    current.left = node
                    return
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = node
                    return
                else:
                    current = current.right
          else:
            if node.salary < current.salary:
                if current.left is None:
                    current.left = node
                    return
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = node
                    return
                else:
                    current = current.right
          aux += 1

    def preordem(self, minSalary, maxSalary, minAge, maxAge, node):
      if minSalary <= node.salary <= maxSalary and minAge <= node.age <= maxAge:
        print(node.name)
      if node.left:
        self.preordem(minSalary, maxSalary, minAge, maxAge, node.left)
      if node.right:
        self.preordem(minSalary, maxSalary, minAge, maxAge, node.right)



def main():
    tree = Tree()

    N = int(input())

    for _ in range(N):
        name, age, salary = input().split(" ")
        tree.insert(Node(name, int(age), int(salary)))

    minAge, maxAge = input().split(" ")
    minSalary, maxSalary = input().split(" ")

    minAge = int(minAge)
    maxAge = int(maxAge)
    if maxAge == 0:
        maxAge = 100000000000000000000000000000
    minSalary = int(minSalary)
    maxSalary = int(maxSalary)
    if maxSalary == 0:
        maxSalary = 100000000000000000000000000000

    tree.preordem(minSalary, maxSalary, minAge, maxAge, tree.root)

main()

"""
23
Jaymee 34 1148
Lyndsie 55 4117
Missy 63 2120
Ebonee 42 3581
Korie 53 5229
Gilberta 52 4070
Brigit 21 613
Karissa 37 2275
Joete 47 3466
Cesya 18 2104
Nessie 36 6312
Anna-Maria 52 5020
Jenny 24 2919
Lina 47 5920
Kirbee 48 6043
Tricia 60 2104
Truday 26 8688
Nicholle 43 8509
Diena 27 2646
Tommy 61 1143
Beryl 41 4564
Joray 33 2396
Marilee 51 4353
24 51
0 4247
"""