import pandas as pd
import os

###############################
##  检查目录下xls表格行数   ##
###############################

# path = r'C:\Users\dengqiuyang\OneDrive\文档\WeChat Files\huanghujian1990\FileStorage\File\2019-07\寻找基因\NCBI-ampR阳性-VFDB'

# fls = [os.path.join(path,i) for i in os.listdir(path)]
# lista = list()
# for fl in fls:
#     df = pd.read_excel(fl,header=None)
#     if df.shape[0] == 147:
#         print(fl)
#     lista.append(df.shape[0])
# lista = list(set(lista))
# print(lista)

##############################
##  统计表格的基因  ##
##############################

def obtain_genes():
    genes = dict()
    for fl in fls:
        fl = os.path.join(samples_path,fl)
        df = pd.read_excel(fl,header=None)
        content = df.iloc[3:-1,1:4]
        for _,row in content.iterrows():
            row = list(row)
            if str(row[0]) != 'nan':
                tp = row[0]
            if row[1]=='-' or str(row[1]) == 'nan':
                continue
            try:
                if tp not in genes:
                    genes[tp] = []
                else:
                    if row[1] not in genes[tp]:
                        x = genes[tp]
                        x.append(row[1])
                        genes[tp] = x
            except:
                print(fl,row[1])

    return genes

samples_path = r'C:\Users\dengqiuyang\OneDrive\文档\WeChat Files\huanghujian1990\FileStorage\File\2019-07\寻找基因\NCBI-ampR阳性-VFDB'
fls = os.listdir(samples_path)
gens = obtain_genes()

keys = []
for k,v in gens.items():
    if v == []:
        keys.append(k)
[gens.pop(kk) for kk in keys]

with open(os.path.join(r'C:\Users\dengqiuyang\OneDrive\文档\WeChat Files\huanghujian1990\FileStorage\File\2019-07\寻找基因','genes.txt'),'w') as o1:
    line1 = []
    line2 = []
    for k,v in gens.items():
        vl = len(v)
        line1.append(k+'\t'*(vl-1))
        line2.append('\t'.join(v))
    o1.write('\t'.join(line1)+'\n'+'\t'.join(line2))