import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.corpora import WikiCorpus

# 将训练集转化（xml）为txt
# 参数：wiki训练集存放的路径，txt存放的路径
def translateTheText(xml_path,txt_path):
    path_to_wiki_dump = xml_path
    wiki_corpus = WikiCorpus(path_to_wiki_dump, dictionary={})
    num = 0
    with open(txt_path, 'w', encoding='utf-8') as output:
        for text in wiki_corpus.get_texts():  # get_texts() 将 wiki的一篇文章转为textd的一行
            output.write(' '.join(text) + '\n')
            num += 1
            if num % 10000 == 0 and num != 0:
                print('已处理 %d 篇文章'%(num))
        print('wiki词集转化完毕')

if __name__ == '__main__':
    xml_path = 'F:/wordArray/zhwiki-latest-pages-articles.xml.bz2'
    txt_path = '../saveFile/wiki_text.txt'
    translateTheText(xml_path,txt_path)