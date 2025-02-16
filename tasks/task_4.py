import uuid
import networkx as nx
import matplotlib.pyplot as plt
from utils.helpers import Colors

def draw_heap(heap):
    tree = nx.DiGraph()
    pos = {}
    for i, val in enumerate(heap):
        node_id = str(uuid.uuid4())
        tree.add_node(node_id, color="skyblue", label=val)
        pos[node_id] = (i, -int(i / 2))
        if i != 0:
            parent_id = list(tree.nodes)[(i - 1) // 2]
            tree.add_edge(parent_id, node_id)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def task_4():
    heap = list(map(int, input(f"{Colors.BLUE}Введіть елементи купи через пробіл: {Colors.RESET}").split()))
    draw_heap(heap)