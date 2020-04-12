# coding=utf-8
import time
from decimal import Decimal
from decimal import getcontext
print('\n编写by梁健丰\n')
time.sleep(2)

print('故事背景：\n')
time.sleep(2)

print('接受了霍格沃茨来信的你，带着欣喜与好奇，\n'
      '跟着魔咒学老师吴枫教授，来到了巫师世界的对角巷。\n'
      '在这个相当于人类集市的对角巷，你立刻被魔法世界稀奇古怪的东西吸引，想掏手机刷花呗买买买。\n')
time.sleep(6)

print('但是吴枫教授说，麻瓜（没有魔法的人）货币在魔法世界不流通，\n'
      '但是你可以去巫师世界的银行——古灵阁兑换货币。\n'
      '你立刻跟着吴枫老师跑到了古灵阁。当你进到巫师世界的银行时，\n'
      '就有银行的小精灵职员问好：\n')
time.sleep(6)

answer = int(input('请问您需要什么帮助呢？\n\n'
                   '1 存取款；\n'
                   '2 货币兑换；\n'
                   '3 咨询；\n'
                   '4 没事了\n'
                   '\n请输入：'))

if answer == 1:
    print('\n小精灵会推荐你去存取款窗口')

elif answer == 3:
    print('\n小精灵会推荐你去咨询窗口')

elif answer == 4:
    print('\n好的，再见')

elif answer == 2:
    print('\n金加隆和人民币的兑换率为1:51.3，\n即一金加隆=51.3人民币\n请问您需要兑换多少金加隆呢？\n')

    exchange = input('请输入需要的金加隆: ')

    print('\n好的，我知道了，您需要兑换' + str(exchange) + '金加隆。')

    need = Decimal(exchange) * Decimal('51.3')

    print('\n那么，您需要付给我' + str(need) + '人民币.')
