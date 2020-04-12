# -*- coding: utf-8
zhidian=(
    {'English':'fruit','Chinese':'水果'},
    {'English':'apple','Chinese':'苹果'},
    {'English':'banana','Chinese':'香蕉'},
    {'English':'lemon','Chinese':'柠檬'},
)
def xians():
    for i in range(len(zhidian)):
        print('词No.{} 英文：{} 中文：{}'.format(i+1,zhidian[i]['English'], zhidian[i]['Chinese']))

def chax():
    print('请选择搜索模式\n1.英-汉\n2.汉-英\n（直接输入数字）')
    xuanz = int(input('请输入选项：'))
    if (xuanz == 1):
        Word = input('请输入搜索的词汇：')
        for i in range(len(zhidian)):
            if (Word == zhidian[i]['English']):
                print('{}:{}'.format(zhidian[i]['English'], zhidian[i]['Chinese']))
    if (xuanz == 2):
        Word = input('请输入搜索的词汇：')
        for i in range(len(zhidian)):
            if (Word == zhidian[i]['Chinese']):
                print('{}:{}'.format(zhidian[i]['Chinese'], zhidian[i]['English']))

def add():
    print('请输入要加添的词：')
    English=input('加添的单词：')
    chinese=input('加添单词的意思：')
    zhidian.update({'English': English, 'Chinese': chinese})


def update():
    print('请输入你发现的错误')
    Word = input('输入你要改的词:')
    for i in range(len(zhidian)):
        if (Word == zhidian[i]['English'] or Word == zhidian[i]['Chinese']):
            print('请输入要更改的词')
            English = input('更改的单词：')
            chinese = input('更改单词的意思：')
            zhidian[i]['English'] = English
            zhidian[i]['Chinese'] = chinese
    for i in range(len(zhidian)):
        print('词No.{} 英文：{} 中文：{}'.format(i + 1, zhidian[i]['English'], zhidian[i]['Chinese']))


def main():
    print('欢迎来到个人字典！')
    print('————————————————')
    print('请选择模式：\n1.全部输出\n2.查询单词\n3.加添单词\n4.找错更新\n5.退出程序')
    no = int(input('输入数字选项（输入数字）：'))
    if (no == 1):
        xians()
    elif (no == 2):
        chax()
    elif (no == 3):
        add()
    elif (no == 4):
        update()
    elif(no == 5):
        exit()
    else:
        main()

if __name__ == '__main__':
    while(1):
        main()