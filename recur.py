#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 利用递归函数计算阶乘
# N! = 1 * 2 * 3 * ... * N
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print('fact(1) =', fact(1))
print('fact(5) =', fact(5))
print('fact(10) =', fact(10))

# 利用递归函数移动汉诺塔:
# 认识汉诺塔的目标：把A柱子上的N个盘子移动到C柱子
# 递归的思想就是把这个目标分解成三个子目标
# 子目标1：将前n-1个盘子从a移动到b上
# 子目标2：将最底下的最后一个盘子从a移动到c上
# 子目标3：将b上的n-1个盘子移动到c上
# 然后每个子目标又是一次独立的汉诺塔游戏，也就可以继续分解目标直到N为1
# move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法

def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b) #子目标1
        move(1, a, b, c) #子目标2
        move(n-1, b, a, c) #子目标3
move(4, 'A', 'B', 'C')
 
 -------------------------------------
 过程：
 move(3,a,b,c) 
    move(2,a,c,b)
              move(1,a,b,c) //A->C
              move(1,a,c,b) //A->B
              move(1,c,a,b) //C->B
    move(1,a,b,c)         //A->C
    move(2,b,a,c) 
              move(1,b,c,a) //B->A
              move(1,b,a,c) //B->C
              move(1,a,b,c) //A->C


