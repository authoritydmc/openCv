import urllib.request
import cv2
import numpy as np
import ssl
import config
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
def read_webcam():

    try:
        imgResp = urllib.request.urlopen(config.url_webcam)
        # print("gathered Image Response")
        res_byte_arr=imgResp.read()
        # print("gathered res byte array")
        imgNp = np.array(bytearray(res_byte_arr), dtype=np.uint8)
        # print("Converted to NP array")
        img = cv2.imdecode(imgNp, -1)
        # print("Decoded using imdecode")
        return img
        # return the image
    except Exception as e:
        print("Exception occured ..",e)
        print("Are you sure IP webcam app is running in your phone")
        return None


read_webcam()
