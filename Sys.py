#总系统
from SysWorld import SystemWorld

class System:
    __help = "我贴着地面步行，不在云端跳舞"
    __name = ""
    __World = None

    def help(self):
        print(self.__help)

    def init(self,name):
        self.__name = name
        print("[System] init "+self.__name)

        self.__World = SystemWorld()
        self.__World.help()
        self.__World.init(name)

    def unInit(self):
        self.__World.unInit()
        print("[System] unInit "+self.__name)

if __name__ == '__main__':
    s = System()
    s.help()
    s.init("HL")
    s.unInit()