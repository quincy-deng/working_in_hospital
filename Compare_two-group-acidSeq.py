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
print('-'*25+'\n')

def obtain_acidseq_base(content):
    return ''.join(content.split(r'/translation="')[1].split(r'"')[0].split('\n')).replace(' ','')

def obtain_acidseq(filepath):
    f_content = [obtain_acidseq_base(content) for content in open(filepath).read().split(r'CDS')[1:] if content.find(r'/translation="')!=-1]
    return f_content

def obtain_GeneAcid(filepath):
    f_dict = {''.join(content.split(r'/translation="')[1].split(r'"')[0].split('\n')).replace(' ',''):content.split(r'gene="')[1].split(r'"')[0] for content in open(filepath).read().split(r'CDS')[1:] if content.find("/gene") !=-1}
    return f_dict

acids1 = [acidseq for fl in group1_fls for acidseq in obtain_acidseq(fl)]
acids2 = [acidseq for fl in group2_fls for acidseq in obtain_acidseq(fl)]
acids1_dict,acids2_dict= Counter(acids1),Counter(acids2)

[print(seq) for seq,num in acids1_dict.items() if num>34]

temp = [seq for seq,num in acids1_dict.items() if seq in acids2_dict if (num/count1 - acids2_dict[seq]/count2) > float(sys.argv[3])]

dict_GeneAcid = {}
[dict_GeneAcid.update(obtain_GeneAcid(fl)) for fl in (group1_fls+group2_fls)]

print('\t'.join(['gene',sys.argv[1],sys.argv[2]])+'\n')
[print('\t'.join([dict_GeneAcid[i],str(acids1_dict[i]),str(acids2_dict[i])])) for i in temp if i in dict_GeneAcid]
[print('\t'.join(['',str(acids1_dict[i]),str(acids2_dict[i])])) for i in temp if i not in dict_GeneAcid]