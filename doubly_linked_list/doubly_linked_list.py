class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.head is not None:
            temp = self.tail
            if self.length == 1:
                self.head = self.tail = None
            else:
                self.tail = temp.prev
                temp.prev = self.tail.next = None
            self.length -= 1
            return temp
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.head is not None:
            temp = self.head
            if self.length == 1:
                self.head = self.tail = None
            else:
                self.head = temp.next
                temp.next = self.head.prev = None
            self.length -= 1
            return temp
        
    def get(self, index):
        if 0 <= index < self.length:
            temp = self.head
            if index < self.length / 2:
                for _ in range(index):
                    temp = temp.next
            else:
                temp = self.tail
                for _ in range(self.length - 1, index, -1):
                    temp = temp.prev
            return temp
        
    def set_value(self, index, value):
        if 0 <= index < self.length:
            temp = self.get(index)
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if 0 <= index <= self.length:
            if index == 0:
                return self.prepend(value)
            elif index == self.length:
                return self.append(value)
            
            new_node = Node(value)
            temp = self.get(index - 1)
            new_node.next = temp.next
            temp.next.prev = new_node
            temp.next = new_node
            new_node.prev = temp
            self.length += 1
            return True
        return False
    
    def remove(self, index):
        if 0 <= index < self.length:
            if index == 0:
                return self.pop_first()
            elif index == self.length - 1:
                return self.pop()
            
            temp = self.get(index)
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            temp.next = temp.prev = None
            self.length -= 1
            return temp



dll = DoublyLinkedList(4)
dll.append(7)
dll.append(9)
dll.remove(3)
dll.print_list()

        