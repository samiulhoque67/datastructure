class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]

    def add(self,val):
        g=len(self.s1)
        for i in range(0,g):
            self.s2.append(self.s1[0])
            self.s1.pop(0)
        
        self.s1.append(val)

        h=len(self.s2)
        for j in range(0,h):
            self.s1.append(self.s2[0])
            self.s2.pop(0)
            
    def rem(self):
        if len(self.s1)==0:
            print("Q is Empty")
            return
        x = self.s1[0]  
        self.s1.pop(0)  
        return x
        """ 
    def print(self):
        
        k=len(self.s1)
        for i in range(0,k):
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
        q.add(m)
        
    elif n==2:
        
        if j>=i:
            m1=int(input("stack is empty.push first :"))
            q.add(m)
            i+=1
        else:
            j+=1
            
            p=q.rem()
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



                  





