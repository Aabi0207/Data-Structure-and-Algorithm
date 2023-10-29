class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, start_index, end_index):
        # 1. Edge Case: If list has only one node or none, exit.
        if self.length <= 1:
            return
    
        # 2. Create a dummy node to simplify head operations.
        dummy_node = Node(0)
        dummy_node.next = self.head
    
        # 3. Init 'previous_node', pointing just before reverse starts.
        previous_node = dummy_node
    
        # 4. Move 'previous_node' to its position.
        # It'll be at index 'start_index - 1' after this loop.
        for i in range(start_index):
            previous_node = previous_node.next
    
        # 5. Init 'current_node' at 'start_index', start of reversal.
        current_node = previous_node.next
    
        # 6. Begin reversal:
        # Loop reverses nodes between 'start_index' and 'end_index'.
        for i in range(end_index - start_index):
            # 6.1. 'node_to_move' is next node we want to reverse.
            node_to_move = current_node.next
    
            # 6.2. Disconnect 'node_to_move', point 'current_node' after it.
            current_node.next = node_to_move.next
    
            # 6.3. Insert 'node_to_move' at new position after 'previous_node'.
            node_to_move.next = previous_node.next
    
            # 6.4. Link 'previous_node' to 'node_to_move'.
            previous_node.next = node_to_move
    
        # 7. Update list head if 'start_index' was 0.
        self.head = dummy_node.next
    


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None
    
"""
