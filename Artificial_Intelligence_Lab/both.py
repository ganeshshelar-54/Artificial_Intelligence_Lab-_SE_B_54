from collections import deque

def find_start_end(maze):
    start = None
    end = None
    for r, row in enumerate(maze):
        for c, val in enumerate(row):
            if val == 'S':
                start = (r, c)
            elif val == 'E':
                end = (r, c)
    return start, end

def is_valid(r, c, rows, cols, maze, visited):
    return (0 <= r < rows and 0 <= c < cols and
            maze[r][c] != '#' and (r, c) not in visited)

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(maze):
    rows, cols = len(maze), len(maze[0])
    start, end = find_start_end(maze)
    if not start or not end:
        return None

    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == end:
            return path

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc, rows, cols, maze, visited):
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))
    return None

def dfs(maze):
    rows, cols = len(maze), len(maze[0])
    start, end = find_start_end(maze)
    if not start or not end:
        return None

    stack = [(start, [start])]
    visited = set([start])

    while stack:
        (r, c), path = stack.pop()
        if (r, c) == end:
            return path

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc, rows, cols, maze, visited):
                visited.add((nr, nc))
                stack.append(((nr, nc), path + [(nr, nc)]))
    return None

def print_path(maze, path):
    if not path:
        print("No path found")
        return
    
    maze_copy = [list(row) for row in maze]

    for r, c in path:
        if maze_copy[r][c] not in ('S', 'E'):
            maze_copy[r][c] = '*'

    for row in maze_copy:
        print(''.join(row))


# Example usage:
maze = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', 'E', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]

print("BFS path:")
bfs_path = bfs(maze)
print_path(maze, bfs_path)

print("\nDFS path:")
dfs_path = dfs(maze)
print_path(maze, dfs_path)


