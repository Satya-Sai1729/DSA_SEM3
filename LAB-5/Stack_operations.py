class Stack_Array:
    def __init__(self,length):
        self.length=length
        self.stack=[]
        self.top=-1


    def stack_push(self,data):
        if len(self.stack) == 0:
            print("Stack is empty")
        self.data=data
        self.stack.append(data)
        self.top+=1
        self.length-=1
        print("Element pushed successfully")

    def stack_pop(self):
        if len(self.stack) == 0:
            return "Stack is Empty"
        print(stack.pop(),"removed")
    
            
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Top element:", stack[-1])

    def top_index(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        print(self.stack[self.top])

    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Stack elements:")
            for i in range(len(self.stack) - 1, -1, -1):
                print(self.stack[i])
            

s1=Stack_Array(10)
s1.stack_push(49)
s1.stack_push(48)
s1.stack_push(32)
s1.stack_push(8)
s1.display()
s1.top()
