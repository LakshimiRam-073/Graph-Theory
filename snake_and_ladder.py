class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)

def BFS(graph, start, end):
    queue = [(start, 0)]  # (node, distance)
    visited = set()
    visited.add(start)

    while queue:
        node, dist = queue.pop(0)
        if node == end:
            return dist

        for neighbor in graph.adjList[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return -1  # if no path found (not expected in this case)

def findMinimumMoves(ladder, snake):
    n = 10 * 10
    edges = []
    for i in range(n):
        for j in range(1, 7):
            if i + j < n:
                src = i
                _ladder = ladder.get(i + j, 0)
                _snake = snake.get(i + j, 0)
                if _ladder or _snake:
                    dest = _ladder + _snake
                else:
                    dest = i + j
                edges.append((src, dest))

    g = Graph(edges, n)
    return BFS(g, 0, n - 1)

if __name__ == '__main__':
    ladder = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 51: 67, 72: 91, 80: 99}
    snake = {17: 7, 54: 34, 62: 19, 64: 60, 87: 36, 93: 73, 95: 75, 98: 79}
    print(findMinimumMoves(ladder, snake))
