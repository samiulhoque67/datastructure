n=int(input("Enter input "))
arr=[]

def maxheap(arr,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if(l<n and arr[l]>=arr[largest]):
        largest=l
    if(r<n and arr[r]>=arr[largest]):
        largest=r
    if(largest!=i):
        arr[i],arr[largest]=arr[largest],arr[i]
        maxheap(arr,n,largest)
        

def buildheap(arr,n):
    for i in range(n//2 -1,-1,-1):
        maxheap(arr,n,i)
   
        

for i in range(0,n):
    m=int(input())
    arr.append(m)

buildheap(arr,n)
for i in range(0,n):
    print(arr[i],end=" ")
