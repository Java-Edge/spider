import cv2 as cv

# img = cv.imread("./img/run.png", flags=cv.IMREAD_COLOR)
img = cv.imread("./img/run.png", flags=cv.IMREAD_GRAYSCALE)
# 第一个参数是图像文件的路径
# 第二个参数是读取图像的标志，使用cv.IMREAD_GRAYSCALE标志表示读取灰度图像
# 保存成功后，图像文件将被保存在指定的路径中
cv.imwrite('./img/bg.jpg', img)

# cv.imshow("myImg", img)
# cv.waitKey(0)
# cv.destroyAllWindows()
