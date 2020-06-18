class Stack:
    def __init__(self,sz):
        self.top=-1
        self.st=[None for x in range(0,sz)]
    def push(self,value):
        self.top+=1
        self.st[self.top]=value

    def peek(self):
        return self.st[self.top]

    def pop(self): 
        last=self.st[self.top]
        self.top-=1
        return last
    def is_empty(self):
        return self.top==-1
    
stk=input("enter a string :")

size=len(stk)


stack=Stack(size)
for i in stk:
    stack.push(i)
stk=""
for j in range(0,size):
    stk+=stack.pop()
    
print(stk)
