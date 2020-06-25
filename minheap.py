n=int(input("Enter input "))
arr=[]

def minheap(arr,n,i):
    smallest=i
    l=2*i+1
    r=2*i+2
    if(l<n and arr[l]<=arr[smallest]):
        smallest=l
    if(r<n and arr[r]<=arr[smallest]):
        smallest=r
    if(smallest!=i):
        arr[i],arr[smallest]=arr[smallest],arr[i]
        minheap(arr,n,smallest)
        

def buildheap(arr,n):
    for i in range(n//2 -1,-1,-1):
        minheap(arr,n,i)
   
        

for i in range(0,n):
    m=int(input())
    arr.append(m)

buildheap(arr,n)
for i in range(0,n):
    print(arr[i],end=" ")
