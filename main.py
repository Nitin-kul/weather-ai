import requests
import json

import datetime as d

import pyttsx3
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1])


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(d.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning,!sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon,!sir")
    else:
        speak("Good Evening,!sir")


WishMe()
speak("please enter name of city")
city = input('Name of city:')
while True:

    try:

        url = f"https://api.weatherapi.com/v1/current.json?key=03b4c4e4e88549819f0184308230110&q={city}"

        r = requests.get(url)
        wdic = json.loads(r.text)
        temp = wdic["current"]["temp_c"]
        speak(f"temperature of {city} is {temp}. also these are some information of {city}")
        print('Name of city: ', wdic["location"]["name"])
        print('Region: ', wdic["location"]["region"])
        print('country: ', wdic["location"]["country"])
        print('Localtime: ', wdic["location"]["localtime"])
        print('Last_updated: ', wdic["current"]["last_updated"])

        speak("sir, would you be like to check another city weather and information")
        q = input('y/n: ')

        if q == 'n':
            speak('thanks to come')
            break
        else:
            speak("ok then, enter city name")
            n_city = input('Name of city: ')
            city = n_city
    except Exception as e:
        speak("This type of city isn't find in my information.")
        print("Error is:", e)
        speak("please enter correct city name! or quict then")
        m_city = input('Name of city or quict(q): ')
        if m_city == 'q':
            speak('thanks to come')
            break
        else:
            city = m_city

