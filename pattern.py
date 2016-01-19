import cv2
import time
import numpy as np 
import RPi.GPIO as GPIO
import picamera

GPIO.setup(18, GPIO.OUT)
GPIO.setup(11, GPIO.PIN)

while True:
	GPIO.output(18, True)
	time.sleep(5)
	GPIO.output(18, False)
	camera = picamera.PiCamera()
	camera.capture('pic.jpg')
	camera.close()
	result = pattern_check()
	if result = False:
		break
		

def pattern_check():
	img = cv2.imread('pic.jpg')
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray,50,150,apertureSize = 3)
	T_count = 0
	V_count = 0
	H_count = 0
	O_count = 0
	Canny(img,edges,50,200,3)
	lines = cv2.HoughLines(edges,1,np.pi/180,200)
	for rho, theta in lines[0]:
		T_count += 1
		'''
		a = np.cos(theta)
		b = np.sin(theta)
		x0 = a*rho
		y0 = b*rho
		x1 = int(x0 + 1000*(-b))
		x2 = int(y0 + 1000*(a))
		y1 = int(x0 + 1000*(-b))
		y2 = int(x0 + 1000*(a))
		cv2.line(img,(x1, y1),(0,0,255),2)
		'''
		if theta >= np.pi/180*170 or theta <= np.pi/180*10:
			V_count += 1
		elif theta >= np.pi/180*80 and theta <= np.pi/180*100:
			H_count += 1
		else
			O_count += 1
	
	ratio = V_count/(H_count+O_count+1)		
	if V_count < 5 or (H_count+O_count)/(T_count+1)>0.05:
		return False
	else
		return True	

cv2.imwrite('houghlines3.jpg', img)	
