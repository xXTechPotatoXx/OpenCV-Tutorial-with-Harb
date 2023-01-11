## Importing Necessary Modules
import requests  # to get image from the web
import shutil  # to save it locally
import cv2 as cv

## Set up the image URL and filename
image_url = "https://www.nasa.gov/sites/default/files/images/174116main_2006_01777_highres.jpg"
filename = image_url.split("/")[-1]

# Open the url image, set stream to True, this will return the stream content.
r = requests.get(image_url, stream=True)

# Check if the image was retrieved successfully
if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True

    # Open a local file with wb ( write binary ) permission.
    with open(filename, 'wb') as f:
        shutil.copyfileobj(r.raw, f)

    print('Image sucessfully Downloaded: ', filename)
else:
    print('Image Couldn\'t be retreived')


img = cv.imread("174116main_2006_01777_highres.jpg")
cv.imshow("Logo", img)
cv.waitKey(0)