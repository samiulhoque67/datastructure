class Node:
    def __init__(self,val):
        self.next=None
        self.val=val
class Stack:
    def __init__(self):
        self.head=None
        self.size=0
    def push(self,val):
        node=Node(val)
        if self.head is None :
            self.head=node
            self.size+=1
        else:
            temp=self.head
            self.head=node
            node.next=temp
            self.size+=1
            
    def pop(self):
        self.head=self.head.next
        self.size-=1
    def is_empty(self):
        return self.size==0
    
    def __str__(self):
        if self.head is not None:
            val=[]
            node2=self.head
            while node2 is not None:
                val.append(node2.val)
                node2=node2.next
            return f"{', '.join(str(value) for value in val)}"
        else:
            
            return "empty stack"
           
        

stack=Stack()
while(1):
    n=int(input("type 1 for push \ntype 2 for pop\ntype 3 for see the stack\ntype 4 for quit\nenter: "))
    if(n==1):
        n=int(input("the number you want to input: "))
        stack.push(n)
    elif n==2:
        stack.pop()
    elif n==3:
        
        print("the stack is ",stack)
    else:
        break
    


