import cv2
import numpy as np
image = cv2.imread("C:/Users/lenovo/PycharmProjects/chepai/insect.png")
cv2.imshow("initial", image)
cv2.waitKey()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)
gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient)
cv2.imshow("first", gradient)
cv2.waitKey()
blurred = cv2.blur(gradient, (9, 9))
(_, thresh) = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)
cv2.imshow("thresh", thresh)
cv2.waitKey()
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
cv2.imshow("closed1", closed)
cv2.waitKey()
closed = cv2.erode(closed, None, iterations=4)
closed = cv2.dilate(closed, None, iterations=4)
cv2.imshow("closed2", closed)
cv2.waitKey()
(cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
rect = cv2.minAreaRect(c)
box = np.int0(cv2.boxPoints(rect))
cv2.drawContours(image, [box], -1, (0, 255, 0), 3)
cv2.imshow("Image", image)
cv2.imwrite("contoursImage2.jpg", image)
cv2.waitKey(0)
Xs = [i[0] for i in box]
Ys = [i[1] for i in box]
x1 = min(Xs)
x2 = max(Xs)
y1 = min(Ys)
y2 = max(Ys)
hight = y2 - y1
width = x2 - x1
cropImg = image[y1:y1+hight, x1:x1+width]
cv2.imshow("cropImg", cropImg)
#cv2.imwrite("insect.png", cropImg)
cv2.waitKey()

