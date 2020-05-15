###################################################
# 20190514
# 从gbk或者gbff文件搜索acid序列
# NCBI下载数据查询氨基酸序列
###################################################
import os
from sys import argv
import datetime

today = str(datetime.date.today())[4:]
gene = os.listdir(os.listdir)
def read_acid(i):
    path=os.path.join(argv[2],i)+'.acid'
    return open(path).read()
acidseq = ['/translation=\"'+read_acid(i).replace('\n','').replace(' ','')+'\"' for i in gene]
print(acidseq)

a = os.popen(("find {} -name \"*.gbff.gz\"").format(argv[1]))
fls = a.read().split()

def read_gbff(fl):
    return os.popen('zcat {}'.format(fl)).read().replace('\n','').replace(' ','').replace('\t','')
def search_acid(fl,acid):
    if read_gbff(fl).find(acid)!=-1:
        return '1'
    else:
        return '0' 

with open('{}.txt'.format(today),'w') as f:
    f.write('\t'.join(['SAMPLE']+gene)+'\n')
    for index,fl in enumerate(fls):
        x = [search_acid(fl,i) for i in acidseq]
        print(x)
        sample = fl.split('/')[-1].split('.')[0]
        f.write('\t'.join([sample]+x)+'\n')
        print(index)