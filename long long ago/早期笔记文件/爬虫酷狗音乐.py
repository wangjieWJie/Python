import requests
ur1=''
res=requests.gets(ur1).content
with open('','wb') as f:
    f.write(res)
    