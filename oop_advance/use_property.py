#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60
print('s.score =', s.score)
# ValueError: score must between 0 ~ 100!
s.score = 9999





练习：请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：

# -*- coding: utf-8 -*-
class Screen(object):
    @property
    def width(self):
        return self._width  #此处要使变量名与方法名区分开 否则会超出递归上限报错

    @width.setter
    def width(self, value):
        if not isinstance(value, int) and value > 0:
            raise ValueError('只能输入正整数！')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('只能输入正整数！')
        self._height = value

    @property  # 此处也要加@property 否则会返回一个方法的地址
    def resolution(self):
        return self._width * self._height
        
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
