import cv2
import time
import numpy as np 
import RPi.GPIO as GPIO
import picamera

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
input_state = GPIO.input(18)

while True:
	GPIO.output(14, True)
	print "Starting conveyor..."
	time.sleep(3)
	GPIO.output(14, False)
	print "Stopping conveyor..."
	camera = picamera.PiCamera()
	time.sleep(0.2)
	camera.resolution(640, 480)
	camera.capture('pic.jpg')
	camera.close()
	print "Image captured"
	result = pattern_check()
	if result == False:
		print "Pattern is not matching. Halting the conveyor...\nTriggering buzzer...\nSending text message to admin..."
		GPIO.output(15, True)
		time.sleep(0.2)
		GPIO.output(15, False)
		while input_state == True:
			print "Press button to restart"
        		break	

def pattern_check():
	img = cv2.imread('pic.jpg')
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray,50,150,apertureSize = 3)
	T_count = 0
	V_count = 0
	H_count = 0
	O_count = 0
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
		else:
			O_count += 1
	
	ratio = V_count/(H_count+O_count+1)		
	if V_count < 5 or (H_count+O_count)/(T_count+1)>0.05:
		return False
	else
		return True	

cv2.imwrite('houghlines3.jpg', img)	
