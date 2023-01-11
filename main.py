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

cap = cv.VideoCapture(0)
chk = cap.isOpened()
print(chk)
fourcc = cv.VideoWriter_fourcc(*"DIVX")
out = cv.VideoWriter("output.avi", fourcc, 30.0, (640, 480))
outGray = cv.VideoWriter("output-gray.avi", fourcc, 30.0, (640, 480), 0)
while True:
    ret, vid = cap.read()
    out.write(vid)
    gray = cv.cvtColor(vid, cv.COLOR_BGR2GRAY)
    outGray.write(gray)


    cv.imshow("output", vid)
    cv.imshow("gray", gray)
    if cv.waitKey(1) == ord("q"):
        break

cap.release()
out.release()
outGray.release()
cv.destroyAllWindows()



cap = cv.VideoCapture("output-gray.avi")
while cap.isOpened():
    ret, frame = cap.read()
    print(frame)
    cv.imshow("gray", frame)
    if cv.waitKey(1) == ord("q"):
        break

frame.release()
cap.release()

cap = cv.VideoCapture("output.avi")
while cap.isOpened():
    ret, frame = cap.read()
    print(frame)
    cv.imshow("video", frame)
    cv.waitKey(2)


#_______________________________________________________________________________________________________________________



