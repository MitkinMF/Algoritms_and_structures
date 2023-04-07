# Необходимо реализовать метод разворота связного списка (двухсвязного или односвязного на выбор).

class Node: #двусвязный
    def __init__(self):
        self.value = None
        self.next = None
        self.previous = None

# class Node: #Односвязный
#     def __init__(self):
#         self.value: int
#         self.next: Node

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def find (self, value: int):
        current_node = self.head
        while (current_node != None):
            if (current_node.value == value):
                return current_node
            return None

    def add (self, value: int):
        node = Node()
        node.value = value
        if (self.head == None):
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node

    # def add (value: int, node: Node): для односвязного
    #     next = node.next
    #     new_node: Node
    #     node.next = new_node
    #     new_node.previous = node
    #     if (next == None):
    #         self.tail = new_node
    #     else:
    #         next.previous = new_node
    #         new_node.next = next
                
    def delete (self, node: Node):
        previous = node.previous
        next = node.next
        if(previous == 0):
            next.previous = None
            self.head = next
        else:
            if (next == None):
                previous.next = None
                self.tail = previous
            else:
                previous.next = next
                next.previous = previous
                
    def revert(self):
        current_node = self.head
        while(current_node !=  None):
            next = current_node.next
            previous = current_node.previous
            current_node.next = previous
            current_node.previous = next
            if( previous == None ):
                self.tail = current_node
            if (next == None):
                self.head = current_node
            current_node = next
            
            
    def printt(self):
        current_node = self.head    
        while(current_node != None):
            print (current_node.value)
            current_node = current_node.next
                   
        
        
My_list = List()

My_list.add(1)
My_list.add(2)
My_list.add(3)
My_list.add(4)

My_list.printt()

My_list.revert()

My_list.printt()
 
        
        



        



