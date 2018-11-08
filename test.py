# -*- coding: utf-8 -*-
from __init__ import Pinyin
def main():
    nameList=['丁一洋']
    for name in nameList:
        print(Pinyin().get_pinyin_name(name,'','','lower'))

if __name__ == '__main__':
    main()