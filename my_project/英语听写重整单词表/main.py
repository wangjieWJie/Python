# 我要写一个程序，将一个十分专业的课本单词表转化为一个简洁的可以快速查看的单词表（词典）

# 首先我要写一个类，其中包含我这个文件该有的参数，便于设置
# 然后我要写一个函数 用于识别一行的开头或者结尾是什么并返回相关的参数以判断如何处理这一行，并且它可以判断这一行是否为空行等等

# 因为程序简单，所以我只写两个文件，一个是主程序一个是函数和类
import setting


# 初始化一个类
BS = setting.BookSet(8)
#开始进入修改格式
for UN in BS.unit_name:
    or_path = BS.path + str(BS.count) + '.txt'
    new_path = BS.path + "Unit" + str(BS.count) + '  new.txt'
    # 下面编译时报错，参考  https://blog.csdn.net/sinat_26811377/article/details/107629934  加了个参数
    with open(or_path,'r',encoding='utf-8') as BS.or_file[BS.count-1]:
        with open(new_path,'w',encoding='utf-8') as BS.new_file[BS.count-1]:
            n = 1
            for or_line in BS.or_file[BS.count-1]:
                # 判断这一行的性质 并将这一行写入新文件中
                setting.write_add(BS, setting.look_line(BS, or_line, n), BS.new_file[BS.count-1], or_line)
                n += 1
    # 计数前进            
    BS.count += 1






   # BS.or_file[BS.count-1]