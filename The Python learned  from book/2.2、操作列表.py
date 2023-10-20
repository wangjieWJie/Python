# 1、遍历整个列表
# 列表中有很多元素，挨个对他们进行操作会写大量重复的代码，这里我们遍历整个列表来操作

# 使用for循环来挨个对列表元素进行操作
test_list = ["dog", "apple", "Zoom", "Arm", "cow", "banana"]
for test_list in test_list:
    print(test_list)

print("test_list最终变成了一个元素：" + test_list + "\nThat's so bad\n")
# 将test_list中的变量取出来存放在test_list变量中然后再将test_list打印出来
# 在这个过程中，test_list 的值将变成最后一个元素的值，除非把临时变量重命名

# for后边的变量表示临时变量（变量，只有一个元素）
# in 后边的变量表示原列表（列表，内含n个元素）

object = ["dog", "apple", "bread", "grape", "beef", "banana"]
for object in object:
    print("I like eat " + object + " very much!")
    print("I want eat more about it!\n")


# 创建数值列表
# 使用 range() 函数快速生成数据
# range(起始值，终止值，步长)
# 据编程中常见的差一现象，range生成的数据中没有终止值，他会在终止值之前一个数停下来
for num_list in range(1, 5):
    print(num_list)

# list() 函数可以将range生成的数据转换成列表
num_list_1 = list(range(1, 10, 2))
print(num_list_1)

# 专门处理数字列表的函数
# 求和：sum()、  最小值：min()  最大值：max()
print(sum(num_list_1))
print("1到1000000相加之和：" + str(sum(list(range(1, 1000000)))))


# 列表解析
# 列表名=[由包含变量X的表达式表示的最终存储值  for  变量X  in  range(A,B,C) / 一个数集]
num_list_2 = [X**2 - 3 for X in num_list_1]
print("列表解析之结果：" + str(num_list_2))


# 2、切片：使用列表的一部分
# 注意：和range一样，在终止值的前一个数据处终止，起始值照常
players = ["1、charles", "2、martina", "3、michael", "4、florence", "5、eli"]
# 提取第2、3、4个元素：
print("第2、3、4个元素" + str(players[1:4]))
# 提取前三个元素
print("前三个元素" + str(players[:3]))
# 提取2之后的元素
print("2及之后所有的元素：" + str(players[1:]))
# 提取最后两个人：
print("提取最后两个人：" + str(players[-2:]))


# 遍历切片
my_foods = ["pizza", "falafel", "carrot cake", "agg", "chenken"]
same_food = my_foods
same_food.append("none")
print("修改后的my_food: " + str(my_foods))
# 从上面的例子可以很好的看出来，在python中，如果你给两个变量建立了等式，那么他们在之后的程序中会一直相等，一起变化，即：具有相同的储存地址
# 所以应该用切片创建副本后再复制到其他变量中去
same_food = my_foods[:]
# 这样same_food就是一个独立的变量了，因为my_food的切片在赋完值之后就被销毁了


# 3、元组
# Python将不能修改的值称为不可变的，而不可变的列表被称为元组。
P50 = (50, 888, 9990, 1e8)
# 圆括号代替方括号就成了元组，元组中的数据不允许修改，修改就会报错，就像 P50，50的型号、远超晓龙888的芯片、9990的售价、一亿像素的摄影是真实不可修改的一样
# 但是元组的访问方式和列表相同
print("P50的像素：" + str(P50[3]))

# 遍历起来和列表相同

# 修改元组变量
# 虽然直接修改元组内的某个变量是非法的，但是修改一下储存元组的那个变量还是可以的（赋值）
# 赋值（也可以说重新定义整个元组）
P60 = (60, 9200, 19999, 2e8)
P50 = P60[:]
print("我的P50升级版：" + str(P50))

# 或者是使用遍历的放法
P50 = [P * 2 for P in P50]
print("我的P50超级坚强版：" + str(P50))
