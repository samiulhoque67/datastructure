
import random

class Node:
    def __init__(self,val):
        self.next=None
        self.val=val



class Single:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
        
    def add(self,val,where=None):
        node=Node(val)
        if(where is None):
            self.__attheend(node)
        else:
            self.__traverse(node,where)
        
    def recursiveprint(self):
        node=self.head
        val=[]
        val1=[]
        val1=self.__print_using_recursion(node,val)
        print(', '.join(str(value) for value in val1))

        
        
    def recursiveprintreverse(self):
        node=self.head
        vall=[]
        self.head=self.__print2_using_recursion(node)
        temp=self.head
        
        while temp is not None:
            vall.append(temp.val)
            temp=temp.next
        print(', '.join(str(value) for value in vall))
    def __attheend(self,node):
        if(self.tail is None):
            self.head=node
            self.tail=node
            self.size+=1
        else:
            self.tail.next=node
            self.tail=node
            self.size+=1
            
    def __beginning(self,node):
        if(self.head is None):
            self.head=node
            self.tail=node
            self.size+=1
        else:
            node.next=self.head
            self.head=node
            self.size+=1
            
    def __remove_val(self,node):
       if self.head==node:
           self.head=node.next
           self.size-=1
           
       else:
           node1=self.head
           while node1 is not None:
               if node1.next==node:
                   node1.next=node.next
                   self.size-=1
                   break
               node1=node1.next
               
    def __remove_index(self,node):
       if self.head==node:
           self.head=node.next
           self.size-=1
           
       else:
           node1=self.head
           while node1 is not None:
               if node1.next==node:
                   node1.next=node.next
                   self.size-=1
                   break
               node1=node1.next
          
     
    def removebyindex(self,value):
       node=self.head
       p=1
       while node is not None:
           if p==value:
               self.__remove_index(node)
               break
           node=node.next
           p=p+1
    def remove(self,value):
       node=self.head
       while node is not None:
           if node.val==value:
               self.__remove_val(node)
               break
           node=node.next
           
    def __traverse(self,node,where):
        
        if(where>self.size+1):
            print("invalid position to insert:")
        else:
            if(where==1):
                self.__beginning(node)
            elif(where==self.size+1):
              
              self.__attheend(node)
            else:
                node2=self.head
                p=1
                while node2 is not None:
                    if(where==p+1):
                        temp=node2.next
                        node2.next=node
                        node.next=temp
                        self.size+=1
                        break
                    node2=node2.next
                    p=p+1
    def __reverse(self):
        curr=self.head
        prev=None
        while curr is not None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev
        return self.head
    
    def __print_using_recursion(self,node,val):
        if node is None:
            
            return 
        else:
            val.append(node.val)
            
            self.__print_using_recursion(node.next,val)
           
        
        return val
        
    def __print2_using_recursion(self,node):
        if node.next is None:
            self.head=node
            
            return self.head
        rest=self.__print2_using_recursion(node.next)
        temp=node.next
        temp.next=node
            
        node.next=None
        return rest
       
    def reverselist(self):
        self.head=self.__reverse()
        val=[]
        node=self.head
        while node is not None:
            val.append(node.val)
            node=node.next
        print(', '.join(str(value) for value in val))
      

    def __str__(self):
        val=[]
        node=self.head
        while node is not None:
            val.append(node.val)
            node=node.next

        return f"{', '.join(str(vall) for vall in val)}"


mylist = Single()
n=int(input("how many numbers want to add :"))

for i in range(0,n):
    m=int(input("give the number :"))
    wh=int(input("where to input  :"))
    mylist.add(m,wh)
g=int(input("do you want to remove type \n 1 for remove \n 0 for not\n please type:"))
if g==0:
    print("do nothing")
elif(g==1):
    n1=int(input("how many numbers want to remove :"))
    for j in range(0,n1):
        ch=int(input("how  do you want to remove  0 for remove by value 1 for remove by index:"))
        if ch==0:
            m1=int(input("give the number you want to remove:"))
            mylist.remove(m1)
            print(mylist)
        elif ch==1:
            m1=int(input("give the index you want to remove:"))
            mylist.removebyindex(m1)
            print(mylist)

while(1):
    print("how do you want to see your list :")
    print("""type=traverse ' if you want to see the original list'
type=reverse ' if you want to see the reverse list'
type anything if you don't want to see anything """)
             
    pr=input()
    if pr=="traverse":
        print(mylist)
    elif pr=="reverse":
        mylist.reverselist()
    else:
        break
print("print the list using recursion\n")
while(1):
    print("how do you want to see your list :")
    print("""type=traverse ' if you want to see the original list'
type=reverse  ' if you want to see the reverse list'
type anything if you don't want to see anything """)
             
    pr=input()
    if pr=="traverse":
        mylist.recursiveprint()
    elif pr=="reverse":
        mylist.recursiveprintreverse()
    else:
        break
"""
print(mylist.print)
       
print(mylist)

mylist.print2()

print(mylist)
mylist.print3()

"""


