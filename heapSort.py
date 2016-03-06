import random

def generate(columns=30, max=100):
    result=[]
    for i in range(columns):
        result.append(random.randint(0,max-1))
    result=[0]+result
    return result

n=1000
k=500
list1=generate(n,k)
print list1

def heapSort(list1):
    buildMinHeap(list1)
    result=[]
    size=len(list1)-1
    while (size>=1):
        result.append(list1[1])
        list1[1]=list1[size]
        size-=1
        Minheap(list1,1)
    return result

def buildMinHeap(list1):
    floor=len(list1)/2
    for i in range(floor,0,-1):
        Minheap(list1,i)


def Minheap(A,i):
    min=i
    size=len(A)-1
    if (2*i<=size and A[min]>A[2*i]):
        min=2*i
    if (2*i+1<=size and A[min]>A[2*i+1]):
        min=2*i+1
    if (min!=i):
        A[min],A[i]=A[i],A[min]
        Minheap(A,min)

print heapSort(list1)
