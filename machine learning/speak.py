import pyaudio
import wave
import speech_recognition as sr
import subprocess
from commands import Commander

running = True

def play_audio(filename):

    chunk = 1024
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()

    stream = p.open(
        format = p.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True)
    data = wf.readframes(chunk)

    while data != '':
        stream.write(data)
        data = wf.readframes(chunk)

    stream.close()
    p.terminate()


#play_audio('./audio/two.wav')

def initSpeech():
    r = sr.Recognizer()
    cmd = Commander()
    
    print("Listening")
    #play_audio('./audio/before.wav')
        
    with sr.Microphone() as source:                # use the default microphone as the audio source
        print("say something")
        audio = r.listen(source) 

    #play_audio('./audio/after.wav')
    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        print("please repeat")

    print("Your command:" )
    print(command)

    if command in ["quit", "exit", "bye", "goodbye"]:
        global running 
        running = False

    command = command.replace("'", "")
    cmd.discover(command)
    
    #say('You said: ' + command)

def say(text):
    subprocess.call('say ' + text, shell = True)
    

while running == True:
    initSpeech()














    
    
