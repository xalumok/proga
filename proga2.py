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

    def is_sorted(self):
        if self.empty():
            return True
        last = self.start_node
        cur = self.start_node
        while cur != None:
            if last.val>cur.val:
                return False
            last = cur
            cur = cur.next
        return True

    def sum_of_positives(self):
        res = 0
        cur = self.start_node
        while cur != None:
            res += cur.val
            cur = cur.next
        return res

    def mult_of_diff(self):
        if self.empty():
            return 0
        res = 1
        last = self.start_node
        cur = self.start_node
        ind = 0
        while cur != None:
            if (ind != 0):
                res *= (cur.val-last.val)
            last = cur
            cur = cur.next
            ind+=1
        return res


a = list(map(float, input().split()))

ll = LinkedList()

for x in a:
    ll.push_back(x)

if ll.is_sorted():
    print(ll.mult_of_diff())
else:
    print(ll.sum_of_positives())