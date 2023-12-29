#数据库
import sqlite3

class SystemDB:
    __help = "一个人能够看见他拥有什么，但看不见他自己是什么"
    __dbName = ""
    __dbConnect = None

    def help(self):
        print(self.__help)

    def init(self,name):
        self.__dbName = name
        print("[SystemDB] init "+self.__dbName)
        self.__dbConnect = sqlite3.connect(self.__dbName+".db")

    def unInit(self):
        self.__dbConnect.close()
        print("[SystemDB] unInit "+self.__dbName)