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

    def __insert

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


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print("BST contains 27: ")
print(my_tree.r_contains(27))

print("\nBst contains 17: ")
print(my_tree.r_contains(17))