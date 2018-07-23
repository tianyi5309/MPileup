# creates a pileup file with the first n samples of bamfilenames, and also a filenames.txt containing the bam files used
# mpileup ref.fa bamfilenames sample_size

import sys
import subprocess

referencefile = sys.argv[1]
bamfilenames = sys.argv[2]
sample_size = int(sys.argv[3])

filenames = []
with open(bamfilenames, "r") as f:
    for _ in range(sample_size):
        filenames.append(f.readline())

with open("filenames.txt", "w") as f:
    for name in filenames:
        f.write(name)

with open("compiled.pl", "w") as outfile:
    subprocess.run(["samtools", "mpileup", "-B", "-d10000", "-f", referencefile, "-q", "40", "-b", "filenames.txt"], stdout=outfile)