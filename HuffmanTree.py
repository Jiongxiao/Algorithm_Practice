class HTNode():
    def __init__(self):
        self.parent=None
        self.lchild=None
        self.rchild=None
        self.weight=None

w=[0,10,7,8,2]

def HuffmanCoding(w,n):
    m=2*n
    p=HTNode()
    ht=[p]*m
    for i in range(1,n+1):
        ht[i].weight=w[i]
        ht[i].lchild=ht[i].rchild=ht[i].parent=0
    for i in range(n+1,m):
        ht[i].weight=ht[i].lchild=ht[i].rchild=ht[i].parent=0
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
    







