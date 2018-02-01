# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：

# -*- coding: utf-8 -*-
def findMinAndMax(L):

if L == []: 
        return (None, None)
    else:
        max = L[0]
        min = L[0]
        for m in L:            
            if max < m:
                max = m            
            if min > m:
                min = m
        return (min, max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
