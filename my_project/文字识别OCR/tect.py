import requests
import easyocr

# 设置识别器
# 设置识别中英文两种语言,设置使用GPU
reader = easyocr.Reader(["ch_sim"], gpu=True)
# need to run only once to load model into memory
# result = reader.readtext("file/text.PNG", detail=0)
# print(result)

img = requests.get("https://www.haitangsoshu.org/wzbodyimg/T3koy5.png")
with open("file/img_download/dao.PNG", "wb") as character:
    character.write(img.content)
result = reader.readtext("file/img_download/dao.PNG", detail=100, contrast_ths=0.5)
print(result)
