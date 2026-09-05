# 约瑟夫环：n 人围圈报数，报到 m 出列，输出出列顺序
# 核心：当前指针 + 取模回绕 + 删完不动下标
n, m = map(int, input().split())
alive = [x + 1 for x in range(n)]
i = 0
order = []

while alive:
    i = (i + m - 1) % len(alive)
    order.append(alive[i])
    alive.pop(i)

print(*order)
