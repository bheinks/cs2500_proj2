#!/usr/bin/env python3

import random
from sys import argv

import networkx as nx


def init_graph(gml, weight, K):
    graph = nx.read_gml(gml)

    for u, v, d in graph.edges(data=True):
        d["weight"] = random.randint(*weight)

    #graph.add_node('S')
    #for i in range(K):
    #    rand_node = random.choice(graph.nodes())

    return graph


def main(gml, weight):
    graph = init_graph(gml, [1, 20], 50)
    print(graph["Rolla"])


if __name__ == "__main__":
    if len(argv) == 2:
        main(argv[1], [1, 20])
    else:
        print("Usage: ./main.py file.gml")
