class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __r_insert(self, current_node, value):
        #base case
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    
    def __r_contains(self, current_node, value):
        #base case
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        else:
            return self.__r_contains(current_node.right, value)
        
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    
    def min_value(self, current_node):
        while current_node.left is not None:
            #min value is always open to the left
            current_node = current_node.left
        #not returning node, returning value
        return current_node.value
    
    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        #traverse left or right 
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        #find value and handle cases
        else:
            #no l&r values
            if current_node.left == None and current_node.right == None:
                return None
            #only r value
            elif current_node.left == None:
                current_node = current_node.right
            #only l value
            elif current_node.right == None:
                current_node = current_node.left
            #l&r value
            else:
                #gets value, not node, from min node
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                #uses delete node method on current node with min value
                current_node.right = self.delete_node(current_node.right, sub_tree_min)
        return current_node

    def delete_node(self, value):
        self.__delete_node(self.root, value)

    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            #add value to results first
            results.append(current_node.value)
            #check left and right
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        
        traverse(self.root)
        return results
    
    def dfs_post_order(self):
        results = []
        
        def traverse(current_node):
            #check left and right first
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            #add value to results
            results.append(current_node.value)
        
        traverse(self.root)
        return results
    
    def dfs_in_order(self):
        results = []
        
        def traverse(current_node):
            #check left first
            if current_node.left is not None:
                traverse(current_node.left)
            #add value to results
            results.append(current_node.value)  
            #check right last
            if current_node.right is not None:
                traverse(current_node.right)
        
        traverse(self.root)
        return results
    





my_tree = BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

print(my_tree.dfs_pre_order())
print(my_tree.dfs_post_order())
print(my_tree.dfs_in_order())