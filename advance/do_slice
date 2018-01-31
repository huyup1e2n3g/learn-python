# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：

# -*- coding: utf-8 -*-
def trim(s):

# 1
while s[0:1]==' ':
    s=s[1:]
while s[-1:]==' ':
    s=s[0:-1]
return s

# 2 
if s == '':
    return ''
if s[0] == ' ':
    return trim(s[1:])
elif s[-1] == ' ':
    return trim(s[:-1])
else:
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
