import random


def generate(columns=30,max=100):
    result=[]
    for i in range(columns):
        result.append(random.randint(0,max-1))
    return result


n=1000
k=500
list1=generate(n,k)

def quickSort(list1):
    recursive_quicksort(list1,0,len(list1)-1)
    return list1

def recursive_quicksort(A,p,q):
    if p<q:
        r=partition(A,p,q)
        recursive_quicksort(A,p,r-1)
        recursive_quicksort(A,r+1,q)

def partition(A,p,q):
    i=p-1
    pivot=A[q]
    for j in range(p,q):
        if A[j]<=pivot:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[q]=A[q],A[i+1]
    return i+1

print quickSort(list1)
