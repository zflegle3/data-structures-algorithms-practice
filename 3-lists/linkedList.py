class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList: 

    def __init__(self, value):
        #create a node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append (self, value):
        #create a new node 
        #add node to end
        new_node = Node(value)
        #if only one node head and tail are set to one node
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else: 
            #sets current last node to point to new node
            self.tail.next = new_node
            #sets tail pointer to new node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop (self):
        #No items 
        if self.length == 0:
            return None
        #List > 0
        #variables for iterating
        temp = self.head
        pre = self.head
        #iterates through nodes to find when temp points to the end 
        # pre points to the preceeding node
        while(temp.next != None):
            pre = temp
            temp = temp.next 
        #At end
        #set tail to point to new end node
        self.tail = pre
        #reset new tail node as end 
        self.tail.next = None
        #decrement length
        self.length -= 1
        #handle case if was only one node and reset head/tail
        if self.length == 0:
            self.head = None
            self.tail = None
        #returns removed node
        return temp

    def prepend(self, value):
        #create a new node 
        new_node = Node(value)
        #add node to beginning
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
                self.tail = None
        return temp
    
    def get(self, index):
        #test for valid index
        if (index <0 or index >= self.length):
            return None
        temp = self.head
        #only put variable in for loop if used inside of loop
        #use _ if not used
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        #will return none or a node
        temp = self.get(index)
        if temp != None:
            temp.value = value
            return True
        return False
        
    def insert(self, index, value):
        #test for valid index
        if (index <0 or index > self.length):
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        #create a new node 
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove (self, index):
        #test for valid index
        if (index <0 or index >= self.length):
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        #O(1) way of getting temp vs get method O(n)
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse (self):
        #switch head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp
        #reverse next
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        

my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.prepend(1)
my_linked_list.set_value(1,9)
# my_linked_list.pop_first()
my_linked_list.print_list()

# Pop Test Cases
#2 items
# print(my_linked_list.pop_first())
# #1 item
# print(my_linked_list.pop_first())
# #0 items
# print(my_linked_list.pop_first())
# print(my_linked_list.get(1))




