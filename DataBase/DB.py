import pymysql
from clustering_scenery_tags.uitls import logUtil

logger = logUtil.getLogger(0)

class operate:
    def __init__(self):
        self.__dbName = 'qunarNew'
        self.__user = 'root'
        self.__password = '123456'
        self.__host = 'localhost'
        self.__char = 'utf8'

    # 查询景点
    # 参数：城市编号
    # 返回：成功查询到的景点二维元组，失败false
    def searchScenery(self, city_number):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        sql = "SELECT scenery_number,scenery_name FROM scenery_table WHERE city_number = '%s';"%(city_number)
        try:
            cs.execute(sql)
            result = cs.fetchall()
            return result
        except:
            db.rollback()
            logger.error(city_number + ":景点查找失败")
            return False
        finally:
            db.close()

    # 查找标签
    # 参数：景点编号
    # 返回：成功，一个二维元组标签的，失败false
    def searchLabel(self,scenery_number):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        # 记得改回来scenery_words
        sql = "SELECT word FROM newWords WHERE scenery_number = '%s';" % (scenery_number)
        try:
            cs.execute(sql)
            result = cs.fetchall()
            return result
        except:
            db.rollback()
            logger.error(scenery_number + ":景点的标签查找失败")
            return False
        finally:
            db.close()

    def __str__(self):
        return "DB --ing"