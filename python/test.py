gbk_1689 = r'/home/dengqiuyang/01.Klebsiella_pneumoniae/06.kpData.gbk/AH1689-2.gbk'
reverse_comp = {"A":"T",'C':'G','T':'A','G':'C'}

with open(gbk_1689) as F:
    gbk_content = F.read()
    for contig in gbk_content.split('LOCUS'):
        if contig.find('ampR') != -1:
            CDS,ORIGIN=contig.split("ORIGIN")
            ORI=''
            seq,c_seq='',''
            for line in ORIGIN.split('\n'):
                ORI += ''.join(line.split()[1:])
            for cds in CDS.split('    CDS    ' ):
                if cds.find('ampR') != -1:
                    # print(cds)
                    seq_range = cds.split('\n')[0].strip()
                    print(seq_range)
                    if seq_range.startswith('comp'):
                        startpoint = seq_range.split('..')[0].split('(')[1]
                        startpoint =int(startpoint)
                        endpoint = seq_range.split('..')[1].split(')')[0]
                        endpoint = int(endpoint)
                        # print(ORI)
                        seq = ORI[startpoint-1000:endpoint+1000].upper()
                        seq = (''.join([reverse_comp[i] for i in seq]))[::-1]
                        c_seq = ''.join([reverse_comp[i] for i in seq])
                        break
                    startpoint,endpoint=int(seq_range.split('..')[0]),int(seq_range.split('..')[1])
                    seq = ORI[startpoint-1000,endpoint+1000].upper()
                    c_seq = ''.join([reverse_comp[i] for i in seq])
                    break
            # print(seq[])
            with open('ampRseq.txt','w') as O:
                O.write(seq[:1000]+'\t'+seq[1000:-999]+'\t' +seq[-999:]+'\n')
                O.write(c_seq[:1000]+'\t'+c_seq[1000:-999]+'\t' +c_seq[-999:])
