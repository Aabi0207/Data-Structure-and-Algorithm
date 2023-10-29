class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    
class Queue:
    def __init(self, value):
        new_node = Node(value)
        self.first = self.last = new_node
        self.length = 1

    def print_stack(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next  

    def enqueue(self, value):
        new_node = Node(value) 
        if self.length == 0:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.tail = new_node
        self.length += 1

    def dequeue(self):
        if self.first is not None:
            temp = self.first
            if self.length == 1:
                self.first = self.last = None
            else:
                self.first = temp.next
                temp.next = None
            return temp