import jieba

# 将txt文本中的句子分词
# 参数：txt路径,分词之后的存放文本路径
def getCutWords(txt_path, seg_txt):
    stopword_set = set()
    output = open(seg_txt, 'w', encoding='utf-8')
    with open(txt_path, 'r', encoding='utf-8') as content:
        for texts_num, line in enumerate(content):  # enumerate 给 line前加序号
            line = line.strip('\n')
            words = jieba.cut(line, cut_all=False)
            for word in words:
                if word not in stopword_set:
                    output.write(word + ' ')
            output.write('\n')
            if (texts_num + 1) % 10000 == 0:
                print("已完成 %d 行的分词"%(texts_num + 1))
        print('文本分词完毕')
    output.close()

if __name__ == '__main__':
    txt_path = '../saveFile/wiki_text2.txt'
    seg_txt = '../saveFile/wiki_seg.txt'
    getCutWords(txt_path,seg_txt)