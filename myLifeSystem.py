# 面向系统级编程
#外部输入输出设备
ioArray = []




#内存数组
memoryArray= [
    'goto',
    'offset',
    '4',
    '0',
    '1',
    '0',
    'add',
    'offset',
    '-5',
    'offset',
    '-6',
    'offset',
    '-7',
    'move',
    'offset',
    '-11',
    'offset',
    '-14',
    'move',
    'offset',
    '-15',
    'offset',
    '-18',
    'goto',
    'offset',
    '-19'


]

# 根系统
class RootSystem:
    __lifeLong = 0      #系统生命周期数
    __ir = 'stop'       #指令寄存器
    __pc = 0            #程序计数器
    __dr0 = 0           #数据临时交换寄存器
    __dr1 = 0           #数据寄存器1
    __dr2 = 0           #数据寄存器2
    __dr3 = 0           #数据寄存器3
    __dr4 = 0           #数据寄存器4

    def __init__(self, lifeLong=0):
        self.__lifeLong = lifeLong
        print('根系统启动')
        self.__life()

    #生命过程
    def __life(self):
        while self.__lifeLong > 0:
            self.__lifeLong -= 1
            #print('根系统剩余时间', self.__lifeLong)
            #print(memoryArray)
            self.__do()

    #指令解析器
    def __do(self):
        self.__irRead()
        print(self.__pc,self.__ir)
        if(self.__ir == 'stop'):
            self.__irStop()
            return
        elif(self.__ir == 'null'):
            self.__irNULL()
            return
        elif(self.__ir == 'goto'):
            self.__irGoto()
            return
        elif(self.__ir == 'add'):
            self.__irAdd()
            return
        elif(self.__ir == 'sub'):
            self.__irSub()
            return
        elif(self.__ir == 'mul'):
            self.__irMul()
            return
        elif(self.__ir == 'div'):
            self.__irDiv()
            return
        elif(self.__ir == 'mod'):
            self.__irMod()
            return
        elif(self.__ir == 'move'):
            self.__irMove()
            return
        self.__irError('undefined ir')

    def __isPC(self,pc):
        if(pc < (len(memoryArray)) and(pc >= 0)):
            return True
        else:
            return False

    def __getAddress(self):
        self.__irRead()
        if(self.__ir == 'here'):
            self.__dr0 = self.__pc
            self.__pcNext()
            return self.__dr0
        elif(self.__ir == 'offset'):
            self.__pcNext()
            self.__irRead()
            self.__dr0 = self.__pc+int(self.__ir)
            self.__pcNext()
            return self.__dr0
        else:
            self.__dr0 = int(self.__ir)
            self.__pcNext()
            return self.__dr0

    def __getData(self):
        self.__irRead()
        if(self.__ir == 'address'):
            self.__pcNext()
            self.__irRead()
            self.__pcNext()
            if (self.__isPC(int(self.__ir))):
                return int(memoryArray[int(self.__ir)])
            else:
                self.__irError('address pc out of index')
                return -1
        elif(self.__ir == 'offset'):
            self.__pcNext()
            self.__irRead()
            self.__dr0 = self.__pc+int(self.__ir)
            self.__pcNext()
            if(self.__isPC(self.__dr0)):
                return int(memoryArray[self.__dr0])
            else:
                self.__irError('offset pc out of index')
                return -1
        else:
            self.__irRead()
            self.__pcNext()
            return int(self.__ir)

    def __irRead(self):
        if (self.__isPC(self.__pc)):
            self.__ir = memoryArray[self.__pc]
        else:
            self.__irError('ir read error')

    #pc指令递增器
    def __pcNext(self):
        self.__pc+=1

    def __irError(self,e = ''):
        print('[error|',self.__pc,":",self.__ir,"]",e)
        #执行停机
        self.__pc = -1
        self.__ir = 'stop'

    def __irStop(self):
        return

    def __irNULL(self):
        self.__pcNext()

    def __irGoto(self):
        self.__pcNext()
        self.__pc = self.__getAddress()

    def __irAdd(self):
        self.__pcNext()
        self.__dr1 = self.__getData()
        self.__dr2 = self.__getData()
        self.__dr3  = self.__getAddress()
        if(self.__isPC(self.__dr3)):
            memoryArray[self.__dr3] = self.__dr1 + self.__dr2

    def __irSub(self):
        self.__pcNext()
        self.__dr1 = self.__getData()
        self.__dr2 = self.__getData()
        self.__dr3  = self.__getAddress()
        if(self.__isPC(self.__dr3)):
            memoryArray[self.__dr3] = self.__dr1 - self.__dr2

    def __irMul(self):
        self.__pcNext()
        self.__dr1 = self.__getData()
        self.__dr2 = self.__getData()
        self.__dr3  = self.__getAddress()
        if(self.__isPC(self.__dr3)):
            memoryArray[self.__dr3] = self.__dr1 * self.__dr2

    def __irDiv(self):
        self.__pcNext()
        self.__dr1 = self.__getData()
        self.__dr2 = self.__getData()
        self.__dr3  = self.__getAddress()
        if(self.__isPC(self.__dr3)):
            memoryArray[self.__dr3] = self.__dr1 / self.__dr2

    def __irMod(self):
        self.__pcNext()
        self.__dr1 = self.__getData()
        self.__dr2 = self.__getData()
        if(self.__dr2 == 0):
            return
        self.__dr3  = self.__getAddress()
        if(self.__isPC(self.__dr3)):
            memoryArray[self.__dr3] = self.__dr1 % self.__dr2

    def __irMove(self):
        self.__pcNext()
        self.__dr1 = self.__getData()
        self.__dr2 = self.__getAddress()
        if (self.__isPC(self.__dr2)):
            memoryArray[self.__dr2] = self.__dr1

    def __del__(self):
        print('根系统关闭')

if __name__ == '__main__':
    print('内存',memoryArray)
    rootSystem = RootSystem(100)

