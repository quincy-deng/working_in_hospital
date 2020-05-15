# -*- coding: utf-8 -*-
import pandas as pd
import os
from sys import argv
def obtain_genes(xls_vf):
    df = pd.read_excel(xls_vf,header=None)
    content = df.iloc[3:-1,1:4]
    genes = list()
    for _,row in content.iterrows():
        row = list(row)
        if str(row[0]) != 'nan':
            tp = row[0]
        if row[1]=='-' or row[2]=='-' or str(row[1]) == 'nan':
            continue
        try:
            genes.append(tp+'_'+row[1])
        except:
            print(xls_vf,row[1],row[2])
    return genes

def obtain_samplefile(sample):
    for sample_fl in fls:
        if sample_fl.find(sample) != -1:
            return sample_fl
    print(sample)
    return None


table = r'C:\Users\dengqiuyang\OneDrive\文档\WeChat Files\huanghujian1990\FileStorage\File\2019-07\寻找基因\NCBI-ampR-VFDB(3).xlsx'

samples_path = r'C:\Users\dengqiuyang\OneDrive\文档\WeChat Files\huanghujian1990\FileStorage\File\2019-07\寻找基因\NCBI-ampR阳性-VFDB'
fls = os.listdir(samples_path)

df = pd.read_excel(table,header=None)
tp = df.iloc[0,:].tolist()[2:]
genes_temp = df.iloc[1,:].tolist()[2:]
genes = list()
for x,y in zip(tp,genes_temp):
    x = str(x)
    if x != 'nan':
        temp = x
    genes.append(temp+'_'+y)

samples = df.iloc[:,0].tolist()[2:]
for index_row,sample in enumerate(samples):
    fl = obtain_samplefile(sample)
    if fl == None:
        continue
    sample_genes = obtain_genes(os.path.join(samples_path,fl))
    # print(sample_genes)
    for index_col,gene in enumerate(genes):
        if gene in sample_genes:
            # print(gene)
            df.iloc[index_row+2,index_col+2] = 1
        else:
            df.iloc[index_row+2,index_col+2] = 0
print(df)
df.to_excel(r'C:\Users\dengqiuyang\OneDrive\文档\WeChat Files\huanghujian1990\FileStorage\File\2019-07\寻找基因\new_NCBI-ampR-VFDB(3).xlsx',index = False,header=False)