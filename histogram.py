import csv
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', type=int, default=2)

col = parser.parse_args()
col.extra_args = col.extra_args[1:]
with open("population_analysis.tsv") as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")

plt.hist(tsvreader[col])

# Save the histogram
plt.savefig('hist.png')

# Display the plot
plt.show()