#!/usr/bin/env python3
#coding=utf-8

import math

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
        return (((-b + math.sqrt(judge))/(2 * a)), ((-b - math.sqrt(judge))/(2 * a)))

print('x^2 + 2x + 1 = 0的实数解是:\n', quadratic(1, 2, 1))
print('x^2 + 2x + 5 = 0的实数解是:\n', quadratic(1, 2, 5))
