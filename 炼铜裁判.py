# -*- coding: utf-8

while True:
    a = raw_input('A，你炼铜ma？请回答炼或者不炼：\n')
    b = raw_input('B，你炼铜ma？请回答炼或者不炼：\n')
    if a == '不炼' and b == '不炼':
        print('两人都得判10年，唉')
    elif a == '不炼' and b == '炼':
        print('A判20年，B判1年，唉')
    elif a == '炼' and b == '不炼':
        print('A判1年，B判20年')
    elif a == '炼' and b == '炼':
        print('都判3年，太棒了')
        break
    else:
        print('别捣乱，只能回答“炼”或“不炼”！')