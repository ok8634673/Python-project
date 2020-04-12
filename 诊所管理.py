# -*- coding: utf-8
import time

person = {'小明': 0, '池面87': 87, '爽哥': 1551, '火车boy': 0, 'A': 10}
# 病人

doctor = {'内科医生': 0, '儿科医生': 0, '产科医生': 0, '全科医生': 0}
# 医生

specialty = ['surgeon', 'pediatrician', 'obstetrician', 'general practitioner']
# 医生专业

drug_fee = {'小明': 0, '池面87': 87, '爽哥': 1551, '火车boy': 0, 'A': 10}
# 药费

office_vist_fee = {'surgeon': 0, 'pediatrician': 0, 'obstetrician': 0, 'general practitioner': 0}
# 患者的诊费

print('\n欢迎来到【义务巫医诊所】\n')
time.sleep(2)

print('请问需要什么服务？\n')
time.sleep(2)

select = int(input('请选择：\n'
                   '1 查药费；\n'
                   '2 查患者的诊费；\n'
                   '3 查患者的详细信息(药费+医生信息)；\n'
                   '4 没事了\n'
                   '\n请输入：'))

if select == 1:
    while True:
        name = str(raw_input('\n请输入患者姓名：'))
        fee = drug_fee[name]
        print(str(name) + '的药费为' + str(fee) + '元\n')
        time.sleep(3)
        print('还要查ma？')
        choose = int(input('请选择：\n'
                       '1 要；\n'
                       '2 不用了；\n'
                       '3 返回上层\n'
                       '\n请输入：'))
        if choose == 1:
            continue
        if choose == 2:
            print('再见')
            break







elif select == 2:
    name = input('\n请输入患者姓名：')

elif select == 3:
    name = input('\n请输入患者姓名：')

elif select == 4:
    print('\n好的，再见')
