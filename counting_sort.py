import random


def generate(columns=30,max=100):
    result=[]
    for i in range(columns):
        result.append(random.randint(0,max-1))
    return result


n=1000
k=500
list1=generate(n,k)
print list1


def countingSort(list1,k):
    L=[]
    for j in range(k):
        L.append([])
    n=len(list1)
    for i in range(n):
        L[list1[i]].append(list1[i])
    output=[]
    for m in range(k):
        output.extend(L[m])
    return output
print countingSort(list1,k)