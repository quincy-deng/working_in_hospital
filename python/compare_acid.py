##########################################
# 2019.8.5
# compare acid seq of two group
# To HuiZhen
##########################################
import os,sys

def obtain_gbkfiles(path):
    fls = [os.path.join(boot,fl) for boot,dirs,fls in os.walk(os.path.abspath(path)) for fl in fls if fl.endswith('gbk') and not fl.startswith('.')]
    return fls

def obtain_acidseq_base(content):
    return ''.join(content.split(r'/translation="')[1].split(r'"')[0].split('\n')).replace(' ','')

# 获得氨基酸序列列表
def obtain_acidseq(filepath):
    f_content = [obtain_acidseq_base(content) for content in open(filepath).read().split(r'CDS')[1:] if content.find(r'/translation="')!=-1]
    return f_content

# 求交集
def intersections(seq_list):
    interseqs = set(seq_list[0]).intersection(*seq_list[1:])
    return interseqs

# 求并集
def unions(seq_list):
    interseqs = set(seq_list[0]).union(*seq_list[1:])
    return interseqs

fls1 = obtain_gbkfiles(sys.argv[1])
fls2 = obtain_gbkfiles(sys.argv[2])

# 获取氨基酸序列
seq1 = [obtain_acidseq(fl) for fl in fls1]
seq2 = [obtain_acidseq(fl) for fl in fls2]

# 获取交集
is1 = intersections(seq1)
# is2 = intersections(seq2)

# 获取并集
# un1 = unions(seq1)
un2 = unions(seq2)

# 比较差异
ret1 = is1.difference(un2)
# ret2 = is2.difference(un1)
# print(len(ret1),len(ret2))

def obtain_GeneAcid(filepath):
    f_dict = {''.join(content.split(r'/translation="')[1].split(r'"')[0].split('\n')).replace(' ',''):content.split(r'gene="')[1].split(r'"')[0] for content in open(filepath).read().split(r'CDS')[1:] if content.find("/gene") !=-1}
    return f_dict

f1 = fls1[0]
f2 = '/home/dengqiuyang/Downloads/LowMIC/A0511/A0511.gbk'

f1_dict = obtain_GeneAcid(f1)
f2_dict = obtain_GeneAcid(f2)

H_gene = {f1_dict[i]:i for i in ret1 if i in f1_dict}
# print(H_gene,len(H_gene))
print(H_gene.keys())
# L_gene = {f2_dict[i]:i for i in ret2 if i in f2_dict}
# print(L_gene,len(L_gene))
# print(H_gene['paaJ'],L_gene['paaJ'])