class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if value == temp.value:
                return False
            if value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    

    def BFS(self):
        if self.root is not None:
            result = []
            queue =[]
            queue.append(self.root)
            while len(queue) >= 1:
                current_node = queue.pop(0)
                result.append(current_node.value)
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
            return result
    
    def dfs_pre_order(self):
        if self.root is not None:
            result = []

            def traverse(current_node):
                result.append(current_node.value)
                if current_node.left is not None:
                    traverse(current_node.left)
                if current_node.right is not None:
                    traverse(current_node.right) 
            traverse(self.root)
            return(result)
        
    def dfs_post_order(self):
        if self.root is not None:
            results = []

            def traverse(current_node):
                if current_node.left is not None:
                    traverse(current_node.left)
                if current_node.right is not None:
                    traverse(current_node.right)
                results.append(current_node.value)
            traverse(self.root)
            return results
        
    def dfs_in_order(self):
        if self.root is not None:
            results = []

            def traverse(current_node):
                if current_node.left is not None:
                    traverse(current_node.left)
                results.append(current_node.value)
                if current_node.right is not None:
                    traverse(current_node.right)
            traverse(self.root)
            return results



my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
print(my_tree.dfs_in_order())