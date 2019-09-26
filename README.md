---
**将景点标签相似度较高的找出来**
---

调用main.py要先将模型训练了。。。

入口函数：main.py

包说明：

trainWords：训练模型没有模型前要训练

word2vecModel：存放训练好的模型

saveCSV：存放分析之后的词向量

DataBase：访问数据库

logs：存放错误日记

utils：存放工具的地方

dealLabel：处理文字，形成词向量并找出相许度较高的词

---
**技术栈**
---

python(python3.7 x64)：有python的一定基础，https://www.runoob.com/python/python-tutorial.html

opencc：用于将繁体字转化为简体字的工具，下载地址https://bintray.com/byvoid/opencc/OpenCC

csv：是逗号分隔值，一般用Excel打开也可以用文本打开，可以看https://www.cnblogs.com/yanglang/p/7126660.html

numpy：这个也是一个非常有用的包，如果想要详细学习可以看https://zhuanlan.zhihu.com/p/57872490

---
**包的层次结构**
---

clustering_scenery_tags ---- trainWords ---- txtToWords.py

                                        ---- WIKIToTxt.py
                                        
                                        ---- wordsToNumber.py

                        ---- DataBase ---- DB.py
                  
                        ---- logs ---- data_log.log
                  
                                  ---- DB_log.log
                            
                        ---- saveFile ---- 
                        
                        ---- dealLabel ---- cluster.py
                        
                                       ---- similarity.py
                  
                        ---- utils ---- logUtil.py
                                   
                        ---- word2vecModel -----
                  
                        ---- main.py
                  
                        ----README.md
       
---
**依赖包**
---

pymysql：用于python连接数据库

numpy：用来计算多维数组的包，基本操作可看：https://blog.csdn.net/cxmscb/article/details/54583415

scipy：用于数据统计，有多种常用的数据统计函数，也包括连续和离散两种随机变量，这个包要在安装了numpy之后才能安装

gensim：gensim是一个python的自然语言处理库，能够将文档根据TF-IDF, LDA, LSI 等模型转化成向量模式，这个包要在安装了scipy之后才能安装

csv：用于读写一个类似于Excel表格的文件

---
**训练模型步骤**
---

模型以及词集太大，就不上传了

训练的中文词集下载：https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2

训练模型的过程可以看：

1. WIKIToTxt.py（将WIKI数据转为txt数据）

2. 用opencc将txt数据的繁体转化为简体（在命令行中转化），进入cmd键入：***(opencc的路径)\opencc.exe -i ***（txt文件的路径）\wiki_text.txt -o ***（txt文件的路径）\wiki_text2.txt -c ***(opencc的路径)\t2s.json

3. txtToWords.py（将txt数据分词）

4. wordsToNumber.py（训练模型）