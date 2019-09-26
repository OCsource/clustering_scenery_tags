---
**将景点标签相似度较高的找出来**
---
入口函数：main.py

包说明：

saveCSV：存放分析之后的词向量

DataBase：访问数据库

logs：存放错误日记

utils：存放工具的地方

word2vecModel：存放训练好的模型

dealLabel：处理文字，形成词向量并找出相许度较高的词

---
**技术栈**
---

python(python3.7 x64)：有python的一定基础，https://www.runoob.com/python/python-tutorial.html

---
**包的层次结构**
---

clustering_scenery_tags ---- DataBase ---- DB.py
                  
                        ---- logs ---- data_log.log
                  
                                  ---- DB_log.log
                            
                        ---- saveCSV ----
                        
                        ---- dealLabel ----
                  
                        ---- utils ---- logUtil.py
                        
                                   ---- readFile.py
                                   
                        ---- word2vecModel -----
                  
                        ---- main.py
                  
                        ----README.md
       
---
**依赖包**
---

pymysql：用于python连接数据库

---
**训练模型步骤**
---

1. toText（将WIKI数据转为txt数据

2. 用opencc将txt数据的繁体转化为简体

3. cutWords（将txt数据分词）

4. train（训练模型）