# 寻找lyb24 19基因结构,提取核酸序列
# 将gbff文件根据"LOCUS"拆分contig,根据"ORIGIN"拆分注释信息和核酸序列,再用"  gene  "拆分注释信息,搜索第一个和最后一个基因氨基酸序列,将可以匹配出来序列位置信息从核酸序列提取出来
import sys
import gzip

def splitcontig(filename):
    with gzip.open(filename) as f:
        # o1 = filename.rstrip('gbff.gz')
        content = str(f.read(),encoding='utf-8')
        # 分contig寻找
        for part in content.split('LOCUS'):
            if part.find('MSTDIQLNLIGRTQELFVDDIQQWNNKLIEIVSSSKF') != -1:
                # a_dict = dict()
                part1,part2 = part.split('ORIGIN')
                contig = ''
                # 拼接核酸序列
                for line in part2.split('\n'):
                    contig = contig + (''.join(line.split()[1:]))
                # 从contig寻找起始和结束位点
                reverse_comp = {"A":"T",'C':'G','T':'A','G':'C'}
                startpoint,endpoint,tag =0,0,''
                for subpart in part1.split('    gene    '):
                    if subpart.find('MSTDIQLNLIGRTQELFVDDIQQWNNKLIEIVSSSKF') != -1:
                        # print(subpart)
                        f1 = subpart.split('\n')[0].strip()
                        # print(f1)
                        if f1.startswith('comp'):
                            tag = '**compliment_seq**'
                            endpoint = f1.split('..')[1].split(')')[0]
                        else:
                            startpoint = f1.split('..')[0]
                    elif subpart.find('MNVIISFIILFLISFVLTFSVRKYALRKN') != -1:
                        # print(subpart)
                        f2 = subpart.split('\n')[0].strip()
                        # print(f2)
                        if f2.startswith('comp'):
                            startpoint = f2.split('..')[0].split('(')[1]
                            if startpoint.startswith('<'):
                                startpoint = startpoint.split('<')[1]
                        else:
                            endpoint = f2.split('..')[1]
                print(startpoint,endpoint,'\n')
                SEQ = contig[int(startpoint)-1:int(endpoint)]
                SEQ = SEQ.upper()
                if tag == '**compliment_seq**':
                    temp = ''
                    for i in SEQ:
                        temp += reverse_comp[i]
                    SEQ = temp[::-1]

                return ">"+filename+'\t'+str(len(SEQ))+'\n'+SEQ

# o = open('lyb24_seq','w')
# f1 = open('sample_assembly_variant.txt')
# d2 = {line.split()[2]:'_'.join(line.split()[:2]) for line in f1}
# f1.close()

for filename in sys.stdin.readlines():
    filename=filename.rstrip()
    filename1 =filename.split('gbk')[0]+'fasta'
    with open(filename1,'w') as o1:
        seq = splitcontig(filename)
        o1.write(seq)
    
    # o.write(seq+'\n')

# o.close()
    
