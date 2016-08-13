class HTNode():
    def __init__(self):
        self.parent=0
        self.lchild=0
        self.rchild=0
        self.weight=0

w=[0,10,8,7,2]

def HuffmanCoding(w,n):
    m=2*n
    ht=['']*m
    for i in range(m):
        ht[i]=HTNode()

    for i in range(1,n+1):
        ht[i].weight=w[i]
    for i in range(n+1,m):
        p1=0
        p2=0
        w1=w2=100000
        for j in range(1,i):
            if ht[j].parent==0:
                if ht[j].weight<w1:
                    w2=w1
                    p2=p1
                    w1=ht[j].weight
                    p1=j
                elif ht[j].weight<w2:
                    w2=ht[j].weight
                    p2=j
        ht[p1].parent=i
        ht[p2].parent=i 
        ht[i].lchild=p1
        ht[i].rchild=p2
        ht[i].weight=w1+w2


    # for i in range(1,m):
    #     print ht[i].parent,ht[i].weight,ht[i].lchild,ht[i].rchild
    # ####encode
    hc=['']*(n+1)
    
    import copy

    for k in range(1,n+1):
        start=0
        cd=['']*n
        c=k
        f=ht[k].parent

        while(f):
            if ht[f].lchild==c:
                cd[start]='0'
                start+=1
            else: 
                cd[start]='1'
                start+=1
            c=f
            f=ht[f].parent
            # print k, f,cd
        cd.reverse()
        hc[k]=''.join(copy.deepcopy(cd))
    return hc
hc=HuffmanCoding(w,4)
print hc



    







