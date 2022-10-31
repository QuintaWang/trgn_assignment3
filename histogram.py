#!/usr/bin/python
import pandas as pd
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file',type=str)
parser.add_argument('-f', type=int, default=1)
name=parser.parse_args().file
col = parser.parse_args().f
table=pd.read_csv(name, sep='\t', usecols=[col])
plt.hist(table)
plt.savefig('hist.png')
