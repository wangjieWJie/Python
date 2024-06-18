# 此文件用于保存所需的函数和类

#首先是一个必须的类
class BookSet:
    def __init__(self,N_u):
        # 单元数
        self.Num_unit = N_u
        # 词性判断
        self.all_adj = {'v.','n.','a.','vi.','vt.','ad.','int.','jn.','prep.','m.'}
        # 单元名称
        self.unit_name = []
        # 原始文件路径
        self.path = "file/English/"
        # 原始文本文件暂存
        self.or_file = []
        # 新建文本文件暂存
        self.new_file = []
        # 计数器
        self.count = 1
        # 行数计数
        self.nu_line = 1
        # 空行、单词行、词性及解释行
        self.nonono = 0
        self.word = 1
        self.adj = 3
        # 输出参数
        self.all = -1

        # 非中文字符
        self.disChina = 'qwertyuioipasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM{}[]:""<>?/.,;][()&!@#$%^&*_+-=] \0 \n \r；; ： （）() ”“ ‘’'
        # 字母表
        self.alphabet = 'abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM, .() - \n \0'



        # 生成一串名称备用
        n = 1
        for i in range(0,self.Num_unit):
            self.unit_name.append("unit"+ str(n))
            self.or_file.append(0)
            self.new_file.append(0)
            n+=1
        print(self.unit_name)



# 判断一行的性质，并处理它
def look_line(BS,one_line,count):
    # 输出参数
    BS.all = -1
    # 判断是否为空行
    if one_line == "\n":
        BS.all = BS.nonono
        # print("line "+ str(count) + ' is a Enter: ' + one_line)
    # 判断是否是单词行
    else:
        for one in one_line:
            if one in BS.alphabet:
                BS.all = BS.word
            else:
                BS.all = -1
                #print('不是纯单词，有杂质，杂质为：'+ one+'\n')
                break
        if BS.all == BS.word:
            for one_adj in BS.all_adj:
                if one_adj in one_line:
                    BS.all = BS.adj
                    #print("line "+ str(count) + ' is a 词性解释行: ' + one_line)
                    break
            if BS.all == BS.word:
                return BS.all
        # 判断是否是词性行解释行
        if BS.all == -1  and (one_line[0] in BS.all_adj or one_line[0:1] in BS.all_adj or one_line[0:2] in BS.all_adj or one_line[0:3] in BS.all_adj or one_line[0:4] in BS.all_adj or one_line[0:5] in BS.all_adj) :
                BS.all = BS.adj
                #print("line "+ str(count) + ' is a 词性解释行: ' + one_line)
        elif BS.all == 3:
            #print("确定为解释性行\n")
            pass
        #判断此行是否有特殊问题
        else:
            print(one_line[0:4])
            print("The line"+ str(count) +" has a terrible problem:" + one_line)
            BS.all = -1
    return BS.all




# 将一行写入新文件
def write_add(BS,all,file_write,one_line):
    if all == 0:
        file_write.write('\n')
    elif all == 1:
        # rstrip()方法用于删除字符串末尾的换行符
        file_write.write(one_line.rstrip())
    elif all == 3:
        n = 0
        for aa in one_line:
            if one_line[n] in BS.disChina:
                n+=1
            else:
                break
        if one_line[-1] == one_line[n-1]:
            file_write.write('  \\\\'+one_line)
        else:
            file_write.write('  '+one_line[n:])
    
