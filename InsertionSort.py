import sys


def loadfile(filename):
    with open(filename) as handle:
        namespace=dict()
        exec(handle.read(),namespace)
        return namespace['list']

def InsertionSort(list1):
    n=len(list1)
    for i in range(n):
        key=list1[i]
        j=i-1
        while j>=0 and list1[j]>key:
            list1[j+1]=list1[j]
            j-=1
        list1[j+1]=key
    return list1
def main():
    
    if len(sys.argv) <2:
        print 'usage: InsertionSort.py filename',len(sys.argv)
    else:
        filename=sys.argv[1]
        list1=loadfile(filename)
        array=InsertionSort(list1)
        print array

if __name__=='__main__':
    main()