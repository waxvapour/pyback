import os
from pydub import AudioSegment
sou = AudioSegment.from_file('benn.wav')
bhenkitakki= sou.dBFS
audioo = 'out15.wav'
soundd = AudioSegment.from_file(audioo)
loudness = soundd.dBFS
print(loudness)
