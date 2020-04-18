# python 3.8
# -*- coding: utf-8

scores = [91, 95, 97, 99, 92, 93, 96, 98]

n = len(scores)
s = 0
for i in range(n):
    t = scores[i]
    s = t + s

p = s / n
print('平均分为：{}'.format(p))
list = []
for i in range(n):
    x = scores[i]
    if x < p:

        list.append(x)

print(list)


