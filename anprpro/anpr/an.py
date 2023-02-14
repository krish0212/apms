import cv2
import numpy as np
import pytesseract

numberPlateCascade = cv2.CascadeClassifier('haarcascade_plate_number.xml') 
plat_detector =  cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")
img = cv2.imread('C:/Users/ELCOT/Downloads/car.jpg')

#print("image:",img)
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plates = plat_detector.detectMultiScale(img,scaleFactor=1.2, minNeighbors = 5, minSize=(25,25))   
#plates = plat_detector.detectMultiScale2(img)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny_edge = cv2.Canny(gray_image, 170, 200)
contours, new  = cv2.findContours(canny_edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours=sorted(contours, key = cv2.contourArea, reverse = True)[:30]
contour_with_license_plate = None
license_plate = None
x = None
y = None
w = None
h = None
for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.01 * perimeter, True)
        if len(approx) == 4: 
            contour_with_license_plate = approx
            x, y, w, h = cv2.boundingRect(contour)
            license_plate = gray_image[y:y + h, x:x + w] 
            #print("lp:",license_plate)
            break
# Removing Noise from the detected image, before sending to Tesseract
license_plate = cv2.bilateralFilter(license_plate,15,30,30)
(thresh, license_plate) = cv2.threshold(license_plate, 150, 180, cv2.THRESH_BINARY)
#print("lp1:",license_plate)
#Text Recognition
text = pytesseract.image_to_string(license_plate)
#Draw License Plate and write the Text
img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 3) 
img = cv2.putText(img, text, (x-100,y-50), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,255,0), 6, cv2.LINE_AA)
cv2.imshow("License Plate Detection",img)
#print("img",img)
print("License Plate :", text)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
