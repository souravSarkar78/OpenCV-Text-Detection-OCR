import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#pytesseract.pytesseract.tesseract_cmd
img = cv2.imread("image.png")
imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

st = pytesseract.image_to_string(imgrgb)

#s = st.splitlines()
print(st)
cv2.imshow("Result", imgrgb)

cv2.waitKey(0)