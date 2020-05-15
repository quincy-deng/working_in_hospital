##########################################
# 2019.5.6
# compare acid seq of two group
# To xushuye
##########################################
import os,sys
from collections import Counter
from Bio import SeqIO

group1_fls = [os.path.join(boot,fl) for boot,dirs,fls in os.walk(os.path.abspath(sys.argv[1])) for fl in fls if fl.endswith('gbk') and not fl.startswith('.')]
count1 = len(group1_fls)
print("{} have {} samples".format(sys.argv[1],count1))

group2_fls = [os.path.join(boot,fl) for boot,dirs,fls in os.walk(os.path.abspath(sys.argv[2])) for fl in fls if fl.endswith('gbk') and not fl.startswith('.')]
# print(group2_fls)
count2 = len(group2_fls)
print("{} have {} samples".format(sys.argv[2],count2))
print('-'*25)

record_iterator = SeqIO.parse(group1_fls[0], "genbank")
# first_record = 
for gb in record_iterator:
    print(gb)