M, N = map(int, input().split())
field = []
for _ in range(N):
    field.append(input())
X, Y = map(int, input().split())
if field[Y][X] == '.':
    print(0)
else:
    queue = [(X, Y)]
    visited = {(X, Y)}
    area = 0
    while queue:
        x, y = queue.pop(0)
        area += 1
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < M and 0 <= ny < N:
                if field[ny][nx] == '#' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    print(area)
