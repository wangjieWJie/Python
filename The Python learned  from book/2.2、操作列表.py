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
