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

#先导入随机数的模板
import random
#再用随机数给某个数赋值
num=random.randint(0,9)
#再输出num
print(f'您今天的幸运数字是{num}')



if num==6:
    print('时来天地皆同力')
if num==4:
    print('运去英雄不自由')
if num==8:
    print('纵贩粒米亦善价，是发')
if num==0:
    print('零既百分百')
else:
    print('平淡的一天')
    
   
    
    

