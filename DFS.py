from collections import deque

class DFSResult:
    def __init__(self):
        self.parent={}
        self.start_time={}
        self.finish_time={}
        self.edges={}
        self.order=[]
        self.t=0

class Graph:
    def __init__(self):
        self.adj={}

    def add_edge(self,u,v):
        if u not in self.adj:
            self.adj[u]=[]
        self.adj[u].append(v)

    def itervertices(self):
        return self.adj.iterkeys()


def dfs(g):
    results=DFSResult()
    for vertex in g.itervertices():
        if vertex not in results.parent:
            dfs_visit(g,vertex, results)
    return results

def dfs_visit(g,v,results,parent=None):
    # print v
    results.parent[v]=parent
    results.t+=1
    results.start_time[v]=results.t
    if parent:
        results.edges[(parent, v)]='tree'


    if v in g.adj:
        for n in g.adj[v]:
            if n not in results.parent: # n is not visited
                dfs_visit(g,n,results,v)
            elif n not in results.finish_time: # cool
                results.edges[(v,n)]='back'
            elif results.start_time[v]<results.start_time[n]:
                results.edges[(v,n)]='forward'
            else: results.edges[(v,n)]='cross'
    results.t+=1
    results.finish_time[v]=results.t
    results.order.append(v)

graph=Graph()
for edge in [('A','B'),('B','C'),('C','F'),('C','D'),('D','E'),('D','F'),('A','G'),('G','C'),('C','A')]:
    graph.add_edge(edge[0],edge[1])

result=dfs(graph)
