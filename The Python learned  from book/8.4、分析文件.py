# .split()  :这个方法能将一个字符串中的单词提取出来生成一个单词列表（其实就是空格和标点之间的字母的集合）
# 比如：
you_thinking = "YOU are so funny.I am so love you.I can not resist to kiss you.".split()
print(you_thinking)

# len()  函数用于计算列表的元素个数或者是字符串的长度

# 当你不想要在冒号后面写代码的时候，可以用 pass


import re

test_str = "山东省，济南市，槐荫区，山东中医药大学，，，，，男神宿舍，1131"
print(re.split("[，]+", test_str, maxsplit=100))

# split 在 re 模块中：
# 添加一个参数，使用正则表达式的元字符。
# 其中 [] 表示匹配位于 [] 中的任一字符，'+'表示 匹配位于+之前的字符或子模式的 1次或多次重复
# 上述函数表示在 test_str 中，以 ',' 为分隔符，将字符串分割并将每个元素储存在列表中
# 详见 正则表达式.pdf
