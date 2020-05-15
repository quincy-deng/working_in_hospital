# -*- coding: utf-8 -*-
# 2090710
# 找出两组个体差异的基因组合
import sys
import os
from itertools import combinations

class GeneGroup:
    def __init__(self):
        self.execute()
    
    def obtainfiles(self,path):
        fls = os.popen("find {} -name *.gbk".format(path)).readlines()
        return [i[:-1] for i in fls]

    def genelist(self,gbkFile):
        f_content = [i.split(r'"')[0].split('_')[0] for i in open(gbkFile).read().split(r'/gene="')[1:]]
        f_content=list(set(f_content))
        return f_content

    def commongenes(self,alist):
        n = len(alist)
        star = alist[0]
        for j in range(n-1):
            star = list(set(star).intersection(set(alist[j+1])))
        return star

    # 列出所有组合
    def combination(self,alist,n):
        x = list(combinations(alist, n))
        return x
    
    def gene_exist_ornot(self,alist,blist):
        return set(alist).issubset(set(blist))
    
    def execute(self):
        fls = self.obtainfiles(sys.argv[1])
        fls_genes = [self.genelist(fl) for fl in fls]
        # group1共有基因
        group1_common_genes = self.commongenes(fls_genes)
        
        fls2 = self.obtainfiles(sys.argv[2])
        # group2基因列表
        fls_genes2 = [self.genelist(fl) for fl in fls2]
        group2_samples = len(fls_genes2)
        x,flag=0, 0
        csv = open('test.csv','w')
        for i in range(7)[1:]:
            combin = self.combination(group1_common_genes,i)
            print(i)
            # print(combin)
            for j in combin:
                count = [1 for k in fls_genes2 if self.gene_exist_ornot(j,k)]
                counts = len(count)

                if flag ==0:
                    if (counts/group2_samples )< (1-float(sys.argv[3])):
                        csv.write("{},基因{},在group2({})有{}个,差异{:.2f}%".format(i,j,group2_samples,counts,(1-counts/group2_samples)*100))
                        print("{},基因{},在group2({})有{}个,差异{:.2f}%".format(i,j,group2_samples,counts,(1-counts/group2_samples)*100))
                        x = counts
                        flag = 1
                    continue
                
                if counts>x:
                    continue
                elif counts == x:
                    csv.write("{},基因{},在group2({})有{}个,差异{:.2f}%".format(i,j,group2_samples,counts,(1-counts/group2_samples)*100))
                    continue
                else:
                    csv.write("{},基因{},在group2({})有{}个,差异{:.2f}%".format(i,j,group2_samples,counts,(1-counts/group2_samples)*100))
                    x = counts
                    print("{},基因{},在group2({})有{}个,差异{:.2f}%".format(i,j,group2_samples,counts,(1-counts/group2_samples)*100))
                
                if counts ==0:
                    sys.exit()
        csv.close()

if __name__ == "__main__":
    x = GeneGroup()