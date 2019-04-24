"""
    写一个猜数字的游戏，随机生成一个1~100的整数，让用户输入数字进行猜测，猜大了或者猜小了要有对应的提示，猜对了则退出游戏。
    需要添加异常处理，如果用户输入的不是数字，要求程序不能中断，提示用户”请输入正确的数字”,程序继续执行。
	随机数使用random模块的randomint(start,end)函数
"""
import random

while True:
    num = random.randint(1, 100)
    print('随机数:%s' % num)
    ok = """
        ----- 恭喜！猜对了！-----
        ----- 奖励一朵小红花 ----
        """

    try:
        inp = int(input('猜数字游戏，请输入数字:'))
    except (ValueError, NameError):
        print('输入错误，请重新输入...')
        continue

    if inp > num:
        print('猜大了')
    elif inp < num:
        print('猜小了哦')
    elif inp == num:
        print('%s' % ok)
        break
