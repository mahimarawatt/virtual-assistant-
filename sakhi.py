import pyttsx3
import speech_recognition 
import requests
from requests import get
from bs4 import BeautifulSoup
import datetime
import os
import random
import json
from urllib.request import urlopen
import wikipedia
import pywhatkit as kit
import wolframalpha
import pyautogui
import cv2
import smtplib
from mail import senderemail, epwd
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import time 
from newsapi import NewsApiClient
from news import speak_news, getNewsUrl
import randfacts
import pyjokes
import psutil
import sounddevice
from scipy.io.wavfile import write
import winshell



engine = pyttsx3.init("sapi5") 
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#################################################################################################################

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone(device_index=0) as source:
        print("Listening.....")
        # speak("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


#################################################################################################################

# to got user location.
def My_location():   
    ip_ad=requests.get('https://api.ipify.org').text
    url= 'https://get.geojs.io/v1/ip/geo/'+ip_ad+".json"    # revel user location.
    r=requests.get(url)
    r=r.json()   
    city=r['city']
    country=r["country"]
    speak(f"you are in {city,country}")

#################################################################################################################

# for maths and science

def wolfram(query):    
    api_id ="KX9VK9-Y4JX8EG7YT"
    requester=wolframalpha.Client(api_id)
    requested=requester.query(query)
    try:
        ans=next(requested.results).text
        return ans
    except:
        speak("Sorry, not got any answer")

#################################################################################################################
# for maths calculations.
def calculation(query):  
    query=str(query)
    query=query.replace("jarvis","")
    query=query.replace("plus","+")
    query=query.replace("multiply","*")
    query=query.replace("into","*")
    query=query.replace("minus","-")
    query=query.replace("divide","/")

    query=str(query)
    try:
        result=wolfram(query)
        speak(f"answer is {result}")
        print(f"answer is {result}")
    except:
        speak("Sorry, did not got the answer")

#################################################################################################################
# date function...show current date.
def time():      
    today=datetime.datetime.now()
    format = '%I:%M %p'
    time = today.strftime(format)
    speak(time)
    print(time)

#################################################################################################################
def date():      
    date = int(datetime.datetime.now().day)
    mon = int(datetime.datetime.now().month)
    speak("Today's date is ")
    speak(date)
    print(date)
    speak(mon)
    print(mon)

#################################################################################################################
# current year 
def year():
    year = int(datetime.datetime.now().year)
    speak("year is ")
    speak(year)
    print(year)



#################################################################################################################
# sending email
def sendEmail(receiver, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email['subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()


#################################################################################################################
def sendwhatsmsg(phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com//send?phone='+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')


#################################################################################################################
# def screenshot():
#     name_img = tt.time() # will name the image using time module , will take current time as name 
#     name_img = 'C:\\Users\\Mahima\\Desktop\\project\\fp\\screenshot\\{name_img}.png'
#     img = pyautogui.screenshot(name_img)
#     img.show()

def screenshot():
    img = pyautogui.screenshot()
    speak("By what name should I save it?")
    ans=takeCommand()
    #Replace FolderPath with the path of folder where you want to save your screenshots in your computer 
    ans="C:\\Users\\Mahima\\Desktop\\project\\fp\\screenshot"+ans+".png"
    img.save(ans)
    speak("Screenshot taken")


#################################################################################################################
def CPUstatus():
    usage=str(psutil.cpu_percent())
    speak('Current CPU usage is at '+usage + "%")
    print('Current CPU usage is at '+usage + "%")
    battery = psutil.sensors_battery()
    speak("Battery remaining is " + str(battery.percent)+"%")
    print("Battery remaining is " + str(battery.percent)+"%")
    hdd = psutil.disk_usage('/')
    hddusage=(hdd.used/hdd.total)*100
    hddusage=round(hddusage,2)
    speak("Storage used in C Drive is "+str(hddusage)+"%")
    print("Storage used in C Drive is "+str(hddusage)+"%")
    frequency=psutil.cpu_freq()
    speak("Current frequency of CPU is "+str(frequency.current)+" Megha Hetz")
    print("Current frequency of CPU is "+str(frequency.current)+" Megha Hetz")
    RAMused=psutil.virtual_memory().percent
    speak("RAM used is "+str(RAMused)+"%")
    print("RAM used is "+str(RAMused)+"%")


#################################################################################################################
def help():
    speak("Here are the keywords that should be in your command for following work to be done")
    speak("dictionary to know meaning of any word")
    speak("TIME to get time")
    speak("DATE to get date")
    speak("CPU STATUS to get information about present condition of CPU")
    speak("JOKE to listen a joke")
    speak("SCREENSHOT to get screenshot")
    speak("mail to send mail to anyone")
    speak("WIKIPEDIA to get do wikipedia search")
    speak("ip address to know your ip address")
    speak("SEARCH to do google search")
    speak("SONG to start a song")
    speak("REMENBER if you want me to remember something")
    speak("reminders if you want me to tell you what you have asked me to remember earlier")
    speak("WEATHER to know a weather forcast")
    speak("facts or fact to know some random facts")
    speak("photo to take a photo")
    speak(" and speak HELP to repeat these thing again")



##################################################################################################

def voice_recorder():
    speak('Enter the time duration in seconds')
    fs=44100
    second = int(input("Enter the time duration in seconds : "))
    speak('Recording voice')
    record_voice = sounddevice.rec(int(second * fs),samplerate=fs,channels=2)
    sounddevice.wait()
    write("Output.wav",fs,record_voice)
    print("Finished....\nPlease Check it......")

##################################################################################################

def takePicture():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    (grabbed, frame) = cap.read()
    showimg = frame
    cv2.imshow('img1', showimg)  # display the captured image
    cv2.waitKey(1)
    #time.sleep(0.3) # Wait 300 miliseconds
    speak("Photo clicked")
    speak("By what name should I save it?")
    im=takeCommand()
    image = "C:\\Users\\Mahima\\Desktop\\project\\fp\\captured_pictures"+im+".png"
    cv2.imwrite(image, frame)
    cap.release()
    return image
    speak("photo saved")

##################################################################################################



# def camera():
#     speak("Press space to take image and escape to stop Camera")
#     Camera = cv2.VideoCapture(0)
#     cv2.namedWindow("Camera")
#     img_counter = 0
#     while True:
#         ret, frame = Camera.read()
#         if not ret:
#             print("failed to grab frame")
#             break
#         cv2.imshow("Camera", frame)
#         k = cv2.waitKey(1)
#         if k%256 == 27:
#             speak("closing camera")
#             break
#         elif k%256 == 32:
#             img_name = "camera{}.png".format(img_counter)
#             #Replace CameraPath with the path of the folder where you want to save your photos taken by camera
#             path="CameraPath"
#             cv2.imwrite(os.path.join(path , img_name), frame)
#             cv2.imwrite(img_name, frame)
#             speak("{} image taken".format(img_name))
#             img_counter += 1
#     Camera.release()
#     cv2.destroyAllWindows() 



#https://api.openweathermap.org/data/2.5/weather?q={Bangalore}&units=imperial&appid={47865040d10346f46c21ac9b33ba84a3}
    

##############################################################################################################
if __name__ == "__main__":
    # while True:
    #     query = takeCommand().lower()
        
    #     if "wake up" in query:
    #         from GreetMe import greetMe
    #         greetMe()
            
            while True:
                query = takeCommand().lower()
                if "go to sleep" in query :
                    speak("Ok , You can call me anytime")
                    break 

                elif "hello" in query :
                    speak("Hello, how are you ?")
                    print("Hello, how are you ?")
                
                elif "What is your name" in query :
                    speak("My name is sakhi. I am your personal assistant")
                    print("My name is sakhi. I am your personal assistant")

                elif "i am fine"  in query:
                    speak("that's great")
                    print("that's great")

                elif "how are you" in query:
                    speak("I am doing great")
                    print("I am doing great")

                elif "thank you" in query:
                    speak("you are welcome")
                    print("you are welcome")

                elif "are you there?" in query:
                    speak("yes, at your service")
                    print("yes, at your service")

                elif 'what are you doing' in query:
                    speak("I am here talking to you. That's what I am doing")
                    print("I am here talking to you. That's what I am doing")

                elif 'what am i doing' in query:
                    speak("You tell me. My guess is you are talking to me")
                    print("You tell me. My guess is you are talking to me")

                


                #Personalized Playlist : Make your own playlist and let sakhi play a random song from it...
                elif "tired" in query:
                    speak("Playing your favourite songs")
                    a = (1,2,3,4) # You can choose any number of songs 
                    b = random.choice(a)
                    if b==1:
                        wb.open("https://www.youtube.com/watch?v=kpNYfy0Do0I")
                    elif b==1:
                        wb.open("https://www.youtube.com/watch?v=GtomcMiBLvc")
                    elif b==1:
                        wb.open("https://www.youtube.com/watch?v=25B35c1LkBQ")
                    elif b==1:
                        wb.open("https://www.youtube.com/watch?v=Br1Gl6TZzhI")


                # contolling the volume and all
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")

                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")

                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume kup,sir")
                    volumeup()

                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()


                # for opening and closing tabs (Dictapp file)
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                
                #searching from web
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)

                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                
                
                #wikipedia
                elif 'wikipedia' in query:
                    speak('Searching Wikipedia....')
                    query = query.replace('wikipedia', '')
                    results = wikipedia.summary(query, sentences=2)
                    speak('According to Wikipedia')
                    print(results)
                    speak(results)

                # #temperature and weather in bangalore
                # elif "temperature" in query:
                #     search = "temperature in bangalore"
                #     url = f"https://www.google.com/search?q={search}"
                #     r  = requests.get(url)
                #     data = BeautifulSoup(r.text,"html.parser")
                #     temp = data.find("div", class_ = "BNeawe").text
                #     speak(f"current{search} is {temp}")
                
            
                elif "weather" in query:
                    search = "weather in bangalore"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")


                # ##News Function : It will help you to get the top headlines in your chosen field
                # elif 'news' in query:
             
                #     try:
                #         jsonObj = urlopen('''https://newsapi.org/v2/top-headlines?country=in&apiKey=cfa45cded4034f2eb39a246d566c42c4''')
                #         data = json.load(jsonObj)
                #         i = 1
                 
                #         speak('here are some top news from the times of india')
                #         print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                #         for item in data['articles']:
                     
                #             print(str(i) + '. ' + item['title'] + '\n')
                #             print(item['description'] + '\n')
                #             speak(str(i) + '. ' + item['title'] + '\n')
                #             speak(item['description'] + '\n')
                #             i += 1
                #     except Exception as e:
                 
                #          print(str(e))
                
                
                #time 
                elif("time" in query):
                    query=query.replace("what is","")
                    time()

                #time 
                elif("date" in query):
                    query=query.replace("what is","")
                    date()

                elif("year" in query):
                    query=query.replace("what is","")
                    year()

                elif "finally sleep" in query:
                    speak("Going to sleep,sir")
                    exit()

                #REMINDER
                elif "remember that" in query:
                    speak("What should I remember ?")
                    data = takeCommand()
                    speak("you said to remember " +data)
                    
                    remember = open('data.txt','w')
                    remember.write(data)
                    remember.close()

                elif "reminders" in query or "do you remember anything" in query:
                    remember = open("data.txt","r") # open new file "Remember.txt"
                    speak("You told me " + remember.read())
                    
                #ip address
                elif "ip address" in query:
                    ip = get('https://api.ipify.org').text
                    speak(f"your IP address is {ip}")
                    print(f"your IP address is {ip}")

                # DICTIONARY 
                elif 'dictionary' in query:
                    from diction import translate
                    speak('What you want to search in your intelligent dictionary?')
                    print('What you want to search in your intelligent dictionary?')
                    translate(takeCommand())

                elif 'contact' in query:
                    from contact import contact
                    speak("whose contact info you want to search?")
                    contact(takeCommand())

                elif("location" in query):
                    My_location()

                elif("minus" in query or "add" in query or "calculation" in query or "plus" in query or "calculate" in query or "-" in query or "+" in query):
                    calculation(query)

                
                elif 'mail' in query:
                    email_list = {
                        'test mail':'mahimarawat22@gmail.com',
                        'mahima' :'mahiamr8420@gmail.com'
                    }
                    try: 
                        speak("To whom you want to send the mail?")
                        print("To whom you want to send the mail?")
                        name = takeCommand()
                        receiver = email_list[name]
                        speak("What is the subject of the mail?")
                        print("What is the subject of the mail?")
                        subject = takeCommand()
                        speak('what should i say?')
                        print('what should i say?')
                        content = takeCommand()
                        sendEmail(receiver, subject, content)
                        speak("email has been sent")
                        print("email has been sent")
                    except Exception as e:
                        print(e)
                        speak("unable to send  the mail")

                
                elif 'message' in query:
                    user_name = {
                        'Friend' : '+91 82966 00633'
                    }
                    try: 
                        speak("To whom you want to send the whats app message?")
                        name = takeCommand()
                        phone_no = user_name[name]
                        speak("What is the message ?")
                        message = takeCommand()
                        sendwhatsmsg(phone_no,message)
                        speak("message has been sent")
                    except Exception as e:
                        print(e)
                        speak("unable to send the message")

                elif 'news' in query.lower():
                    speak('Ofcourse sir..')
                    speak_news()
                    speak('Do you want to read the full news...')
                    test = takeCommand()
                    if 'yes' in test:
                        speak('Ok Sir, Opening browser...')
                        wb.open(getNewsUrl())
                        speak('You can now read the full news from this website.')
                    else:
                        speak('No Problem Sir')


                elif "facts" in query or "fact" in query or "facts" in query.lower():
                    a = randfacts.get_fact()
                    b = randfacts.get_fact()
                    c = randfacts.get_fact()
                    
                    x = a #, b, c
                    facts = ("one", "two" ,"three")
                    for i in range(len(facts)):
                        print(f"Fact number {facts[i]}:", x[i])
                        speak(f"Fact number {facts[i]}:, {x[i]}")

                elif "tell me a joke" in query or "joke" in query:
                    joke = pyjokes.get_joke()
                    speak(joke)
                    print

                # elif "voice" in query:
                #     if 'female' in query:
                #         engine.setProperty('voice', voices[1].id)
                #     else:
                #         engine.setProperty('voice', voices[0].id)
                #     speak("Hello, I have switched my voice. How is it?")
                
            #shut down

                elif "shutdown the system" in query:
                    shutdown = speak("Are You sure you want to shutdown ? Yes or No")
                    print("Are You sure you want to shutdown ? Yes or No")
                    #shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 3")

                    elif shutdown == "no":
                        break

                elif "weather" in query:
                    url = "https://api.openweathermap.org/data/2.5/weather?q=Bangalore&units=imperial&appid=47865040d10346f46c21ac9b33ba84a3"
                    
                    res = requests.get(url)
                    data = res.json()

                    weather = data['weather'] [0] ['main']
                    temp = data['main']['temp']
                    desp = data['weather'] [0] ['description']
                    temp = round((temp-32) * 5/9)
                    print(weather)
                    print('temperature :{} degree celcius'.format(temp))
                    print('weather is {}'.format(desp))
                    speak('temperature:{} degree celcius'.format(temp))
                    speak('weather is {}'.format(desp))

                elif 'screenshot' in query:
                    screenshot()

                elif 'offline' in query:
                    quit()

                elif "contact" in query:
                    speak("Whose contact details do you want?") 

                elif 'cpu status' in query:
                    CPUstatus()

                elif 'record my voice' in query:
                    voice_recorder()

                elif 'photo' in query:
                    speak('Taking photo! Look into the camera and smile')
                    takePicture()

                elif 'clean recycle bin' in query:
                    speak("Emptying the recycle bin")
                    winshell.recycle_bin().empty(confirm=True, show_progress=True, sound=False)

                elif 'help' in query:
                    help()
                    

        

                # elif 'camera' in query:
                #     camera()       

                
