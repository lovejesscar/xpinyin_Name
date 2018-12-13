# -*- coding: utf-8 -*-
from __init__ import Pinyin
domain = u'@qdbankchina.com'
nameFilePath = 'E:\\KD Files\\Desktop\\name.txt'
def main():

    #nameList=['闫晶莹','吕思佳','郑真真','刘彩艳','张悦','邵莹','李昕怡','吕珊','姜晓萍','李海娇','吴秋月','赵雪芳','苏丹','陈平','万玉艺','孙政']

    nameList=[]
    with open(nameFilePath) as f:
        for name in f:
            nameList.append(name.strip())

    totolnum = 0
    for name in nameList:
        totolnum = totolnum+1
        print(name,Pinyin().get_pinyin_name(name,'','','lower').strip(),'<'+Pinyin().get_pinyin_name(name,'','','lower').strip()+domain+'>')
    print("完成，共处理"+str(totolnum)+'个账户')
if __name__ == '__main__':
    main()