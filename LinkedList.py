class Node:
   
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)
    
    def get_value(self):
        return self.value


node1 = Node(5)
node2 = Node(10)
node3 = Node(15)

node1.next = node2
node2.next = node3

current = node1
while current:
    print(current.value)
    current = current.next