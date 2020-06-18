class Stack:
    def __init__(self,sz):
        self.top=-1
        self.st=[None for x in range(0,sz)]
    def push(self,value):
        self.top+=1
        self.st[self.top]=value

    def pop(self):
        
        last=self.st[self.top]
        self.top-=1
        return last






stk=input("enter a string :")
st2=[]
size=len(stk)


stack=Stack(size)
for i in range(0,size):
    stack.push(stk[i])
stk=""
for j in range(0,size):
    stk+=stack.pop()
    
print(stk)
