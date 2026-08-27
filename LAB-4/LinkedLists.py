class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,data):
        n=Node(data)
        if self.head is None:
            self.head=n
            return
        n.next=self.head
        self.head=n

    def insert_at_end(self,data):
        n=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=n

    def insert_at_index(self,data,index):
        if self.head is None:
            print("No data Available")
            return
        new=Node(data)
        temp=self.head
        if index == 0:
            new.next = self.head
            self.head = new
            return
        for i in range(index-1):
            temp=temp.next
        new.next=temp.next
        temp.next=new

    def delete_at_beginning(self):
        if self.head is None:
            print("No data Available")
            return
        temp=self.head
        self.head=temp.next

    def delete_at_end(self):
        if not self.had:
            print("No data Available")
            return 
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=None

    def remove_with_value(self,target):
        if self.head is None:
            print("No data Available")
            return
        else:
            temp=self.head
            if temp and temp.data == target:
                self.head=temp.next
                return
            while temp.next and temp.next.data != target:
                temp=temp.next
            if temp.next:
                temp.next=temp.next.next
            else:
                print("No Value Present")
            
    def count(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        print(count)

    def display(self):
        if self.head is None:
            print("No data available")
            return
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

l1=LinkedList()
l1.insert_at_beginning(10)
l1.insert_at_beginning(20)
l1.insert_at_end(10)
l1.insert_at_end(20)
l1.display()
l1.count()
l1.delete_at_beginning()
l1.count()
l1.display()
