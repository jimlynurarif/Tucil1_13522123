def generate_patterns(n, m, max_len):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, left, down, up directions
    patterns = []

    def dfs(x, y, path, direction_index):
        if len(path) > max_len:
            return
        patterns.append(path[:])
        for i in range(2):
            dx, dy = directions[direction_index + i]
            nx, ny = x + dx, y + dy 
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in path:
                path.append((nx, ny))
                dfs(nx, ny, path, (direction_index + 2) % 4)  # Alternate between vertical and horizontal
                path.pop()

    for i in range(m):
        dfs(0, i, [(0, i)], 2)  # Start with downward movement, 2 is the index of downward movement, see directions array

    return patterns

# Testing
n, m, max_len = 4, 4, 8
print(generate_patterns(n, m, max_len))
