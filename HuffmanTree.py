class HTNode():
    def __init__(self):
        self.parent=None
        self.lchild=None
        self.rchild=None
        self.weight=None

def HuffmanCoding(w,n):
    m=2*n-1
    p=HTNode()
    ht=[p]*m