# 为了学习《6、函数》而做的赠品
# 2023/10/21


# 和世界说早安
def SayHi():
    print("Hello World")


# 求好几个数里面最大的
def max(*nums):
    tmp = nums[1]
    for n in nums:
        if n > tmp:
            tmp = n
    return tmp


# def exchenage(a, b):
#     a = a + b
#     b = a - b
#     b = a - b


# 任意输入一堆数字，将这堆数字按照从大到小的顺序进行排列
def rank_num(*nums):
    tmp = 0
    tmp_nums = []
    for num in nums:
        tmp_nums.append(num)
        tmp += 1
    Real_index = tmp - 1
    while tmp:
        # 为了让列表的索引可以一点点 减小，从而引导他们往左前进，而真正的个数下标Real_index又不会受影响
        index = Real_index
        # 当 只有一个数字的时候 tmp 等于1，Real_index 等于0，下面的这个for循环不会执行
        for suibiian in range(0, Real_index):
            if tmp_nums[index] > tmp_nums[index - 1]:
                tmp_nums[index] += tmp_nums[index - 1]
                tmp_nums[index - 1] = tmp_nums[index] - tmp_nums[index - 1]
                tmp_nums[index] = tmp_nums[index] - tmp_nums[index - 1]
            index -= 1
        tmp -= 1
    return tmp_nums
    # 上述函数中所有的 index 和 real_index 都可以用 tmp-1 表示，其中 index-1 可以写作 tmp-2
