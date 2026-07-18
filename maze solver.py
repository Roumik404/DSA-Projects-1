import random
from collections import deque

def generate_maze(rows, cols, density=0.3):
    maze = [[0 if random.random() > density else 1 for _ in range(cols)] for _ in range(rows)]
    maze[0][0] = 0  
    maze[rows-1][cols-1] = 0  
    return maze

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    q = deque([(start, [start])])
    visited = set([start])
    while q:
        (x, y), path = q.popleft()
        if (x, y) == end:
            return path
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append(((nx, ny), path+[(nx, ny)]))
    return None

def dfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    stack = [(start, [start])]
    visited = set([start])
    while stack:
        (x, y), path = stack.pop()
        if (x, y) == end:
            return path
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                stack.append(((nx, ny), path+[(nx, ny)]))
    return None

def print_maze(maze, path=None):
    rows, cols = len(maze), len(maze[0])
    path_set = set(path) if path else set()
    for r in range(rows):
        line = ""
        for c in range(cols):
            if (r,c) in path_set:
                line += "* "
            elif maze[r][c] == 1:
                line += "# "
            else:
                line += ". "
        print(line)

def main():
    rows = int(input("Enter maze rows: "))
    cols = int(input("Enter maze cols: "))
    density = float(input("Enter wall density (0-1, e.g. 0.3): "))
    maze = generate_maze(rows, cols, density)
    start, end = (0,0), (rows-1, cols-1)

    print("\nGenerated Maze:")
    print_maze(maze)
    
    print("\n--- Maze Solver ---")
    print("Choose algorithm: 1. BFS  2. DFS")
    choice = input("Enter choice: ")

    path = bfs(maze, start, end) if choice == "1" else dfs(maze, start, end)
    algo = "BFS" if choice == "1" else "DFS"

    if path:
        print(f"\n{algo} Path found ({len(path)} steps): {path}")
        print("\nMaze visualization:")
        print_maze(maze, path)
    else:
        print("No path found!")

if __name__ == "__main__":
    main()
