#自我
from SysMind import SystemMind

class SystemSelf:
    __help = "不欺骗自己是世界上最难的事"
    __name = ""
    __SystemMind = None

    def help(self):
        print(self.__help)

    def init(self,name):
        self.__name = name
        print("[SystemSelf] init "+self.__name)
        self.__SystemMind = SystemMind()
        self.__SystemMind.help()
        self.__SystemMind.init(name)

    def unInit(self):
        self.__SystemMind.unInit()
        print("[SystemSelf] unInit "+self.__name)


