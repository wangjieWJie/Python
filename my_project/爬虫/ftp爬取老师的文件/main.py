from ftplib import FTP, error_perm

def download_file(ftp, remote_file, local_file):
    try:
        with open(local_file, 'wb') as f:
            ftp.retrbinary(f'RETR {remote_file}', f.write)
        print(f'Successfully downloaded {remote_file}')
    except error_perm as e:
        print(f'Permission error: {e}')
    except Exception as e:
        print(f'Error: {e}')

def main():
    ftp_server = '210.44.172.251'
    username = 'zh'
    password = '123456'
    remote_file = '/学生上传/22级生医-信号与系统/2022121213王凡信号与系统作业5.docx'  # 替换为实际文件名
    local_file = 'downloaded_file.docx'

    ftp = FTP(ftp_server)
    ftp.login(user=username, passwd=password)
    ftp.set_pasv(True)  # 启用被动模式

    # 尝试下载文件
    download_file(ftp, remote_file, local_file)

    ftp.quit()

if __name__ == '__main__':
    main()