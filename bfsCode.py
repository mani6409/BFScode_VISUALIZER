# bfs.py

class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    def is_empty(self):
        return self.items == []

def bfs(graph, start):
    visited = {}
    level = {}
    traversal = []

    # initialize
    for node in graph:
        visited[node] = False
        level[node] = -1

    q = Queue()
    visited[start] = True
    level[start] = 0
    q.enqueue(start)

    while not q.is_empty():
        current = q.dequeue()
        traversal.append(current)

        # check neighbors
        for neighbor in graph[current]:
            if visited[neighbor] == False:
                visited[neighbor] = True
                level[neighbor] = level[current] + 1
                q.enqueue(neighbor)

    return traversal, level

if __name__ == "__main__":
    # Example graph
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start_node = 'A'
    traversal_order, levels = bfs(graph, start_node)

    print("BFS traversal starting at", start_node, ":", traversal_order)
    print("Levels (distance from start):", levels)

    # Save results to JSON
    import json
    output_data = {
        "graph": graph,
        "start": start_node,
        "traversal": traversal_order,
        "levels": levels
    }
    with open("bfs_output.json", "w") as f:
        json.dump(output_data, f, indent=4)

    print("Results saved to bfs_output.json")
