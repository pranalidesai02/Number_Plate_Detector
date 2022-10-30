import cv2
import pytesseract
import PythonScript

LIST = ["21 BH 0001 AA","21 BH 2345 AA","KA 05 MG 1909","KA 19 EQ 1316","KA 19 P 8488"]
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract'

cam = cv2.VideoCapture(0)
#cv2.namedWindow("output", cv2.WINDOW_NORMAL)
#cv2.resizeWindow("output", 640,480)

#currentframe = 0

success,frame = cam.read()

while success:
    # cv2.waitKey(100)
    success,frame = cam.read()
    if not success:
        break
    
    # We are creating a variable gray_image. We are then passing our input image to cv2.cvtColor. 
    # cv2.COLOR_BGR2GRAY specifies that the image should be converted to grey image.
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

    # We are reducing the noise in the grey image hence smoothening it.
    gray_image = cv2.bilateralFilter(gray_image, 11, 17, 17)

    # We are creating variable edged. We are then passing our smoothened image to cv2.canny to detect the edges in it. 
    edged = cv2.Canny(gray_image, 30, 200)

    # cnts: This represents the contours.
    # RETR_LIST: It retrieves all the contours
    # CHAIN_APPROX_SIMPLE: Removes all the redundant points on the contours detected
    cnts,new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    # image1=frame.copy()
    # We are drawing the identified contours on our image. Input the values as they are.
    # cv2.drawContours(image1,cnts,-1,(0,255,0),3)

    # We are sorting contours based on the minimum area 30 and ignoring the ones below that.
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True) [:30]
    # Stores the number plate contour
    screenCnt = None
    
    #image2 = frame.copy()
    # Draws the sorted contours on the image.
    #cv2.drawContours(image2,cnts,-1,(0,255,0),3)
    new_img = frame.copy()
    for c in cnts:
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
        if len(approx) == 4: 
            screenCnt = approx
            x,y,w,h = cv2.boundingRect(c) 
            new_img=frame[y:y+h,x:x+w]
            break
    
    image = frame.copy()
    try:
        cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
        cv2.imshow("output",image)
    except:
        cv2.imshow("output",frame)

    plate = pytesseract.image_to_string(new_img, lang='eng')
    
    if any(word in plate for word in LIST):
        print("Number plate is:", plate)
        PythonScript.license_plate_detected()
        break

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()            
