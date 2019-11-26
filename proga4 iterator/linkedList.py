class Node:
    def __init__(self,val): 
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.start_node=None

    def push_back(self, val):
        node=Node(val)
        if self.start_node==None:
            self.start_node=node
        else:
            cur=self.start_node
            while cur.next != None:
                cur=cur.next
            cur.next=node

    def empty(self):
        return (self.start_node == None)

    def print(self):
        cur=self.start_node
        while cur != None:
            print(cur.val)
            cur=cur.next
