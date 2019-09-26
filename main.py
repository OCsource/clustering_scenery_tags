from clustering_scenery_tags.dealLabel import similarity,cluster

def main():
    isWriteFile = 1
    city_number = '86'
    labelList, doubleList = '',''
    labelList, doubleList = similarity.wordsEmbedding(isWriteFile,city_number).main()
    wordsDict,sortCountWordsDict = cluster.getSimilarityWords(isWriteFile,labelList, doubleList).main()
    print(wordsDict)
    print(sortCountWordsDict)

if __name__ == '__main__':
    main()