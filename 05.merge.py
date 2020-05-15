import sys

f1 = open(sys.argv[1])
f2 = open(sys.argv[2])
## 合并ST,CT,Assembly和Submitter
# d1 = {line.split()[0]:line.split()[1:] for line in f1}
# d2 = {line.split()[0]:line.split()[1:] for line in f2}
# for assembly in d1:
#     if assembly in d2:
#         d1[assembly] += d2[assembly]

# o1=open('merge.txt','w')
# for i,j in d1.items():
#     o1.write(i+'\t'+'\t'.join(j[:4])+' '.join(j[4:])+'\n')

# f1.close()
# f2.close()
# o1.close()

## 合并作者
# d1 = {line.split('\t')[0]:('\t'.join(line.split('\t')[1:])).rstrip() for line in f1}
# d2 = dict()
# for line in f2:
#     d2.setdefault(line.split()[0][:15],[]).append(''.join(line.split()[2:]))

# print(d2)
# print('-'*30)
# print(d1)
# for assembly in d1:
#     if assembly in d2:
#         d1[assembly] = d1[assembly]+'\t'+';'.join(d2[assembly])

# o1=open('merge2.txt','w')
# for i,j in d1.items():
#     o1.write(i+'\t'+j+'\n')

# f1.close()
# f2.close()
# o1.close()

## 合并地理位置

d1 = [line.rstrip() for line in f1]
d2 = {line.split()[0].rstrip():' '.join(line.strip().split()[1:]) for line in f2}

# print(d2)
for i in d1:
    try:
        print(i,d2[i])
    except:
        print('NA')

f1.close()
f2.close()