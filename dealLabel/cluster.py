import csv
from clustering_scenery_tags.uitls import logUtil

class getSimilarityWords:
    def __init__(self,isWriteFile,labelList='',numberList=''):
        self.isWriteFile = isWriteFile
        self.logger = logUtil.getLogger(1)
        self.labelList = labelList
        self.numberList = numberList

    # 读取CSV中的数据
    # 返回：一维的标签名称以及标签相似度二维数组
    def readDataCSV(self):
        with open("./saveFile/similarity.csv",'r') as csvFile:
            rows = csv.reader(csvFile)
            rs = list(rows)
        labelList = rs[0]
        rs.remove(labelList)
        return labelList,rs

    # 将关联词与被关联词存入字典中
    # 参数：关联字典，关联次数字典，被关联词，关联词
    def setWordsDict(self,wordsDict,countWordsDict,word1,word2):
        if word1 not in wordsDict:
            wordsDict[word1] = [word2]  # 记录相似度高的词,键是一个标签，值是一个数组
            countWordsDict[word2] = countWordsDict.get(word2, 0) + 1  # 记录某词被关联的次数
        else:
            wordsDict[word1].append(word2)
            countWordsDict[word2] = countWordsDict.get(word2, 0) + 1

    # 找出相似度较高的词语
    # 参数：一维的标签名，二维的标签相似度
    # 返回：标签关联以及被关联的字典，排序后的标签数组
    def getSimWords(self,labelList, numberList):
        wordsDict = {}   # 记录相似度较高的词
        countWordsDict = {}   #记录所有词的次数
        for i in range(len(numberList)):
            for j in range(i, len(numberList)):
                if float(numberList[i][j]) > 0.6:
                    self.setWordsDict(wordsDict,countWordsDict,labelList[i],labelList[j])
                    self.setWordsDict(wordsDict, countWordsDict, labelList[j], labelList[i])
        sortCountWordsDict = sorted(countWordsDict.items(), key=lambda x: x[1], reverse=True)   # 按字典值降序，返回数组
        return wordsDict,sortCountWordsDict

    def main(self):
        if self.isWriteFile:
            self.labelList, self.numberList = self.readDataCSV()
        return self.getSimWords(self.labelList, self.numberList)
