# Command line file content sampler!
# Want to randomly select a certain number of cases (rows) from a file?
# 
# Algorithm reference for ReservoirSample function:
#     (from https://en.wikipedia.org/wiki/Reservoir_sampling):
#     Li, Kim-Hung (4 December 1994). 
#     "Reservoir-Sampling Algorithms of Time Complexity O(n(1+log(N/n)))". 
#     ACM Transactions on Mathematical Software. 20 (4): 481–493.
#
# For yourfile (e.g.: .csv, .txt), provided each row is a case, 
# Enter at command line:
# python3 sampling_ReservoirAP.py -f yourfilename -n desiredsamplesize
# Example:
# python3 sampling_ReservoirAP.py -f TitanicPassengers.csv -n 30

import random
import math
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', required=True, help="file with data or cases in rows")
parser.add_argument('-n', type=int, required=True, help="desired sample size")
args = parser.parse_args()
sampleSize = args.n
data=[]
with open(args.f) as file:
    reader = csv.reader(file, delimiter='\n') # "\n" grabs entire rows (use "," to limit columns)
    for row in reader:
        data.append(row[0]) # change "0" to index desired column(s)
        
def ReservoirSample(data, sampleSize):
    n = len(data)
    sample = [""]*sampleSize
    for i in range(sampleSize):
        sample[i] = data[i]
    W = math.exp(math.log(random.randint(1,99)/100)/sampleSize)    
    while i <= n:
        i = i + math.floor(math.log(random.randint(1,99)/100)/math.log(1-W))+1
        if i < n:
            sample[random.randint(0, sampleSize-1)] = data[i]
            W = W * math.exp(math.log(random.randint(1,99)/100)/sampleSize)
    print("The following were selected:"); print(*sample, sep="\n")
    return sample
ReservoirSample(data, sampleSize)

# def getSome():
#     for i in range(100):
#        ReservoirSample(data, sampleSize)
# getSome()