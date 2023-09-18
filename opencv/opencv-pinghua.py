import cv2 as cv
import numpy

img = cv.imread("./img/数据中台.png", flags=cv.IMREAD_GRAYSCALE)


# result = cv.blur(img, (5, 5))
result2 = cv.GuassianBlur(img, (5, 5), 1)




cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()
