from gensim.models import word2vec

def getWordsNumber(seg_path, model_path):
    sentences = word2vec.LineSentence(seg_path)
    model = word2vec.Word2Vec(sentences, size=250, min_count=5)  # size 用来设置神经网络的层数
    model.save(model_path)

if __name__ == "__main__":
    seg_path = '../saveFile/wiki_seg.txt'
    model_path = '../word2vecModel/chinese_wiki_word2vec.model'
    getWordsNumber(seg_path,model_path)