import numpy as np
import cv2 as cv


## Importing Necessary Modules
import requests  # to get image from the web
import shutil  # to save it loca

## Set up the image URL and filename
# image_url = "https://www.nasa.gov/sites/default/files/images/174116main_2006_01777_highres.jpg"
# filename = image_url.split("/")[-1]
#
# # Open the url image, set stream to True, this will return the stream content.
# r = requests.get(image_url, stream=True)
#
# # Check if the image was retrieved successfully
# if r.status_code == 200:
#     # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
#     r.raw.decode_content = True
#
#     # Open a local file with wb ( write binary ) permission.
#     with open(filename, 'wb') as f:
#         shutil.copyfileobj(r.raw, f)
#
#     print('Image sucessfully Downloaded: ', filename)
# else:
#     print('Image Couldn\'t be retreived')
#
#
# img = cv.imread("174116main_2006_01777_highres.jpg")
# cv.imwrite("NASALogo.png", img)
# cv.imshow("Logo", img)
# cv.waitKey(0)

#_______________________________________________________________________________________________________________________

## This is video capture, play, and save

# cap = cv.VideoCapture(0)
# chk = cap.isOpened()
# print(chk)
# fourcc = cv.VideoWriter_fourcc(*"DIVX")
# out = cv.VideoWriter("output.avi", fourcc, 30.0, (640, 480))
# outGray = cv.VideoWriter("output-gray.avi", fourcc, 30.0, (640, 480), 0)
# while True:
#     ret, vid = cap.read()
#     out.write(vid)
#     gray = cv.cvtColor(vid, cv.COLOR_BGR2GRAY)
#     outGray.write(gray)
#
#
#     cv.imshow("output", vid)
#     cv.imshow("gray", gray)
#     if cv.waitKey(1) == ord("q"):
#         break
#
# cap.release()
# out.release()
# outGray.release()
# cv.destroyAllWindows()
#
#
#
# # cap = cv.VideoCapture("output-gray.avi")
# # while cap.isOpened():
# #     ret, frame = cap.read()
# #     print(frame)
# #     cv.imshow("gray", frame)
# #     if cv.waitKey(1) == ord("q"):
# #         break
#
#
#
# cap = cv.VideoCapture("output.avi")
# while cap.isOpened():
#     ret, frame = cap.read()
#     print(frame)
#     cv.imshow("video", frame)
#     cv.waitKey(2)


#_______________________________________________________________________________________________________________________


# img = cv.imread("C:/Users/nuras/Pictures/ProjectPictures/mint.png")
# cv.imwrite("mint.png", img)
# cv.imshow("mint", img)
# cv.waitKey(0)


img = cv.imread('mint.png')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('imgray', imgray)
ret, thresh = cv.threshold(imgray, 190, 255, 0)
print(thresh)
cv.imshow("Thresh", thresh)
cv.waitKey(0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cont = cv.drawContours(img, contours, -1, (0,255,0), 3)
cv.imshow("contours", cont)
cv.waitKey(0)





















#_______________________________________________________________________________________________________________________

## Corner and Edge Dections using Harris Corner and more

# img = cv.imread("C:/Users/nuras/Pictures/ProjectPictures/blocks.png")
# cv.imwrite("blocks.png", img)
# cv.imshow("blocks", img)
# cv.waitKey(0)


#
# img = cv.imread("blocks.png")
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# # gray = np.float32(gray)
#
# while True:
#     cv.imshow("gray blocks", gray)
#     if cv.waitKey(1) == ord("q"):
#         break
#
# dst = cv.cornerHarris(gray, 3, 3, 0.04)
# dst = cv.dilate(dst, None)
#
# img[dst>0.01*dst.max()]=[0,0,255]
#
# while True:
#     cv.imshow('dst',gray)
#     if cv.waitKey(1) == ord('q'):
#         cv.destroyAllWindows()
#         break

#_______________________________________________________________________________________________________________________