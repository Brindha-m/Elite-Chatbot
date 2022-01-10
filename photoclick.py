import cv2
import numpy as np 
import os
from os.path import isfile, join

imageName = ''
def clickPhoto():
	global imageName
	if os.path.exists('Camera')==False:
		os.mkdir('Camera')
	
	from time import sleep
	import playsound
	from datetime import datetime

	cam = cv2.VideoCapture(0)
	frame = cam.read()
	playsound.playsound('extrafiles/audios/photoclick.mp3')
	imageName = 'Camera/Camera_'+str(datetime.now())[:19].replace(':', '_')+'.png'
	cv2.imwrite(imageName, frame)
	cam.release()
	cv2.destroyAllWindows()

def viewPhoto():
	from PIL import Image
	img = Image.open(imageName)
	img.show()

