import sys

def loadfile(filename):
    with open(filename) as handle:
        exec(handle.read())
        return list
          
def MergeSort(list1):
    n=len(list1)
    if n==1:
        return list1
    else:
        mid=n//2
        lista=list1[0:mid]
        listb=list1[mid:]
        lista2=MergeSort(lista)
        listb2=MergeSort(listb)
        array=[]
        i=0
        j=0
        while i<len(lista2) and j<len(listb2):
            if lista2[i]<=listb2[j]:
                array.append(lista2[i])
                i+=1
            else:
                array.append(listb2[j])
                j+=1
        if i>=len(lista):
            array.extend(listb2[j:])
        else:
            array.extend(lista2[i:])
        return array
                
def main():
    if len(sys.argv)<2:
        print 'usage: MergeSort.py filename'
    else:
        filename=sys.argv[1]
        list1=loadfile(filename)
        array=MergeSort(list1)
        print array

if __name__=='__main__':
    main()
    