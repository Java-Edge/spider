import cv2 as cv
import numpy

img = cv.imread("./img/数据中台.png", flags=cv.IMREAD_GRAYSCALE)

img = numpy.zeros((500, 500), numpy.uint8)
img[160:300, 200:300] = 255
img[230:270, 230:270] = 0

kernel = numpy.ones((3, 3), numpy.uint8)
# result = cv.erode(img, iterations=1, kernel=kernel)
result = cv.dilate(img, iterations=2, kernel=kernel)

cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()
