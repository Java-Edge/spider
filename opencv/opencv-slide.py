import cv2 as cv
import numpy 

img = cv.imread("./img/数据中台.png", flags=cv.IMREAD_GRAYSCALE)
roi = img[150:250, 150:250]

match = cv.matchTemplate(img, roi, cv.TM_CCORR_NORMED)
info = cv.minMaxLoc(match)
print(info)

cv.imshow("img", img)


cv.waitKey(0)
cv.destroyAllWindows()
