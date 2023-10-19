# 列表由一系列按特定顺序排列的元素组成.
# 可以将任何东西加入列表中，其中的元素之间可以没有任何关系。

# 1、初识
week = ["mon", 2, 3, "thursday", "fri", "weekend"]
print(week)
# 神奇的是他会连同方括号，把整个列表给打印出来，但是这不是用户该看的内容，所以没啥用
print(week[3])
# 相当于C++中的数组，下标（索引）是从0开始的
# 当你想要索引最后一个元素时，你可以直接将下标写成 -1
print(week[-1])

# 使用起来是和 C 的数组一样的，数组就是数组，整型就是整型

# 但是但是但是，她最方便的地方在于
# python列表是活的，他是活的，他可能会随着程序的运行而增删修改元素，所以它的长度在运行过程中可能是不断变化的

# 修改列表元素
week[0] = "monday"
# 添加元素
# 方法.append(添加剂)能将元素添加到列表结尾
week.append("sunday")
print(week)
# 方法.insert(索引,值)可在列表的任何位置添加新元素
week.insert(0, "start")
print(week)
# 删除列表元素
# del list[索引]
del week[0]
print(week)
# 使用 pop 删除元素
# 方法pop()可删除列表末尾的元素，并让你能够接着使用它。
# 术语弹出（pop）源自这样的类比：列表就像一个   栈，而删除列表末尾的元素相当于弹出栈顶元素。
today = week.pop()
print(today)
# 弹出列表中任何位置的元素
# 在pop()的括号中加上索引即可
today = week.pop(4)
print(today)
print(week)
# 根据值删除元素
# .remove(想要删除的元素)
week.remove("weekend")
print(week)
# 这个方法一次只能删除一个值，当有多个相同的值的时候需要使用循环来彻底删除某个值


# 2、组织列表

# 2.1、排序

# 使用方法 .sort() 进行永久性排序
test = ["banana", "cow", "Arm", "Zoom", "apple", "dog"]
test.sort()
print(test)
# 缺点是它区分大小写，大写的 Z 比小写的 a 排行要靠前
# 逆序写法只需要加一个参数（reverse=True）即可
test.sort(reverse=True)
print(test)
# 这种方法所进行的排序是永久性的，你无法恢复之前的排序

# 使用函数sorted()对列表进行临时排序
test = ["banana", "cow", "Arm", "Zoom", "apple", "dog"]
print(sorted(test))
print(test)
# 逆序排列和sort是一样的，即添加‘reverse=True’参数
print(sorted(test, reverse=True))

# 使列表变为倒序
# 使用 .reversed() 方法即可永久性的将列表倒序
test.reverse()
print(test)


# 3、确定列表的长度
# 函数 len() 可以直接返回列表中的元素个数
print("test列表中的元素个数有：" + str(len(test)) + "个")
