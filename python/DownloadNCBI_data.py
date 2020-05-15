###################################################
# 20190508
# 从NCBI下载克雷伯注释文件
###################################################
import sys 
def ftp(line):
    temp = line.rstrip()
    return temp+'/'+temp.split('/')[-1]+'_genomic.fna.gz'
ftps = [ftp(line) for line in open(sys.argv[1]).readlines() if not line.startswith('-')]
with open('kpFTPs.csv','w') as f:
    f.write('\n'.join(ftps))