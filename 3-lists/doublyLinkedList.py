class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList: 

    def __init__(self, value):
        #create a node
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
        #create a new node 
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
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
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None 
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        #test for valid index
        if (index <0 or index >= self.length):
            return None
        temp = self.head
        #only put variable in for loop if used inside of loop
        #use _ if not used
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else: 
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
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
        before = self.get(index-1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True
    
    def remove (self, index):
        if (index <0 or index >= self.length):
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        temp = self.get(index)
        before = temp.prev
        after = temp.next
        before.next = after
        after.prev = before
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp

    def swap_first_last(self):
        if self.head is None or self.head == self.tail:
            return
        # temp = self.head
        # self.head.value = self.tail.value
        # self.tail.value = temp.value
        self.head.value, self.tail.value = self.tail.value, self.head.value

    def reverse(self):
        temp = self.head
        #for each node, swap next and prev
        while temp is not None:
            #swap values of temp
            temp.next, temp.prev = temp.prev, temp.next
            #increment temp with swapped value
            temp = temp.prev
        #swap head and tails
        self.head, self.tail = self.tail, self.head


    def is_palindrome(self):
        if self.length <= 1:
            return True
        fwd = self.head
        bwd = self.tail
        for i in range(self.length // 2):
            if fwd.value != bwd.value:
                return False
            fwd = fwd.next
            bwd = bwd.prev
        return True
        



my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
# my_doubly_linked_list.insert(1,10)
# print(my_doubly_linked_list.length)
# my_doubly_linked_list.remove(3)
my_doubly_linked_list.print_list()

print(my_doubly_linked_list.reverse())

# print(my_doubly_linked_list.get(1))
# print(my_doubly_linked_list.get(2))

# # Pop Test Cases
# # 2 items
# print(my_doubly_linked_list.pop_first())
# #1 item
# print(my_doubly_linked_list.pop_first())
# #0 items
# print(my_doubly_linked_list.pop_first())