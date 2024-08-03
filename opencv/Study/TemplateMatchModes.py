import cv2
from matplotlib import pyplot as plt
# import numpy


# 导入图片
find_pic = cv2.imread("opencv/files/find_pic.png")
ori_pic = cv2.imread("opencv/files/origin_pic.png")
# 确定导入图片的长宽
width, heigth = find_pic.shape[0:2]  # .shape 用于返回一个包含图片的宽、长、深度（2是黑白、3是彩色）的元组，[0:2]表示前两个，即宽和长

# TemplateMatchModes 函数的六种匹配方法
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
# 1. 平方差匹配CV_TM_SQDIFF：用两者的平方差来匹配，最好的匹配值为0
# 2. 归一化平方差匹配CV_TM_SQDIFF_NORMED
# 3. 相关匹配CV_TM_CCORR：用两者的乘积匹配，数值越大表明匹配程度越好
# 4. 归一化相关匹配CV_TM_CCORR_NORMED
# 5. 相关系数匹配CV_TM_CCOEFF：用两者的相关系数匹配，1表示完美的匹配，-1表示最差的匹配
# 6. 归一化相关系数匹配CV_TM_CCOEFF_NORMED


#用六种匹配方法匹配一遍
for meth in methods:
    cp_op = ori_pic.copy()   # 此方法用于图像的拷贝，相当于复制一份，区别于引用，人称深拷贝。如果直接使用等号， 那么两个变量是相关联的，一个变化另一个跟着变化，使用copy后就不会像引用一样了，就独立了
     
    # eval()可以将字符串转化为语句来执行，比如 n = 5  eval("n+5")   结果是 10
    method = eval(meth)
    # 将两个图片通过某个方法相匹配
    result = cv2.matchTemplate(cp_op, find_pic, method)
    # minMaxLoc 用于索引数组中的最大值和最小值，并且返回最大值最小值的索引
    min_val,max_val,min_indx,max_indx=cv2.minMaxLoc(result)
    
    # 计算坐标
    # 如果是平方差匹配TM_SQDIFF或归一化平方差匹配TM_SQDIFF_NORMED，取最小值
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_indx
    else:
        top_left = max_indx
    # 右下角 坐标
    bottom_right = (top_left[0] + width, top_left[1] + heigth)


    # 画个方框看看匹配情况
    cv2.rectangle(cp_op, top_left, bottom_right, 255, 2)

    # 使用 matplotlib 实现窗口绘制
    plt.subplot(121), plt.imshow(result, cmap='gray')
    plt.xticks([]), plt.yticks([])  # 隐藏坐标轴
    plt.subplot(122), plt.imshow(cp_op, cmap='gray')
    plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()

    # 除了TM_CCORR 以外，其他检测方法均完美检测
 