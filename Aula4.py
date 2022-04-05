#falar.py

#pip install pywin32

import win32com.client as win32

speaker=win32.Dispatch('SAPI.SpVoice')
frase='o rato roeu a roupa do rei de roma'
frase2=
#print(frase.split('r'))
#speaker.Speak(frase
speaker.speak(frase.split('r'))
