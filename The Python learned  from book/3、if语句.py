import random

a = random.randint(0, 10)
b = random.randint(0, 10)
c = random.randint(0, 10)
if a == b or a == c or b == c:
    print("You won!\nThat's amazing!")
elif a > b and a > c:
    print("A won!\nYou are a loser!!!")
elif b > a and b > c:
    print("B won!\nYou are a loser!!!")
elif c > a and c > b:
    print("C won!\nYou are a loser!!!")
elif a == b == c:
    print("All the ABC won!!!\nYou failled from the head to toe!!!")
else:
    print("That's impossible.")

# 运算符有 >、<、>=、<=、!=、==、and、or、in、not in

# 关键字in ： 它可以判断某个元素（变量）是否在某个列表中，是则true 否则 false
players = ["charles", "martina", "michael", "florence", "eli"]
if "wangjie" in players:
    print("hero")
elif "wangjie" not in players:
    print("He is not a player.")

# 布尔表达式
I_think = True
You_think = False
# true 和 false 都是关系运算的结果
# 很多地方会用到这些，比如是否允许用户修改网页？ user_chenage = False
# 其中 0 和 空列表相当于 False
