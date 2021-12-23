#!/usr/bin/env python3

import networkx as nx

prices=[
    0,
    446, 358, 704, 514, 298,
    214, 697, 526, 225, 471,
    853, 151, 584, 387, 953,
    685, 188, 489, 285, 498,
    397, 295, 926, 405, 382,
    678, 486, 341, 816, 509,
    839, 570, 189, 287, 646,
    385, 768, 415, 163, 307,
    964, 137, 501, 470, 0
]

Graph = nx.DiGraph()
for k,v in enumerate(prices):
    Graph.add_node(k, price=v)

Graph.add_edge(0, 1)
Graph.add_edge(0, 2)
Graph.add_edge(0, 3)
Graph.add_edge(0, 4)
Graph.add_edge(0, 5)

for i in range(1, 40):
    mod = i % 10
    if mod == 1 or mod == 5:
        Graph.add_edge(i, i + 10) #2つ下のノードへ
    Graph.add_edge(i, i + 5) #下のノードへ
    if mod <= 4:
        Graph.add_edge(i, i + 1) #右のノードへ
    if mod >= 7 or mod == 0:
        Graph.add_edge(i, i - 1) #左のノードへ
    if mod != 1 and mod != 6:
        Graph.add_edge(i, i + 4) #左下のノードへ
    if mod != 0 and mod != 5:
        Graph.add_edge(i, i + 6) #右下のノードへ
Graph.add_edge(41, 42)
Graph.add_edge(42, 43)
Graph.add_edge(43, 44)
Graph.add_edge(44, 45)

nodes = Graph.nodes(data=True)

for path in nx.all_simple_paths(Graph, source=0, target=45):
    sum = 0
    for n in path:
        sum = sum + nodes[n]['price']
    if sum == 10000:
        print("path: {}, sum:{}".format(path, sum))

