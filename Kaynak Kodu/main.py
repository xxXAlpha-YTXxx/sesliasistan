# by Bozkurtlig
# Lütfen Kodları Kurcalama
import speech_recognition as sr
import webbrowser
from random import *
import string
from gtts import gTTS
import os
import time
import playsound

r = sr.Recognizer()

playsound.playsound("Sesler\ebastasoyle.mp3")

while True:
    while True:
        while True:
            try:
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    data = r.record(source, duration=5)
                    print("Sesinizi Tanımlıyor…")
                    text = r.recognize_google(data, language='tr-TR') 
                    print("Anladığım Kelime Veya Cümle : " + text)
                    break
            except sr.UnknownValueError:
                playsound.playsound("Sesler\eanlayamadim.mp3")

        if "selamınaleyküm" in text.lower():
            playsound.playsound("Sesler\elaykumselam.mp3")

        elif "selamın aleyküm" in text.lower():
            playsound.playsound("Sesler\elaykumselam.mp3")

        elif "selamünaleyküm" in text.lower():
            playsound.playsound("Sesler\elaykumselam.mp3")

        elif "selamün aleyküm" in text.lower():
            playsound.playsound("Sesler\elaykumselam.mp3")
              
        elif "selam" in text.lower():
            playsound.playsound("Sesler\sanadaselam.mp3")
                        
                
        elif "merhaba" in text.lower():
            playsound.playsound("Sesler\sanadamerhaba.mp3")
                        

        elif "çık" in text.lower():
            playsound.playsound("Sesler\gulegule.mp3")
            quit()
                        
        elif "güle güle" in text.lower():
            playsound.playsound("Sesler\gulegule.mp3")
            quit()

        elif "youtube'da ara" in text.lower():
            playsound.playsound("Sesler\earamakistersin.mp3")
            while True:
                try:
                    with sr.Microphone() as source:
                        r.adjust_for_ambient_noise(source)
                        data = r.record(source, duration=5)
                        print("Sesinizi Tanımlıyor…")
                        text = r.recognize_google(data, language='tr-TR') 
                        print("Anladığım Kelime Veya Cümle : " + text)
                        break
                except sr.UnknownValueError: 
                    playsound.playsound("Sesler\eanlayamadim.mp3")
                
            webbrowser.open("https://www.youtube.com/results?search_query=" + text)

        elif "youtube" in text.lower():
            webbrowser.open("https://youtube.com")

        elif "google" in text.lower():
            webbrowser.open("https://google.com")

        elif "instagram" in text.lower():
            webbrowser.open("https://instagram.com")
            
        elif "sana küstüm" in text.lower():
            playsound.playsound("Sesler\guleguleozaman.mp3")
            quit()

        elif "sana küstüm" in text.lower():
            playsound.playsound("Sesler\guleguleozaman.mp3")
            quit()

        elif "şifre üret" in text.lower():
            characters = string.ascii_letters + string.punctuation  + string.digits
            password =  "".join(choice(characters) for x in range(randint(7, 14)))
            print(password)

        elif "şifre at" in text.lower():
            characters = string.ascii_letters + string.punctuation  + string.digits
            password =  "".join(choice(characters) for x in range(randint(7, 14)))
            print(password)

                
        elif "ara" in text.lower():
            playsound.playsound("Sesler\earamakistersin.mp3")
            while True:
                try:
                    with sr.Microphone() as source:
                        r.adjust_for_ambient_noise(source)
                        data = r.record(source, duration=5)
                        print("Sesinizi Tanımlıyor…")
                        text = r.recognize_google(data, language='tr-TR') 
                        print("Anladığım Kelime Veya Cümle : " + text)
                        break
                except sr.UnknownValueError: 
                    playsound.playsound("Sesler\eanlayamadim.mp3")
                
            webbrowser.open("https://www.google.com/search?q=" + text)


        elif "yapımcın kim" in text.lower():
            playsound.playsound("Sesler\yapimcinkim.mp3")

        elif "nasılsın" in text.lower():
            playsound.playsound("Sesler\iyiyim.mp3")

        elif "bilgisayarı kapat" in text.lower():          
            onay = input("Bilgisayar Kapatılsınmı (Kapatılmasını İsterseniz Enter Tuşuna İstemezseniz Ctrl + C Tuşuna Basınız) : ")           
            os.system("shutdown /p")

        elif "kapat" in text.lower():
            playsound.playsound("Sesler\gulegule.mp3")
            quit()

        elif "bay bay" in text.lower():
            playsound.playsound("Sesler\ebaybay.mp3")
            quit()

        elif "baybay" in text.lower():
            playsound.playsound("Sesler\ebaybay.mp3")
            quit()
        
        elif "adın ne" in text.lower():
            playsound.playsound("Sesler\eadinne.mp3")

        elif "sen kimsin" in text.lower():
            playsound.playsound("Sesler\eadinne.mp3")
               
        else:
            playsound.playsound("Sesler\komutyok.mp3")



