##########################################
# 2019.5.5
# compare acid seq of two group
# To xushuye
##########################################
import os,sys
from collections import Counter

group1_fls = [os.path.join(boot,fl) for boot,dirs,fls in os.walk(os.path.abspath(sys.argv[1])) for fl in fls if fl.endswith('gbk') and not fl.startswith('.')]
count1 = len(group1_fls)
print("{} have {} samples".format(sys.argv[1],count1))

group2_fls = [os.path.join(boot,fl) for boot,dirs,fls in os.walk(os.path.abspath(sys.argv[2])) for fl in fls if fl.endswith('gbk') and not fl.startswith('.')]
# print(group2_fls)
count2 = len(group2_fls)
print("{} have {} samples".format(sys.argv[2],count2))
print('-'*25)

def obtain_genes(filepath):
    f_content = [i.split(r'"')[0].split('_')[0] for i in open(filepath).read().split(r'/gene="')[1:]]
    f_content=list(set(f_content))
    return f_content

genes1 = [acidseq for fl in group1_fls for acidseq in obtain_genes(fl)]
genes2 = [acidseq for fl in group2_fls for acidseq in obtain_genes(fl)]
acids1_dict,acids2_dict= Counter(genes1),Counter(genes2)
def calculate(seq,num):
    if seq in acids2_dict:
        return num/count1 - acids2_dict[seq]/count2
    else:
        return num/count1

temp = [seq for seq,num in acids1_dict.items()  if calculate(seq,num) > float(sys.argv[3])]
print('\t'.join(['gene',sys.argv[1],sys.argv[2]]))
[print('\t'.join([i,str(acids1_dict[i]),str(acids2_dict[i])])) for i in temp ]