######################################################
# 2019.5.6
# 整理搜集临床数据需要的表格,本次送测100个samples
######################################################

import os
table1=r'F:\2017-2018年铜绿-需送测样本(最终版).csv'
table2=r'F:\待整理样本.csv'
table3=r'F:\送测样本编号.csv'
table4=r'F:\铜绿-已提取样本.csv'

# 1)替换后来自己编的号为样本编号
ids = [i.rstrip() for i in open(table3).readlines()]
ids2 = {i.rstrip().split()[1]:i.rstrip().split()[0] for i in open(table4).readlines() if len(i.rstrip().split())>1}
def replace(i,index):
    if i in ids2:
        ids[index] = ids2[i]
[replace(i,index) for index,i in enumerate(ids)]
# ids

# 2) 待整理表格
cols = ['送检日期']+open(table2,encoding='utf-8').read().rstrip().split()

# 3) 从原始表格提取信息

def collection(line):
    t = line.rstrip().split()
    if t[0] in ids:
        return [t[4],t[0],t[1],'','',t[6],t[5]]+['']*13
    else:
        return 1

with open(r'F:\20190506.KP_Clinical-data.csv','w') as out:
    out.write('\t'.join(cols)+'\n')
    [out.write('\t'.join(collection(line))+'\n') for line in open(table1,encoding='utf-8').readlines()[1:] if collection(line) != 1]
