'''
for 临时变量 in 序列：
    重复执行的代码1
    重复执行的代码2
    ……
'''
A=[1,2,3,4,5]       
for i in A:             # 若元素 i 在列表A里
    print(i)            # 则输出 


a=0
for b in "I love china":                 #完全可以输出
    a+=1                                 #给我干懵逼了，这个for是用来干嘛的啊
    print(a)
    print(b)
else:                                    #for还可以和else搭配使用，但是现在我没看见什么卵用
    print("字符串里没有b")


    
SB='he do is a big 2B'
sb=0
for er in SB:
    print(sb)
    sb+=1
    if sb>5:
        print('that is enough')
    else:
        print('right?')
    if sb==7:
        continue
    if sb==13:
        break
         
         
    