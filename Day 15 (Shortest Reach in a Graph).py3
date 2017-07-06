

class Graph():
    def __init__(self, n):
        self.nodes={}
        for i in range(n):
            self.nodes[i]=set()
    def connect(self, x, y):
        self.nodes[x].add(y)
        self.nodes[y].add(x)
    def find_all_distances(self, s):
        edge_distance=6
        curr_nodes=[s]
        next_nodes=[]
        shortest_distances={}
        curr_length=0
        while True:
            if curr_nodes==[] and next_nodes==[]:
                break
            if curr_nodes==[]:
                curr_nodes=next_nodes
                curr_length+=edge_distance
                next_nodes=[]
            this_node=curr_nodes.pop()
            if this_node in shortest_distances:
                continue
            else:
                shortest_distances[this_node]=curr_length
                for x in self.nodes[this_node]:
                    next_nodes.append(x)
        result=""
        for i in range(len(self.nodes)):
            if i==s:
                continue
            if i in shortest_distances:
                result+=str(shortest_distances[i])+' '
            else:
                result+='-1 '
        print(result)

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1)
    s = int(input())
    graph.find_all_distances(s-1)
