identify = {"name": "axiao", "sex": "male", "age": 19, "weight": 50}
print("姓名:" + identify["name"])
print("体重:" + str(identify["weight"]) + "Kg")
# 字典 就是一系列 “键——值”对，其中的 值 可以是python中的任何对象（数字、字符串、列表、字典等）
# 访问只需： 字典名[键名]

# 字典是一种动态结构，可随时在其中添加键—值对。
# 添加时只需要将想要添加的键值对如下方式写出
identify["IQ"] = 200
identify["IE"] = 200
print(identify)

ot_identify = {}
ot_identify["name"] = "Dabing"
# 这样分行写或更为清晰

# 修改字典中的值
# 很简单，拿出他来直接改就行
ot_identify["name"] = "orther name"

# 删除键值对
# 使用 del 将指定的 键 删除
del ot_identify["name"]
# 也可以直接把字典删除
del identify
# del 永久删除，无法恢复

# 感悟：
# 对象是一个具有多种属性的一个东西
# 上面那个identify就是 一个对象，一个对象可能要干很多事情
long_id = {
    "name": "axiao",
    "sex": "male",
    "age": 19,
    "weight": 50,
    "IQ": 200,
    "IE": 200,
}
# 释怀了：竖着写极大的提高了代码的可读性
# 另：
print(
    "I know a smart man,his name is "
    + long_id["name"]
    + ",he is "
    + str(long_id["age"])
    + "-years-old.I like him very much"
)


# 遍历字典
for k, v in long_id.items():
    print("\nkey键：" + str(k))
    print("value值：" + str(v))
# 方法 items() 返回一个键—值对列表。
# 接下来，for循环依次将每个 键—值对 存储到指定的两个变量中。
# 注意：有可能上述代码的返回顺序和储存顺序不一致，
#       这是很正常的，因为Python不关心键—值对的存储顺序，而只跟踪键和值之间的关联关系。

# 遍历所有的 键 key
# .item() 是键值对，.keys() 是键， .values() 是 值

# keys 也是返回一个列表，包含所有的 键
# 不同的是，你可以省略他
for k_1 in long_id:
    1 + 1
for k_2 in long_id.keys():
    1 + 1
# 上述两种写法都是对的，当你遍历字典时，默认遍历字典的所有的键

# 按顺序遍历字典中所有的键
# 使用函数sorted()来获得按特定顺序排列的键列表的副本：
sorted(long_id.keys())
# 它表示将上面括号中的列表按照当年存储的顺序进行排序

# .value() 和上面俩个方法的使用无大差别，但是有几个特殊情况：值 中可能有很多重复的值
# 可以使用集合来剔除重复项
# 集合（set）类似于列表，但每个元素都必须是独一无二的
set(long_id.values())
# set创建了一个没有重复元素的集合


# 嵌套
# 字典可以嵌套在列表中，列表也可以嵌套在字典中

# 字典列表
# 比如有一个字典列表
# 列表中每一个字典表示一个僵尸，每一个字典里又都有关于每个僵尸的属性参数
monster = []
zombie = {}
for i in range(0, 5):
    zombie["atack"] = 20
    zombie["speed"] = 10
    zombie["golds"] = 25
    monster.append(zombie)
print("生成五个僵尸")
print(monster)
# 上面写的不好，可以改成：
monster = []
for i in range(0, 5):
    zombie = {"atacK": 20, "speed": 10, "golds": 25}
    monster.append(zombie)
print("改进后的生成五个僵尸")
print(monster)


# 将列表储存在字典中
strong = {
    "六味地黄丸": ["熟地黄", "酒萸肉", "牡丹皮", "山药", "茯苓", "泽泻"],
    "锁阳固精丸": [
        "锁阳",
        "肉苁蓉（蒸）",
        "制巴戟天",
        "补骨脂（盐炒）",
        "菟丝子",
        "杜仲（炭）",
        "八角茴香",
        "韭菜子",
        "芡实（炒）",
        "莲子",
    ],
    "黑芝麻丸": ["黑芝麻", "红枣", "枸杞", "桑葚"],
}


# 在字典中储存字典
# 我现在有几个客户，每个客户都有很多毛病，我要记住他们
group = {
    "marsk": {"age": 48, "job": "Boss", "hobby": "Brag"},
    "telonp": {"age": 55, "job": "escaped criminal", "hobby": "beauty"},
}
