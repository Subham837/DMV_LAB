import networkx as nx
import matplotlib.pyplot as plt

n = int(input("Enter number of vertices (>3): "))

if n > 3:
    G = nx.complete_graph(n)
    nx.draw(G, with_labels=True, node_color="lightblue", node_size=1000)
    plt.show()
else:
    print("Number must be greater than 3")
