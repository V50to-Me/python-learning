# 螺旋填数：1~n² 顺时针螺旋填入 n×n 矩阵
# 核心：方向数组 + 试探下一步 + 右转 (d+1)%4
# 右下左上 = 0,1,2,3
n = int(input())
grid = [[0] * n for _ in range(n)]
x, y, d, num = 0, 0, 0, 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while num <= n * n:
    grid[x][y] = num
    num += 1
    nx, ny = x + dx[d], y + dy[d]
    if nx < 0 or nx >= n or ny < 0 or ny >= n or grid[nx][ny] != 0:
        d = (d + 1) % 4
        nx, ny = x + dx[d], y + dy[d]
    x, y = nx, ny

for row in grid:
    print(*row)
