###################################################
# 20190715
# 从gbk或者gbff文件搜索acid序列
# NCBI下载数据查询氨基酸序列
###################################################
# -*- utf-8 -*-

import os
from sys import argv
import datetime
# import gzip
import time

today = str(datetime.date.today())[5:]

a = os.popen(("find {} -name \"*.fasta\"").format(argv[1]))
fls = a.read().split()
seq = argv[2]
seq = seq.upper()

def read_fasta(fl):
    content = [''.join(i.split('\n')[1:]) for i in open(fl).read().split('>')[1:]]
    content = [i.replace('\n','').replace(' ','').replace('\t','') for i in content]
    return content

def similar(fl,seq):
    seq1 = read_fasta(fl)
    seq2 = seq
    c1,c2 = len(seq1),len(seq2)
    match_seq = []
    for i in range(c1-c2+1):
        sub_seq1 = seq1[i:i+c2]
        x,y = 0,0
        for index,j in enumerate(seq2):
            if j == sub_seq1[index]:
                x += 1
        for index,j in enumerate(translate(seq2)):
            if j == sub_seq1[index]:
                y += 1        
        if x/len(sub_seq1) >0.95:
            match_seq.append(sub_seq1)
        if y/len(sub_seq1) >0.95:
            match_seq.append(sub_seq1)
    
    if len(match_seq)>0:
        return [True,match_seq]
    return [False,'']

def translate(seq):
    table = {'A':'T','C':'G','G':'C','T':'A'}
    seq2 = ''.join([table[i.upper()] for i in seq])
    return seq2

def search_fasta(fl):
    seqs = []
    for sub_seq in read_fasta(fl):
        if len(sub_seq) < len(seq):
            return [False]
        elif sub_seq.find(seq)!=-1:
            return [True]
        elif sub_seq.find(translate(seq))!=-1:
            return [True]        
        
        res = similar(fl,seq)
        if res[0]:
            seqs += res[1]
    
    if res != []:
        return [True,seqs]

    return [False]

with open('{}.{}.txt'.format(argv[3],today),'w') as f:
    for fl in fls:
        start = time.clock()
        x = search_fasta(fl)
        end = time.clock()
        print(str(end))
        if x[0]:
            if len(x) ==1:
                sample = fl.split('/')[-1]
                f.write(sample+'\n')
            if len(x) ==2:
                sample = fl.split('/')[-1]
                f.write(sample+';'.join(x[1])+'\n')