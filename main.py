import speech_recognition as sr
from time import strftime
import requests
import espeak
import os
import time
import sys

mic_name = "USB PnP Sound Device: Audio (hw:2,0)"
sample_rate = 48000
chunk_size = 2040

r1 = sr.Recognizer() #The primary purpose of a Recognizer instance is, of course, to recognize speech.

mic_list = sr.Microphone.list_microphone_names()  #method will return a array/list of the connected microphones to the system.

for i, microphone_name in enumerate(mic_list):
    if microphone_name == mic_name:
                 device_id = i

    with sr.Microphone(device_index = device_id, sample_rate = sample_rate, chunk_size = 2040) as source:
            r1.adjust_for_ambient_noise(source)

    print('---------------Say: CHITTI---------------')
    print('speak now')
    audio1 = r1.listen(source) #record audio

    try:
      get1 = r1.recognize_google(audio1) #to attempt to recognize any speech in the audio.
      print('you said: '+ get1)

      if(get1 == 'Chitti'):
          print('Chitti Responce: hi commander! how can i help you?')
          os.system("espeak -ven-us+m3 --stdout 'hi commander, how can i help you?' -a 300 -s 130 | aplay")
      elif(get1 != 'Chitti'):
          print('permission denied!')
          os.system("espeak -ven-us+m3 --stdout 'permission denied' -a 300 -s 130 | aplay")
          sys.exit()
    except sr.UnknownValueError:
          print('error')

    except sr.RequestError as e:
          print('failed'.format(e))

r2 = sr.Recognizer()

while True:
        with sr.Microphone(device_index = device_id, sample_rate = sample_rate, chunk_size = 2040) as source:
             r2.adjust_for_ambient_noise(source)
        print('speak now')
        audio2 = r2.listen(source)
        get2 = r2.recognize_google(audio2)
        print('you said: '+ get2)
        if(get2 == 'what is your name'):
              print('Chitti Responce: i am chitti!')
              os.system("espeak -ven-us+m3 --stdout 'i am chitti!' -a 300 -s 130 | aplay")
        if(get2 == 'how are you'):
              print('Chitti Responce: i am fine!')
              os.system("espeak -ven-us+m3 --stdout 'i am fine' -a 300 -s 130 | aplay")
        if(get2 == 'shutdown'):
              print('Chitti Responce: bye bye sir, have a nice day')
              os.system("espeak -ven-us+m3 --stdout 'bye bye sir, have a nice day' -a 300 -s 130 | aplay")
              sys.exit()
        if(get2 == 'tell about you'):
              print('Chitti Responce: i am chitti!, version=3, speed=4 giga bytes, memory=16 giga bytes')
              os.system("espeak -ven-us+m3 --stdout 'i am chitti!, version 3, speed 4 giga bytes, memory 16 giga bytes' -a 300 -s 130 | aplay")
        if(get2 == 'are you artificial intelligence'):
              print('Chitti Responce: yes, i am')
              os.system("espeak -ven-us+m3 --stdout 'yes, i am' -a 300 -s 130 | aplay")
        if(get2 == 'help'):
              print('Chitti Responce: (1) ' + 'what is your name')
              #os.system("espeak -ven-us+m3 --stdout 'yes, i am' -a 300 -s 130 | aplay")
        if(get2 == 'dance'):
              print('Chitti Responce: dancing!!!...')
              os.system("espeak -ven-us+m3 --stdout 'command activated' -a 300 -s 130 | aplay")
        if(get2 == 'hey robot') or (get2 == 'hi robot') or (get2 == 'hello robot') or (get2 == 'hey Chitti') or (get2 == 'hi Chitti') or (get2 == 'hello Chitti'):
              day_time = int(strftime('%H'))
        if day_time < 12:
              print('Chitti Responce: Hello sir, Good Morning!')
              os.system("espeak -ven-us+m3 --stdout 'Hello sir, Good Morning!' -a 300 -s 130 | aplay")

        elif 12 <= day_time < 18:
              print('Chitti Responce: Hello sir, Good afternoon!')
              os.system("espeak -ven-us+m3 --stdout 'Hello sir, Good afternoon!' -a 300 -s 130 | aplay")

        else:
              print('Chitti Responce: Hello sir, Good evening!')
              os.system("espeak -ven-us+m3 --stdout 'Hello sir, Good evening!' -a 300 -s 130 | aplay")
        if(get2 == 'tell me a joke'):
              res = requests.get('https://icanhazdadjoke.com/',headers={"Accept":"application/json"})
              if res.status_code == requests.codes.ok:
                   print(str(res.json()['joke']))
              else:
                 os.system("espeak -ven-us+m3 --stdout 'oops!, ran out of jokes!!!' -a 300 -s 130 | aplay")
   
        r3 = sr.Recognizer()

        if(get2 == 'open YouTube'):
          import webbrowser as wb
          os.system("espeak -ven-us+m3 --stdout 'Command Activated?' -a 300 -s 130 | aplay")
          link = "https://www.youtube.com/results?search_query="
          wb.open_new_tab(link)
        if(get2 == 'open Google'):
          import webbrowser as wb
          os.system("espeak -ven-us+m3 --stdout 'Command Activated?' -a 300 -s 130 | aplay")
          link = "https://www.google.com"
          wb.open_new_tab(link)
          if(get2 == 'close browser'):
             print('Chitti Responce: closing browser!!!...')
             import os
             browserExe = "chrome.exe"
             os.system("taskkill /f/im" + browserExe)
             os.system("espeak -ven-us+m3 --stdout 'browser closed' -a 300 -s 130 | aplay")
        if(get2 == 'lights on'):
          import paho.mqtt.client as mqtt
          # The callback for when the client receives a CONNACK response from the server.
          def on_connect(client, userdata, flags, rc):
             print("connected with result code" + str(rc))
              # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.

             client.subscribe("/led/pi") #Use subscribe() to subscribe to a topic and receive messages

          client = mqtt.Client()
          client.on_connect = on_connect
          client.connect('localhost', 1883, 60) #Connect to a broker using one of the connect*() functions
          client.loop_start()     #Call one of the loop*() functions to maintain network traffic flow with the broker
          print('script is running, press Ctrl-c to quit...')
          print('button pressed!')
          os.system("espeak -ven-us+m3 --stdout 'button pressed' -a 300 -s 130 | aplay")
          client.publish('/leds/esp8266', 'TOGGLE')#Use publish() to publish messages to the broker
        if(get2 == 'call to Sharif'):
            os.system("espeak -ven-us+m3 --stdout 'calling to sherif' -a 300 -s 130 | aplay")
            print("calling to sherif")
            import serial
            ser = serial.Serial("/dev/ttyUSB0", baudrate = 9600, timeout = 30)
            ser.write(b"ATD8925296352;\r")
       if(get2 == 'attend call') or (get2 == 'attend the call'):
         os.system("espeak -ven-us+m3 --stdout 'attending the call' -a 300 -s 130 | aplay")
         print("attending the call")
         import serial
         ser = serial.Serial("/dev/ttyUSB0", baudrate = 9600, timeout = 30)
         ser.write(b"ATA\r")
       if(get2 == 'record video'):
         os.system("espeak -ven-us+m3 --stdout 'recording video' -a 300 -s 130 | aplay")
         print("recording video")
         import cv2
         cap = cv2.VideoCapture(0)
         fourcc = cv2.VideoWriter_fourcc(*'XVID')
         org_out = cv2.VideoWriter('my_video.avi', fourcc, 20.0, (640,480))
         while True:
          _,frame = cap.read()
          cv2.imshow('video',frame)
          org.out.write(frame)
          if cv2.waitKey(1) and 0xFF == ord('q'):
           break
          cap.release()
          cv2.destroyAllWindows()
