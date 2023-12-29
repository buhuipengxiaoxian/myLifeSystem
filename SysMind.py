#心智
from SysDB import SystemDB

class SystemMind:
    __help = "请勿玩弄深埋在他人心底的东西"
    __name = ""
    __SystemDB = None

    def help(self):
        print(self.__help)

    def init(self,name):
        self.__name = name
        print("[SystemMind] init "+self.__name)
        self.__SystemDB = SystemDB()
        self.__SystemDB.help()
        self.__SystemDB.init(name)

    def unInit(self):
        self.__SystemDB.unInit()
        print("[SystemMind] unInit "+self.__name)