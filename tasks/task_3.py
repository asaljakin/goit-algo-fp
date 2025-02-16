import heapq
from utils.helpers import Colors

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    heap = [(0, start)]
    while heap:
        current_distance, current_vertex = heapq.heappop(heap)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    return distances

def task_3():
    graph = {}
    vertices = input(f"{Colors.BLUE}Введіть вершини графа через пробіл: {Colors.RESET}").split()
    for vertex in vertices:
        graph[vertex] = {}
        edges = input(f"{Colors.CYAN}Введіть сусідів вершини {vertex} та ваги ребер (наприклад, B 5 C 10): {Colors.RESET}").split()
        for i in range(0, len(edges), 2):
            neighbor = edges[i]
            weight = int(edges[i + 1])
            graph[vertex][neighbor] = weight

    start_vertex = input(f"{Colors.BLUE}Введіть початкову вершину: {Colors.RESET}")
    distances = dijkstra(graph, start_vertex)
    
    print(f"\n{Colors.YELLOW}Граф:{Colors.RESET}")
    for vertex in graph:
        print(f"{Colors.GREEN}{vertex}:{Colors.RESET} {graph[vertex]}")
    
    print(f"\n{Colors.YELLOW}Найкоротші шляхи від вершини {start_vertex}:{Colors.RESET}")
    for vertex, distance in distances.items():
        print(f"{Colors.GREEN}{vertex}{Colors.RESET}: {distance}")
