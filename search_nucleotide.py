###################################################
# 20190515
# rmlC氨基酸序列在7228个gbff文件里都找不到
###################################################
import os
from sys import argv
import datetime
import argparse

parser = argparse.ArgumentParser(description="运行此程序需接两个参数,第一个是data文件夹,第二个是要搜索seq文件夹")
parser.add_argument('--data','-d',help='data文件后缀gbff.gz')
args = parser.parse_args()

today = str(datetime.date.today())[5:]
gene = os.listdir(argv[2])

def read_acid(i):
    path=os.path.join(argv[2],i)
    return open(path).read().replace('\n','').replace(' ','').upper()

nuc_seqs = [read_acid(i) for i in gene]
fls = os.popen(("find {} -name \"*.gbff.gz\"").format(argv[1])).read().split()

def read_gbff(fl):
    temp = os.popen('zcat {}'.format(fl)).read().replace('\n','').replace(' ','').replace('\t','')
    return ''.join([i for i in temp if not i.isdigit()]).upper()
def search_nucleotide(fl_content,seq):
    if fl_content.find(seq)!=-1:
        return '1'
    else:
        return '0' 

with open('{}.txt'.format(today),'w') as f:
    f.write('\t'.join(['SAMPLE']+gene)+'\n')
    for index,fl in enumerate(fls):
        fl_content = read_gbff(fl)
        x = [search_nucleotide(fl_content,i) for i in nuc_seqs]
        print(x)
        sample = fl.split('/')[-1].split('.')[0]
        f.write('\t'.join([sample]+x)+'\n')
        print(index)