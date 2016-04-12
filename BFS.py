from collections import deque

class BFSResult:
    def __init__(self):
        self.level={}
        self.parent={}

class Graph:
    def __init__(self):
        self.adj={}

    def add_edge(self,u,v):
        if not self.adj[u]:
            self.adj[u]=[]
        self.adj[u].append(v)

def bfs(graph,s):
    r=BFSResult()
    r.parent={s:None}
    r.level={s:0}

    queue=deque()
    queue.append(s)

    while queue:
        u=queue.popleft()
        for n in graph.adj[u]:
            if n not in level:
                queue.append(n)
                r.parent[n]=u
                r.level[n]=r.level[u]+1
    return r
