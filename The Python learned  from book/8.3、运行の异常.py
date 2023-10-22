# ZeroDivisionError  错误
# 妈的，这就是报错后显示的那个问题说明
# 比如说 0 当分母就会有： “ division by zero ” 的报错

# try-except 代码块来测试可行性
try:
    print(8 / 0)
except ZeroDivisionError:
    print("尼玛，你别用0当除数啊，数学咋学的啊，佛")  # 非常友好的提示消息
else:
    print("别看了，我怎么可能被执行")

# 上述代码中：
# 首先运行 try 中的代码，如果没有问题则会跳过 except 代码并运行 else 中的代码，所以except和else应该是try的分支语句
# 如果 try 中的代码有ZeroDivisionError问题，python则会寻找并运行except中的代码，而不会停止进程


# FileNotFoundError 错误
# 无法打开文件的错误
filename = "alice.txt"
try:
    with open(filename) as file_test:
        test_contents = file_test.read()
except FileNotFoundError:
    msg = "给老子好好看看，妈的 " + filename + " 根本就不存在，你自己看看有这个文件吗。"
    print(msg)
else:
    print(test_contents)

# 和之前ZeroDivisionError的错误是差不多的
