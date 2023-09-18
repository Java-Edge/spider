import cv2 as cv
import numpy

img = cv.imread("./img/数据中台.png", flags=cv.IMREAD_GRAYSCALE)

# 使用切片操作将img变量中的图像数据按照[100:300, 100:300]的范围进行切片
# 即从第100行到第300行，第100列到第300列的区域
# 最后，使用cv.imshow()函数将切片后的图像数据显示出来。
# roi = img[100:300, 100:300]
# 将图像数据显示出来，第一个参数是窗口的名称，第二个参数是要显示的图像数据
# cv.imshow("img", roi)


# cover = numpy.ones((873, 1003, 3), numpy.uint8) * 50
# result = cv.add(img, cover)

thresh, results = cv.threshold(img, 180, 255, cv.THRESH_BINARY)

cv.imshow("img", img)


cv.waitKey(0)
cv.destroyAllWindows()
