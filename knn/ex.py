import os
import numpy as np

dir=os.getenv('HOME')+'/machinelearninginaction/Ch02/digits/trainingDigits'
os.chdir(dir)
trainingFileList = os.listdir(dir)
m = len(trainingFileList)
print m

def img2vector(filename):
    height=32;
    width=32;
    mylist = []
    fr = open(filename)
    for i in range(height):
        lineStr=fr.readline()
        for j in range(width):
            mylist.append(int(lineStr[j]))
    return mylist
    #print mylist
    r=len(mylist)
    print r

