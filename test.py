# -*- coding: utf-8 -*-
from __init__ import Pinyin
def main():
    nameList=['解老板','单田芳','爱新觉罗·玄烨','都教授']
    for name in nameList:
        print(Pinyin().get_pinyin_name(name,'~','marks','capitalize'))

if __name__ == '__main__':
    main()