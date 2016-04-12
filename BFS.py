from collections import deque

class BFSResult:
    def __init__(self):
        self.level={}
        self.parent={}

class Graph:
    def __init__(self):
        self.adj={}

    def add_edge(self,u,v):
        if u not in self.adj:
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
        if u in graph.adj:
            for n in graph.adj[u]:
                if n not in r.level:
                    queue.append(n)
                    r.parent[n]=u
                    r.level[n]=r.level[u]+1
    return r

graph=Graph()
graph.add_edge('A','B')
graph.add_edge('A','C')
graph.add_edge('A','D')
graph.add_edge('B','D')
graph.add_edge('C','D')
graph.add_edge('C','E')
graph.add_edge('C','F')
graph.add_edge('F','E')
graph.add_edge('D','F')
graph.add_edge('F','E')
graph.add_edge('E','G')

r=bfs(graph,'A')
