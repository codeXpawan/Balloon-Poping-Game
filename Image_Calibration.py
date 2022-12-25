import cv2 as cv
import numpy as np
import Resizing_img as ri

img = cv.imread("Balloon/copy.jpg")
img = ri.resize(img, 0.15)
if img is None:
    print("Error opening image")
    exit(1)
cv.imshow("Original", img)
pt_A = [10,476]
pt_B = [641,469]
pt_C = [536,63]
pt_D = [116,119]
# Here, I have used L2 norm. You can use L1 also.
width_AB = np.sqrt(((pt_A[0] - pt_B[0]) ** 2) + ((pt_A[1] - pt_B[1]) ** 2))
width_CD = np.sqrt(((pt_D[0] - pt_C[0]) ** 2) + ((pt_D[1] - pt_C[1]) ** 2))
maxWidth = max(int(width_AB), int(width_CD))


height_AD = np.sqrt(((pt_A[0] - pt_D[0]) ** 2) + ((pt_A[1] - pt_D[1]) ** 2))
height_BC = np.sqrt(((pt_C[0] - pt_B[0]) ** 2) + ((pt_C[1] - pt_B[1]) ** 2))
maxHeight = max(int(height_AD), int(height_BC))
input_pts = np.float32([pt_A, pt_B, pt_C, pt_D])
output_pts = np.float32([[0, maxHeight],
                        [maxWidth, maxHeight],
                        [maxWidth - 1, 0],
                        [0, 0]])
# Compute the perspective transform M
M = cv.getPerspectiveTransform(input_pts,output_pts)
out = cv.warpPerspective(img,M,(maxWidth, maxHeight),flags=cv.INTER_LINEAR)
cv.imshow("Output", out)
cv.waitKey(0)
cv.destroyAllWindows()