# -*- utf-8 -*-
###################################################
# 根据给定氨基酸序列,寻找相似序列
# 20190806
# To 惠真
###################################################

from sys import argv
import os

# 1.找到氨基酸文件
a = os.popen(("find {} -type f -name \"*.faa\"").format(argv[1]))
fls = a.read().split()

def obtain_acid(fl):
    with open(fl) as f1:
        acid_dict = dict()
        line = f1.readline().rstrip()
        v = ''
        k = ''
        while True:
            line = f1.readline().rstrip()
            if not line:
                break
            if line.startswith(">"):
                k = line
                continue
            v += line
            acid_dict[k] = v
        return acid_dict

for fl in fls:
    x = obtain_acid(fl)
    for k,v in x.items():
        if v.startswith(argv[2][:8]) or v.endswith(argv[2][-8:]):
            print(v,'\n','-'*30,'\n',argv[2],'\n')