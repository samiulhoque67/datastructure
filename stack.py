class Stack:
    def __init__(self,size):
        self.top=-1
        self.size=size
        self.st=[None for sz in range(size)]
    def push(self,value):
        if(self.top==self.size-1):
            print("overflow")
            return
        
        self.top+=1
        self.st[self.top]=value
    def pop(self):
        if(self.top==-1):
            print("underflow")
            return
        lastitem=self.st[self.top]
        self.top-=1
        return lastitem
    def peek(self):
        return self.st[self.top]
    def is_empty(self):
        return self.top==-1
    def print(self):
        if(self.top==-1):
            print("no number in stack\n")
            return
        
        print(','.join(str(self.st[i]) for i in range(self.top,-1,-1)))
        



size=int(input("Enter the size :"))       
stack=Stack(size)
while(1):
    n=int(input("type 1 for push \ntype 2 for pop \ntype 3 for print\ntype 4 for quit\ntype : "))
    if n==1:
        m=int(input("give a number :"))
        stack.push(m)
    elif n==2:
        p=stack.pop()
        print('\nyou have poped :',p)
    elif n==3:
        stack.print()
    elif n==4:
        break

