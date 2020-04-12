# -*- coding: utf-8
# 需要的变量放到开头，明显一些。
result = []  # 存起所有选择
n = 0
while True:
    a = input('A，你认罪吗？请回答认罪或者不认：')
    b = input('B，你认罪吗？请回答认罪或者不认：')
    n = n + 1
    # 需要将每一对实验者的选择存起来。

    if a == '认罪' and b == '认罪':
        print('两人都得判10年，唉\n')
        result.append('都认罪')
    elif a == '不认' and b == '认罪':
        print('A判20年，B判1年，唉\n')
        result.append('a不认b认罪')
    elif a == '认罪' and b == '不认':
        print('A判1年，B判20年\n')
        result.append('a认罪b不认')
    elif a == '不认' and b == '不认':
        print('都判3年，太棒了\n')
        result.append('都不认罪')
        break
    else:
        n = n - 1
        print('\n别捣乱，只能回答“认罪”或“不认”！\n')

print('\n第' + str(n) + '组是最优解\n')
# 打印是第几对实验者做出了最优选择。


# 通过循环打印每一对实验者的选择。
num = 1
for i in result:
    print('第' + str(num) + '组选择：' + i)
    num = num + 1


