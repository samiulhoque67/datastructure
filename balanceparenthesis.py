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

def balance(stk,size):
    stack=Stack(size)
    for i in stk:
        if i=="{" or i=="(" or i=="[" :
            stack.push(i)
        else:
            if stack.is_empty():
                return False
            if i=="}" and stack.peek()!="{":
                return False
            if i==")" and stack.peek()!="(":
                return False
            if i=="]" and stack.peek()!="[":
                return False
            else:
                stack.pop()
    if stack.is_empty():
        return True
    
    return False
            
n=int(input("enter the test case :"))
while(n!=0):
    stk=input("enter a string :")
    size=len(stk)
    print(balance(stk,size))
    n-=1
