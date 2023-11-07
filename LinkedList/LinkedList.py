class Node:
    """This class creates a Node whenever required."""
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """This class creates a linked list and also contain all the methods and attributes related to the linked list."""
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if not self.head is None:
            temp = self.head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                while temp.next.next is not None:
                    temp = temp.next
                
                self.tail = temp
                temp.next = None
            self.length -= 1
            return temp
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length != 0:
            temp = self.head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = temp.next
                temp.next = None
            self.length -= 1
            return temp
        
    def get(self, index):
        if 0 <= index < self.length:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if 0 <= index <= self.length:
            if index == 0:
                return self.prepend(value)
            elif index == self.length:
                return self.append(value)
            else:
                temp = self.head
                for _ in range(index - 1):
                    temp = temp.next
                new_node = Node(value)
                new_node.next = temp.next
                temp.next = new_node
            self.length += 1
            return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first
        if index == self.length -1:
            return self.pop()
        
        pre = self.get(index -1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head, self.tail = self.tail, self.head
        after, before = temp.next, None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    
    

linked_list = LinkedList(4)
linked_list.append(3)
linked_list.append(8)
linked_list.append(5)
linked_list.reverse()
linked_list.print_list()


