###################################################
# 20190715
# 从gbk或者gbff文件搜索acid序列
# NCBI下载数据查询氨基酸序列
###################################################
# -*- utf-8 -*-

import os
from sys import argv
import datetime
import gzip

today = str(datetime.date.today())[5:]

a = os.popen(("find {} -type f -name \"*.gbk\"").format(argv[1]))
fls = a.read().split()
acid_seq = argv[2]

def read_gbff(fl):
    return os.popen("cat {}".format(fl)).read().replace('\n','').replace(' ','').replace('\t','')
def search_acid(fl,acid):
    if read_gbff(fl).find(acid.upper())!=-1:
        return '1'
    else:
        return '0' 

with open('{}.{}.txt'.format(argv[3],today),'w') as f:
    for fl in fls:
        x = search_acid(fl,acid_seq)
        if x == '1':
            sample = fl.split('/')[-1]
            f.write(sample+'\n')