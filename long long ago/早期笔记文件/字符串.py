strl="abcdefghijklmn"
print(strl)
print(strl[0])
print(strl[1])
#冒号间的三个数分别表示  开头：结尾:步长
print(strl[1:5:1])

#find的用法
#find(子串，开始位置下标，结束位置下标)
xue='sown song faster ,kill the singer, send it to the alabaster.'
print(xue.find('singer'))                     #表示打印singer中s所在的位数
print(xue.find('er',27,33))                   #表示在 27 ~ 33 中找到er中e的位数


#index和find貌似是一样的

print(xue.index('er',27,33))                  #表示在 27 ~ 33 中找到er中e的位数


#count是返回某个子串在整个字符串里出现的次数
print(xue.count('r'))   #返回 3

"""
refind和find功能一样，就是从右边开始查
reindex和index功能一样，就是从右边开始查

"""



#x下面是replace替换的语法
#replace(旧子串，新子串，替换次数)
#替换次数  如果查出子串出现次数，则替换次数为子串出现次数

shishi='wangjie is a very outstanding father,all of his sons are respect him so much. '


print(shishi.replace('wangjie','axiao',12))       #将wangjie 替换成 axiao 最多替换 12 次
#print("现在来测试replace的用法：")               #如果空着第三个参数，那么替换次数没有上限
#print(shishi.replace('o','0'))

new_strl=shishi.replace('father','grandfather')
print(new_strl)




#下面是split的用法
"""
字符串序列.split(分割字符,num)
num表示的是分割字符出现的次数，既将来返回数据个数为num+1个
"""

listl=strl.split('d',3)
print(listl)

#分割的字符将丢失成为间隔





#join用来合并列表里的字符串数据使成为一个大字符串

#比如这里有一个列表
mlist=['you','me','he']
#用and连接
new_mlist=" and ".join(mlist)
print(new_mlist)




"""
captain的用法
使整个字符串的第一个字母大写，就大写一个
"""

print(shishi.capitalize())


"""
title（）是把每个分字符串的首字母都大写

"""
print(shishi.title())



