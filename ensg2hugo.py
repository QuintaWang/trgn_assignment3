#!/usr/bin/python
import sys
import fileinput
import re
import numpy as np

import os
eth={}
for each_line_of_text in fileinput.input("Homo_sapiens.GRCh37.75.gtf"):
    gene=re.findall(r'^.*?\t.*?\t(gene)\t', each_line_of_text, re.I)
    gene_id=re.findall(r'gene_id "(ENSG\d*?)"', each_line_of_text, re.I)
    gene_name=re.findall(r'gene_name "(.*?)"', each_line_of_text, re.I)
    if gene:
        if gene_id:
            if gene_name:
                eth[gene_id[0]] = gene_name[0]

if sys.argv[1][:2] == '-f':
    columnnumber = sys.argv[1][2]
    data = sys.argv[2]
    column = int(columnnumber)
else:
    column = 1
    data = sys.argv[1]   

print('"","gene_name","gene_type","logFC","AveExpr"')
if os.path.exists(sys.argv[2]):    
    for line in open(sys.argv[2],"r"):
        arr=line.split(",")
        g=arr[1].split(".")
        k=g[0].replace("\"","")

        if column==2:
            if k in eth:
                new_str=line.replace(arr[1],"\""+eth[k]+"\"");
                print(new_str.replace("\n",""))        
        else:
            print(line.replace("\n",""))
