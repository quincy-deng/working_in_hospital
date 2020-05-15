###########################################
# 比较基因在两组存在个数的差异,设定区间输出表格.
###########################################

from sys import argv
import os
from functools import reduce
from collections import Counter

def add(x,y):
    return x+y

def gene_list(fl):
    with open(fl) as F:
        ls1 = F.read().split('/gene=\"')[1:]
        genes = [i.split('\"')[0].split('_')[0] for i in ls1]
        return list(set(genes))

#来一个根据value排序的，先把item的key和value交换位置放入一个list中，再根据list每个元素的第一个值，即原来的value值，排序：
def sort_by_value(d):
    items=d.items()
    backitems=[[v[1],v[0]] for v in items]
    backitems.sort()
    return backitems


group1_gbks,group2_gbks = argv[1],argv[2]
f = lambda x: os.popen('ls {}/*.gbk'.format(x)).readlines()
gbks1,gbks2 =f(group1_gbks),f(group2_gbks)
gbks1,gbks2 = list(map(str.strip,gbks1)),list(map(str.strip,gbks2))

group1 = Counter(list(reduce(add,map(gene_list,gbks1))))
group2 = Counter(list(reduce(add,map(gene_list,gbks2))))

fls1,fls2 = len(gbks1),len(gbks2)
for i,j in group1.items():
    group1[i] = j/fls1

for i,j in group2.items():
    group2[i] = j/fls2

chayi = dict()
for gene,count in group1.items():
    if gene not in group2:
        chayi[gene] = count
    else:
        chayi[gene] = count - group2[gene]

x = sort_by_value(chayi)[::-1]

y = list(map(lambda n: n[1] + '\t' +str(int(group1[n[1]]*fls1))+ '\t' +str(int(group2[n[1]]*fls2))+ '\t' + str(round(n[0],2)),x))

with open('3176和其他差异统计.csv','w') as O:
    O.write('\t'.join(['Gene','CT3176({})'.format(fls1),'orthers({})'.format(fls2),'差异'])+'\n')
    O.write('\n'.join(y))