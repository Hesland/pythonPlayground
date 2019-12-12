#!/usr/bin/env python3
#coding=utf-8

def test1():
    str = '''
    python中，字符串中的转义字符是同样适用的
    如果多行字符串前添加 r，则代表前方添加…(为啥没卵用)
    '''
    
    print(str)

    print(r'''hello,\n
    world''')

#test1()

def test2():
    str = 'Hello, %s' % 'world'
    print(str)
    
def test3(a, b):
    if not isinstance(a,(int, float)):
        raise TypeError('bad operand type about \'a\'')
    elif not isinstance(b, (int, float)):
        raise TypeError('bad operand type about \'b\'')
    a = int(a)
    b = int(b)
    str = '%s + %s = %s' % (a, b, a + b)
    print(str)
    
#test2()

#如果这里输入的 a, b 其中存在一个不是可计算的数类型，就会出现报错，因此需要某个函数来判断当前变量的类型来做出来容错处理
#test3(3, 'p')
#test3(3, 5)

# [NSString stringWithFormat:@""]; 类似 oc 中 字符串 format 配置
def test4(string):
    str = '我默认的字符串变量，后面需要加上{0}，以及{1}'.format('字符串的第一部分', string)
    print(str)
    
#test4('我真正想说的话')

def test5():
    arr = ['string1', 'string2', 'string3']
    print('打印数组，即 python 中的 list结构: \n',arr[0] , arr[1], arr[2])
    print('倒着也能打印: \n', arr[-1], arr[-2], arr[-3])
    
    text = '''
    arr = ['string1', 'string2', 'string3']
    print('打印数组，即 python 中的 list结构: \n',arr[0] , arr[1], arr[2])
    print('倒着也能打印: \n', arr[-1], arr[-2], arr[-3])
    
    注解:python 中的 list 是类似于 OC 中的 NSMutableArray 的；同样的，python 中的 tuple(元组) 是类似于 OC 中的 NSArray 的。
    tuple初始化后即确定，不可再扩容，不可对内部元素进行翻转等任何操作，但可以更改内部元素，这种更改的本质是指针的指向发生了变化
    '''
    print('code文本:\n', text)
#    同样要意识到数组越界是很严重的问题就是了

#test5()

def testJudgeAndCycle(index):
    #断言数据类型，或者作出判断和修正
    if not isinstance(index, (int, float)):
        raise TypeError('bad operand type')
    
    
    print('----------------------')
    while index < 5:
        print(index)
        if index % 2 == 0:
            print('index 是偶数')
        elif index % 2 == 2:
            print('这种结果不可能')
        else:
            print('index 是奇数')
        index = index + 1
        print('----------------------')
        
    print('index 不符合循环条件，结束')
    
#testJudgeAndCycle('0')
#testJudgeAndCycle(-3)

#自定义绝对值函数 & python中三目运算的具体应用
def zr_abs(num):
    return (num if(num > 0) else(-num))
    
#print(zr_abs(-5))
            
'''
print('%s---%s' % (int, float))
打印结果:
<class 'int'>---<class 'float'>
'''
    
#验算 & 求解一元二次方程
import math

def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('a必须是一个数字')
    if not isinstance(b, (int, float)):
        raise TypeError('b必须是一个数字')
    if not isinstance(c, (int, float)):
        raise TypeError('c必须是一个数字')

    judge = b ** 2 - 4 * a * c
    
    if judge < 0:
#        print('方程{0}x^2 + {1}x + {2} = 0无实根!'.format(a, b, c))
        return '不存在的'
    else:
        return (((-b + math.sqrt(judge))/ （2 * a）), ((-b - math.sqrt(judge))/ （2 * a）))

print('x^2 + 2x + 1 = 0的实数解是:\n', quadratic(1, 2, 1))
print('x^2 + 2x + 5 = 0的实数解是:\n', quadratic(1, 2, 5))


    

