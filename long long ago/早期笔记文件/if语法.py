CodeWord="WangJie_is_dad.  YouAreRightThisAGame"
print(CodeWord)
print("But you should tell me your age so that I can Judge if you can get into the computer.")
a=int(input("Your age="))
if a>=18 and a<75:
    print("your age is enough to enter our shop")
if a>=75 :
    print("You are too old to paly the computer")
else :
    print("GET OUT NOW!")
"""
这是if只要不忘了冒号啥也好说
"""   



#随机数
#先导入模板
import random
#再用随机数给某数赋值
num=random.randint(0,10)

print(f'你的幸运数字是{num}')