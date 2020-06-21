
  
class Queue:  
    def __init__(self): 
        self.s1 = [] 
        self.s2 = [] 
  
    def enqueue(self, x): 
           
        g=len(self.s1)
        for i in range(0,g):
            self.s2.append(self.s1[-1])
                 
            self.s1.pop() 
  
         
        self.s1.append(x)  
 
        h=len(self.s2) 
        for j in range(0,h):  
            self.s1.append(self.s2[-1])  
            self.s2.pop() 
  
 
    def dequeue(self): 
          
            
        if len(self.s1) == 0:  
            print("Q is Empty")
        x = self.s1[-1]  
        self.s1.pop()  
        return x 
    """ 
    def print(self):
        
        k=len(self.s1)
        for i in range(k-1,-1,-1):
            print(self.s1[i])
       """     

        

q=Queue()
i=0
j=0
while(1):
    n=int(input("type 1 for push \ntype 2 for pop \ntype 3 for print\ntype 4 for quit\ntype : "))
    if n==1:
        i+=1
        
        m=int(input("give a number :"))
        q.enqueue(m)
        
    elif n==2:
        
        if j>=i:
            m1=int(input("stack is empty.push first :"))
            q.enqueue(m)
            i+=1
        else:
            j+=1
     
            p=q.dequeue()
            print('\nyou have poped :',p)
            
        """
    elif n==3:
        q.print()
        """
    elif n==4:
        break
        """
print("this is for print")
q.print()
"""
 
