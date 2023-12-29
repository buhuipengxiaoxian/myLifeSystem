#世界
from SysSelf import SystemSelf

class SystemWorld:
    __help = "世界的意义必定在世界之外"
    __name = ""
    __SystemSelf = None

    def help(self):
        print(self.__help)

    def init(self,name):
        self.__name = name
        print("[SystemWorld] init "+self.__name)

        self.__SystemSelf = SystemSelf()
        self.__SystemSelf.help()
        self.__SystemSelf.init(name)

    def unInit(self):
        self.__SystemSelf.unInit()
        print("[SystemWorld] unInit "+self.__name)