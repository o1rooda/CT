from numpy import *

def numCount(dataList):
	num1 = 0; num2 = 0; num0 = 0
	for i in range(len(dataList)):
		if dataList[i] == 1:
			num1 += 1
		if dataList[i] == 2:
			num2 += 1
		if dataList[i] == 0:
			num0 += 1
	return num1, num2

def createVocabList (dataSet):
	vocabSet = set([]) 
	for document in dataSet:
		vocabSet = vocabSet | set(document)
	return list(vocabSet)

def setOfWords2Vec (vocabList, inputSet):
	returnVec = [0]*len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] = 1
		else: print "the word: %s is not in my Vocabulary!" % word
	return returnVec

def trainNB0 (trainMatrix, trainCategory):
	numTrainDocs = len(trainMatrix)
	numWords = len(trainMatrix[0])
	pA1, pA2 = numCount(trainCategory)
	pAbusive2 = pA2/float(numTrainDocs) 
	pAbusive1 = pA1/float(numTrainDocs)
	p0Num = ones(numWords); p1Num = ones(numWords); p2Num = ones(numWords)
	p0Denom = 2.0; p1Denom = 2.0; p2Denom = 2.0;
	for i in range(numTrainDocs):
		if trainCategory[i] == 1:
			p1Num += trainMatrix[i]
			p1Denom += sum(trainMatrix[i])
		elif trainCategory[i] == 2:
			p2Num += trainMatrix[i]
			p2Denom += sum(trainMatrix[i])
		else:
			p0Num += trainMatrix[i]
			p0Denom += sum(trainMatrix[i])
	p1Vect = log(p1Num/p1Denom)
	p2Vect = log(p2Num/p2Denom)
	p0Vect = log(p0Num/p0Denom)
	return p0Vect, p1Vect, p2Vect, pAbusive1, pAbusive2

def classifyNB (vec2Classify, p0Vec, p1Vec, p2Vec, pClass1, pClass2):
	p2 = sum(vec2Classify * p2Vec) + log(pClass2)
	p1 = sum(vec2Classify * p1Vec) + log(pClass1)
	p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass2 -  pClass1)
	
	if (p2 > p1) and (p2 > p0):
		return 2 
	if (p1 > p2) and (p1 > p0):
		return 1
	else:
		return 0

def bagOfWords2VecMN (vocabList, inputSet):
	returnVec = [0]*len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] += 1
	return returnVec

def textParse (bigString):
	import re
	listOfTokens = re.split(r'\W*', bigString)
	return [tok.lower() for tok in listOfTokens if len(tok) > 2]
	
def spamTest():
	docList=[]; classList=[]; fullText=[];
	for i in range(1, 11):
		wordList = textParse(open('/home/rooda/rdClass/final/SentenceCorpus/SentenceCorpus/unlabeled_articles/arxiv_unlabeled/%d.txt' %i).read())
		docList.append(wordList)
		fullText.extend(wordList)
		classList.append(2)
		wordList = textParse(open('/home/rooda/rdClass/final/SentenceCorpus/SentenceCorpus/unlabeled_articles/jdm_unlabeled/%d.txt' %i).read())
		docList.append(wordList)
		fullText.extend(wordList)
		classList.append(1)
		wordList = textParse(open('/home/rooda/rdClass/final/SentenceCorpus/SentenceCorpus/unlabeled_articles/plos_unlabeled/%d.txt' %i).read())
		docList.append(wordList)
		fullText.extend(wordList)
		classList.append(0)
	vocabList = createVocabList(docList)
	trainingSet = range(20); testSet=[]
	for i in range(5):
		randIndex = int(random.uniform(0, len(trainingSet)))
		testSet.append(trainingSet[randIndex])
		del(trainingSet[randIndex])
	trainMat=[]; trainClasses=[]
	for docIndex in trainingSet:
		trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
		trainClasses.append(classList[docIndex])
	p0V, p1V, p2V, pSpam1, pSpam2 = trainNB0(array(trainMat), array(trainClasses))
	errorCount=0
	for docIndex in testSet:
		wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
		if classifyNB(array(wordVector), p0V, p1V, p2V, pSpam1, pSpam2) != classList[docIndex]:
			errorCount += 1
			print "classification error", docList[docIndex]
	print 'the error rate is : ', float(errorCount)/len(testSet)
        return vocabList,fullText
