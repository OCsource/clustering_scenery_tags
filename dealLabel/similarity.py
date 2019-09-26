import csv,os,sys,numpy as np
from gensim.models import word2vec
from clustering_scenery_tags.DataBase import DB
from clustering_scenery_tags.uitls import logUtil

class wordsEmbedding:
    def __init__(self,isWriteFile,city_number):
        self.isWriteFile = isWriteFile
        self.logger = logUtil.getLogger(1)
        self.city_number = city_number
        try:
            print('导入数据......')
            self.model = word2vec.Word2Vec.load('./word2vecModel/chinese_wiki_word2vec.model')
            print('导入完毕!')
        except:
            self.logger.error('导入数据失败！')
            sys.exit(0)

    # 将数据写入CSV中
    # 参数：一维的标签名，二维的标签相似度
    def writeToCSV(self,title, doubleList):
        with open('./saveFile/similarity.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if not os.path.getsize('./saveFile/similarity.csv'):
                writer.writerow(title)
            writer.writerows(doubleList)

    # 得到所有不重复的关键词
    # 参数：城市编号
    # 返回：不重复标签数组
    def getKeyWords(self,city_number):
        operation = DB.operate()
        results1 = operation.searchScenery(city_number)
        noRepeatLabel = []
        for r1 in results1:
            results2 = operation.searchLabel(r1[0])
            if len(results2) == 0:
                continue
            for r2 in results2:
                if r2[0] not in noRepeatLabel:
                    noRepeatLabel.append(r2[0])
        return noRepeatLabel

    # 得到每个词的相似度
    # 参数：标签列表
    # 返回：标签的相似度值二维数组
    def getSimilarity(self,labelList):
        numberList = np.zeros((len(labelList),len(labelList)))
        noWords = []    # 装载训练集中没有的词语
        for i in range(len(labelList)):
            for j in range(i + 1, len(labelList)):
                # 如果两个词都没有在noWords集合里
                if labelList[i] in noWords or labelList[j] in noWords:
                    continue
                try:
                    # 求词的关联度
                    num = self.model.wv.similarity(labelList[i], labelList[j])
                    numberList[i][j] = num
                except:         # 若在训练集中没有的词语与其他词相关度为设为0,本来就是0
                    try:
                        self.model.wv.most_similar(labelList[i])
                        noWords.append(labelList[j])
                    except:
                        noWords.append(labelList[i])
        return numberList

    # 调用函数
    # 参数：是否写入文件
    # 返回：一维的标签名，二维的标签相似度
    def main(self):
        labelList = self.getKeyWords(self.city_number)
        numberList = self.getSimilarity(labelList)
        if self.isWriteFile:
            self.writeToCSV(labelList, numberList)
        return labelList, numberList

