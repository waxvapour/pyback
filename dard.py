import os
import speech_recognition as sr
import subprocess
from pydub import AudioSegment
sou = AudioSegment.from_file('benn.wav')
bhenkitakki= sou.dBFS
sou = AudioSegment.from_file('bhai.wav')
bhenkatakka= sou.dBFS
r = sr.Recognizer()
a=0
b=368
teri=0
while a<b:
	audioo = 'M1/out'+str(a)+'.wav'
	soundd = AudioSegment.from_file(audioo)
	loudness = soundd.dBFS
	if loudness==bhenkitakki:
		os.remove(audioo)
		print("gungi file thi uda di !")
		a=a+1
	if loudness==bhenkatakka:
		os.remove(audioo)
		print("allmost gungi file thi uda di !")
		a=a+1
	audio = 'M1/out'+str(a)+'.wav'
	with sr.AudioFile(audio) as source:
		audi = r.record(source)
		print ('file NO : '+str(a)+' Done!')
		if teri>0:
			a=a+1
			teri=0
		teri=1
	try:
		text = r.recognize_google(audi)
		f = open('musaibat.txt','a')
		f.write(text + '\n')
		f.close()
		a=a+1
		teri=0
		if(a==b):
			print ('Musibat khatam :-)')

	except Exception as e:
		print (e)
