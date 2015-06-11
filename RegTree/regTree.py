from numpy import *

def loadDataset(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
	fltLine = map(float, curLIne):
	dataMat.append(fltLine)
    return dataMat

 
