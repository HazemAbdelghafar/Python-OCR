# import the opencv library
import cv2 as cv
from pytesseract import pytesseract
import pyttsx3
from pytesseract import Output

engine = pyttsx3.init()

pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


vid = cv.VideoCapture(0)

while (True):
	ret, frame = vid.read()

	height, width, c = frame.shape
	print(type(frame))


	image_data = pytesseract.image_to_data(frame,output_type=Output.DICT)


	for i,word in enumerate(image_data['text']):
		if word != "":
			x,y,w,h = image_data['left'][i],image_data['top'][i],image_data['width'][i],image_data['height'][i]
			cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0))
			cv.putText(frame,word,(x,y-16), cv.FONT_HERSHEY_COMPLEX, 1, (250,250,200),2)
			print(word)
			engine.say(word)
			engine.runAndWait()

		cv.imshow('frame', frame)
		if cv.waitKey(1) & 0xFF == ord('q'):
			break

vid.release()
cv2.destroyAllWindows()
