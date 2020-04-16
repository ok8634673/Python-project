# -*- coding: utf-8

import time, random

player_victory = 0
enemy_victory = 0
i = 0
while player_victory < 2 and enemy_victory < 2:
    i += 1
    print('\n目前比分： %s 比 %s \n' % (player_victory,enemy_victory))
    time.sleep(2)  # 让局与局之间有较明显的有时间间隔
    print(' \n——————现在是第' + str(i) + '局——————')  # 作为局的标记

    player_life = random.randint(100, 150)
    player_attack = random.randint(30, 50)
    enemy_life = random.randint(100, 150)
    enemy_attack = random.randint(30, 50)

    # 展示双方角色的属性
    print('【玩家】\n 血量：%s \n攻击：%s' % (player_life,player_attack))
    print('------------------------')
    time.sleep(1)
    print('【敌人】\n 血量：%s \n攻击：%s' % (enemy_life,enemy_attack))
    print('------------------------')
    time.sleep(1)

    # 双方PK
    while player_life > 0 and enemy_life > 0:
        player_life = player_life - enemy_attack
        enemy_life = enemy_life - player_attack
        print('你发起了攻击，【敌人】剩余血量' + str(enemy_life))
        print('敌人向你发起了攻击，【玩家】剩余血量' + str(player_life))
        print('-----------------------')
        time.sleep(1.5)

    # 打印最终战果
    if player_life > 0 and enemy_life <= 0:
        print('敌人死翘翘了，你赢了！')
        player_victory += 1
        while player_victory == 2:
            break
    elif player_life <= 0 and enemy_life > 0:
        print('悲催，敌人把你干掉了！')
        enemy_victory += 1
        while enemy_victory == 2:
            break
    else:
        print('哎呀，你和敌人同归于尽了！')

# 判断最终结果
if player_life > enemy_life:
    print('\n玩家胜利\n')
    print('结果：%s比%s' % (player_victory,enemy_victory))

else:
    print('\n敌人\n')
    print('结果：%s比%s' % (player_victory,enemy_victory))