import os,shutil
WORKDIR='/home/dengqiuyang/02.PA/01.02.fasta'
OUTDIR='/home/dengqiuyang/02.PA/02.fasta'
for DIRNAME in os.listdir(WORKDIR):
    if os.path.isdir(os.path.join(WORKDIR,DIRNAME)):
            sourcefile=os.path.join(WORKDIR,DIRNAME,'scaffolds.fasta')
            if os.path.isfile(sourcefile):
                basename=DIRNAME+'.fasta'
                targetfile=os.path.join(OUTDIR,basename)
                shutil.copy(sourcefile,targetfile)
