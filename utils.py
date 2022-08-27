import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt

namesh = []
freqnh = []
namesm = []
freqnm = []
surnames = []
freqsur1 = []
freqsur2 = []

def getDiscreteNormalDistribution(min, max, center=None):
    if center == None: center = int(round((min + max) / 2))
    x = np.arange(min, max+1)
    prob = ss.norm.pdf(x, center, (min + max) / 2)
    prob = prob / prob.sum()
    num = np.random.choice(x, p=prob)
    return num

def loadFromFile():
    with open("dics/hombres.txt") as f:
        lines = f.readlines()
        for line in lines:
            linedata = line.split(',')
            namesh.append(linedata[0])
            freqnh.append(int(linedata[1]))
    
    with open("dics/mujeres.txt") as f:
        lines = f.readlines()
        for line in lines:
            linedata = line.split(',')
            namesm.append(linedata[0])
            freqnm.append(int(linedata[1]))

    with open("dics/apellidos.txt") as f:
        lines = f.readlines()
        for line in lines:
            linedata = line.split(',')
            surnames.append(linedata[0])
            freqsur1.append(int(linedata[1]))
            freqsur2.append(int(linedata[2]))