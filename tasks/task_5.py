import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from utils.helpers import Colors

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color="skyblue", label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, traversal_type="DFS"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    if traversal_type == "DFS":
        nodes, traversal_order = dfs_traversal(tree_root)
    else:
        nodes, traversal_order = bfs_traversal(tree_root)

    for i, node_id in enumerate(nodes):
        tree.nodes[node_id]['color'] = color_gradient(i, len(nodes))

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    return tree, pos, colors, labels, traversal_order

def color_gradient(index, total):
    factor = index / total
    color = plt.cm.plasma(factor)
    return "#{:02x}{:02x}{:02x}".format(int(color[0]*255), int(color[1]*255), int(color[2]*255))

def dfs_traversal(root):
    stack = [root]
    visited = set()
    order = []
    traversal_order = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node.id)
            traversal_order.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return order, traversal_order

def bfs_traversal(root):
    queue = deque([root])
    visited = set()
    order = []
    traversal_order = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node.id)
            traversal_order.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return order, traversal_order

def task_5():
    root = Node(int(input(f"{Colors.BLUE}Введіть корінь дерева: {Colors.RESET}")))
    queue = deque([root])
    while queue:
        current = queue.popleft()
        left_val = input(f"{Colors.BLUE}Введіть ліве піддерево для {current.val} (або Enter, якщо немає): {Colors.RESET}")
        if left_val:
            current.left = Node(int(left_val))
            queue.append(current.left)
        right_val = input(f"{Colors.BLUE}Введіть праве піддерево для {current.val} (або Enter, якщо немає): {Colors.RESET}")
        if right_val:
            current.right = Node(int(right_val))
            queue.append(current.right)

    print(f"{Colors.GREEN}DFS обхід:{Colors.RESET}")
    tree, pos, colors, labels, dfs_order = draw_tree(root, "DFS")
    print(" -> ".join(map(str, dfs_order)))
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

    print(f"{Colors.GREEN}BFS обхід:{Colors.RESET}")
    tree, pos, colors, labels, bfs_order = draw_tree(root, "BFS")
    print(" -> ".join(map(str, bfs_order)))
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()