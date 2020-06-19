class Node:
    def __init__(self,val):
        self.next=None
        self.val=val
class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
        
    def enqueue(self,data):
        node=Node(data)
        if self.tail is None:
            self.head=node
            self.tail=node
            self.size+=1
        else:
            self.tail.next=node
            self.tail=node
            node.next=None
            self.size+=1
            
    def dequeue(self):
        if self.head is None:
            print("queue is empty")
            return
        self.head=self.head.next
        self.size-=1
        
    def is_empty(self):
        
        return self.size==0

    def __str__(self):
        val=[]
        node=self.head
        while node is not None:
            val.append(node.val)
            node=node.next

        return f"{', '.join(str(vall) for vall in val)}"
    

q=Queue()
while(1):
    n=int(input("type 1 for enqueue \ntype 2 for dequeue\ntype 3 for see the queue\ntype 4 for quit\nenter: "))
    if(n==1):
        n=int(input("the number you want to input: "))
        q.enqueue(n)
    elif n==2:
        q.dequeue()
    elif n==3:
        
        print("the queue is ",q)
    else:
        break
