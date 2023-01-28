# bitwise_and(src1, src2, dst=None, mask=None)
# bitwise_or(src1, src2, dst=None, mask=None)
# bitwise_xor(src1, src2, dst=None, mask=None)
# bitwise_not(src1, src2, dst=None, mask=None)

import cv2
import numpy as np
white = cv2.imread("white.png")
yellow = cv2.imread("yellow.png")
mixed = cv2.bitwise_or(white, yellow)
# cv2.imshow("mixed", mixed)

# 获取原始图像的行和列
row, col = mixed.shape[:2]
# 定义多边形的顶点
bottom_left = [col * 0.05, row]
top_left = [col * 0.45, row * 0.6]
top_right = [col * 0.55, row * 0.6]
bottom_right = [col * 0.95, row]
# 使用顶点定义多边形
vertices = np.array([bottom_left, top_left, top_right, bottom_right], dtype=np.int32)

roi_mask = np.zeros((row, col), dtype=np.uint8)
cv2.fillPoly(roi_mask, [vertices], 255)
# cv2.imshow("roi_mask", roi_mask)

roi = cv2.bitwise_and(mixed, mixed, mask=roi_mask)
cv2.imwrite("final_roi.png", roi)
cv2.waitKey()