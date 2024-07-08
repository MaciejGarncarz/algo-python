import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
from typing import List, Dict

def create_graph(board: List[List[int]]) -> Dict[int, List[int]]:
    n = len(board)
    maxTile = n * n
    graph = defaultdict(list)
    
    # Create a numbered board to map each index to its board value
    numberedBoard = [0] * (maxTile + 1)
    label = 1
    for row in range(n - 1, -1, -1):
        tiles = board[row]
        if (n - row) % 2 == 0:
            tiles.reverse()
        
        for tile in tiles:
            numberedBoard[label] = tile
            label += 1

    # Build the graph
    for current in range(1, maxTile + 1):
        for dice in range(1, 7):
            next_pos = current + dice
            if next_pos <= maxTile:
                if numberedBoard[next_pos] != -1:
                    graph[current].append(numberedBoard[next_pos])
                else:
                    graph[current].append(next_pos)
    return graph


# how the graph should look like:
# 1 -> [15, 3, 4, 5, 6, 7]
# where 1 is a node
# array is node that are connected to 1



def visualize_graph(graph: Dict[int, List[int]]):
    G = nx.DiGraph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    
    pos = nx.spring_layout(G)
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", arrowsize=20)
    plt.title("Snakes and Ladders Graph Visualization")
    plt.show()

# Define the board
board = [
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 35, -1, -1, 13, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 15, -1, -1, -1, -1]
]

# Create and visualize the graph
graph = create_graph(board)
visualize_graph(graph)
