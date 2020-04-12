# -*- coding: utf-8
print('关于爽哥\n')
while True:
    q1 = raw_input('第一问：爽哥的ID是什么？\n')
    if q1 != 'ywwuyi':
        continue
    print('\n答对了，下面是第二问：')
    q2 = raw_input('爽哥的斗鱼直播间是多少？\n')
    if q2 != '6655':
        continue
    print('\n答对了，下面是第三问：')
    q3 = raw_input('爽哥的老鼠台ID是什么？\n')
    if q3 != 'wuyikoei':
        continue
    print('\n答对了，下面是第四问：')
    q4 = raw_input('爽哥的头像是谁？\n')
    if q4 == '堕天使芙蓉':
        break
print('都答对了，你是爽粉。')