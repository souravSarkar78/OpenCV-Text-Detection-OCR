import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#pytesseract.pytesseract.tesseract_cmd
img = cv2.imread("image.png")



img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


st = pytesseract.image_to_string(img)

def draw_boxes_on_character(img):
    img_width = img.shape[1]
    img_height = img.shape[0]
    boxes = pytesseract.image_to_boxes(img)
    for box in boxes.splitlines():
        box = box.split(" ")
        character = box[0]
        x = int(box[1])
        y = int(box[2])
        x2 = int(box[3])
        y2 = int(box[4])
        cv2.rectangle(img, (x, img_height - y), (x2, img_height - y2), (0, 255, 0), 1)
        cv2.putText(img, character, (x, img_height -y2), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255) , 1)
    return img

def draw_boxes_on_strings(img):
    boxes = pytesseract.image_to_data(img)
    for count, data in enumerate(boxes.splitlines()):
        if count > 0:
            data = data.split()
            if len(data) == 12:
                x, y, w, h, content = int(data[6]), int(data[7]), int(data[8]), int(data[9]), data[11]
                cv2.rectangle(img, (x, y), (w+x, h+y), (0, 255, 0), 1)
                cv2.putText(img, content, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255) , 1)
                
    return img

img = draw_boxes_on_character(img)
#img = draw_boxes_on_strings(img)

#print(bo)
cv2.imshow("Result", img)

cv2.waitKey(0)