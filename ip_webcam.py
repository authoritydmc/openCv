import urllib.request
import cv2
import numpy as np
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print("....")
while True:
    print("Starting")
    imgResp = urllib.request.urlopen(url)
    # print("gathered Image Response")
    res_byte_arr=imgResp.read()
    # print("gathered res byte array")
    imgNp = np.array(bytearray(res_byte_arr), dtype=np.uint8)
    # print("Converted to NP array")
    img = cv2.imdecode(imgNp, -1)
    # print("Decoded using imdecode")
    cv2.imshow('temp',cv2.resize(img,(600,400)))
    q = cv2.waitKey(1) & 0xFF
    if q == 27:
        break

cv2.destroyAllWindows()