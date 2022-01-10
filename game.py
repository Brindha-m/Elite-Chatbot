from random import *
import playsound
from tkinter import *
from PIL import Image, ImageTk
from threading import Thread
import speech_recognition as sr
import pyttsx3
import time
from pynput.keyboard import Key, Controller

def closeWindow():
	keyboard = Controller()
	keyboard.press(Key.alt_l)
	keyboard.press(Key.f4)
	keyboard.release(Key.f4)
	keyboard.release(Key.alt_l)

try:
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[1].id) #male
	engine.setProperty('volume', 1)
except Exception as e:
	print(e)

def speak(text):
	print(text)
	engine.say(text)
	engine.runAndWait()

def record():
	global userchat
	userchat['text'] = "Listening..."
	r = sr.Recognizer()
	r.dynamic_energy_threshold = False
	r.energy_threshold = 4000
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
		said = ""
		try:
			said = r.recognize_google(audio)
			print(f"\nUser said: {said}")
		except Exception as e:
			print(e)
			speak("I think it is invalid move...")
			return "None"	
	return said.lower()




def isContain(text, lst):
	for word in lst:
		if word in text:
			return True
	return False


def play(gameName):
	speak('')
	if isContain(gameName, ['dice','die']):
		playsound.playsound('extrafiles/audios/dice.mp3')
		result = "You got " + str(randint(1,6))
		return result

	elif isContain(gameName, ['coin']):
		playsound.playsound('extrafiles/audios/coin.mp3')
		p = randint(-10,10)
		if p>0: return "You got Head"
		else: return "You got Tail"

	else:
		print("Game Not Available")


	
