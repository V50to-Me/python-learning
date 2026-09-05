# 扫地机器人：网格 + 障碍 + F/L/R 指令，输出终点
# 核心：方向可变（左转 (d+3)%4）、先查边界再碰格子、行对应 n 列对应 m
# 右下左上 = 0,1,2,3
n, m = map(int, input().split())
grid = []
for row in range(n):
    grid.append(list(input()))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y, d = input().split()
x = int(x) - 1
y = int(y) - 1
order = list(input())

if d == 'R':
    d = 0
elif d == 'D':
    d = 1
elif d == 'L':
    d = 2
elif d == 'U':
    d = 3

for s in order:
    if s == 'F':
        nx, ny = x + dx[d], y + dy[d]
        if nx >= 0 and nx < n and ny >= 0 and ny < m and grid[nx][ny] == '.':
            x, y = nx, ny
    elif s == 'L':
        d = (d + 3) % 4
    elif s == 'R':
        d = (d + 1) % 4

print(x + 1, y + 1)
