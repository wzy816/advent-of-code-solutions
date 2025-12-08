import os

import networkx as nx
import heapq
import math

def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    h = []
    nodes = []
    for d in data:
        x,y,z = map(int,d.split(","))
        n = (x,y,z)

        if len(nodes) > 0:
            for n1 in nodes:
                x1,y1,z1 = n1 
                dist = (x1-x)**2+ (y1-y)**2+ (z1-z)**2
                heapq.heappush(h, (dist,n,n1))

        nodes.append((x,y,z))


    g = nx.Graph()
    g.add_nodes_from(nodes)

    while nx.number_connected_components(g) > 1:
        d,n1,n2 = heapq.heappop(h)
        g.add_edge(n1,n2)
    
    print(n1[0] * n2[0])

 
    
if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
