import cv2 as cv
import numpy

# img = numpy.zeros((200, 200), numpy.uint8)
# print(img)
# print(type(img))
# for i in range(200):
#     img[100][i] = 255
#
# cv.imshow("img", img)
# cv.waitKey(0)
# cv.destroyAllWindows()

img = cv.imread("./img/run.png", flags=cv.IMREAD_COLOR)
for i in range(len(img)):
    img[i][100] = [100, 100, 255]
cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()