class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert_at_beginning(self,data):
        n=Node(data)
        if self.head is None:
            self.head=n
            self.tail=n
            return
        temp=self.head
        n.next=self.head
        temp.prev=n
        self.head=n
        
    def insert_at_end(self,data):
        n=Node(data)
        temp=self.head
        if self.head is None:
            self.head=n
            return
        while temp.next:
            temp=temp.next
        temp.next=n
        n.prev=temp
        self.tail=n

    def count(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        print("No of Nodes : ",count)

    def display_from_head(self):
        if self.head is None:
            print("No data available")
            return
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

    def display_from_tail(self):
        if self.head is None:
            print("No data available")
            return
        temp=self.tail
        while temp:
            print(temp.data)
            temp=temp.prev

    
d1=DoubleLinkedList()
d1.insert_at_beginning(20)
d1.insert_at_beginning(40)
d1.insert_at_beginning(60)
d1.display_from_head()
d1.display_from_tail()
d1.count()
