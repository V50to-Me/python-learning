# 奶茶店窗口：单窗口先到先服务，输出每人开始被服务的时刻
# 核心：cur 表达"窗口忙到何时"，start = max(cur, t) 统一两分支，
#       (t, c, i) 三元组捆绑排序，结果按编号回填
n = int(input())
t = []
cur = 0
ans = [0] * n

for i in range(n):
    t_i, c_i = map(int, input().split())
    t.append((t_i, c_i, i))

t = sorted(t, key=lambda x: (x[0], x[2]))

for i in range(n):
    start = max(cur, t[i][0])
    cur = start + t[i][1]
    ans[t[i][2]] = start

print(*ans)
