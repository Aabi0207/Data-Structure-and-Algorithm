class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # def insert(self, value):
    #     new_node = Node(value)
    #     if self.root is None:
    #         self.root = new_node
    #         return True
    #     temp = self.root 
    #     while True:
    #         if temp.value == value:
    #             return False
    #         elif temp.value < value:
    #             if temp.right is None:
    #                 temp.right = new_node
    #                 return True
    #             temp = temp.right
    #         else:
    #             if temp.left is None:
    #                 temp.left = new_node
    #                 return True
    #             temp = temp.left

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        elif current_node.value < value:
            current_node.right = self.__r_insert(current_node.right, value)
        elif current_node.value > value:
            current_node.left = self.__r_insert(current_node.left, value)
        return current_node
    
    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        elif current_node.value == value:
            return True
        elif current_node.value < value:
            return self.__r_contains(current_node.right, value)
        else:
            return self.__r_contains(current_node.left, value)
        
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    
    def _minimum_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    
    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        elif value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left and current_node.right is None:
                return None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                sub_tree_min = self._minimum_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node  

    def delete_node(self, value):
        self.__delete_node(self.root, value)


my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)

print("Root:", my_tree.root.value)
print("Root -> Left:", my_tree.root.left.value)
print("Root -> Left:", my_tree.root.right.value)

my_tree.delete_node(2)

print("Root:", my_tree.root.value)
print("Root -> Left:", my_tree.root.left.value)
print("Root -> Left:", my_tree.root.right)