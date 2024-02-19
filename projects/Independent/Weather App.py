#Weather App

import tkinter as tk
import requests
import time
import os

#api allows you to return imperial or metric measurements by adding "&units=imperial" before the appid

def InputWeather(canvas):
    city = text.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid=659d1a4d8890d1b70e2fb9de4749518c"
    JSONdata = requests.get(api).json()
    
    condition = JSONdata["weather"][0]["main"]
    temp = int(JSONdata['main']['temp'] - 273.15)
    Mintemp = int(JSONdata['main']['temp_min'] - 273.15)
    Maxtemp = int(JSONdata['main']['temp_max'] - 273.15)
    pressure = JSONdata['main']['pressure']
    humidity = JSONdata['main']['humidity']
    wspeed = JSONdata['wind']['speed']
    sr = time.strftime("%I:%M:%S", time.gmtime(JSONdata['sys']['sunrise'] -21600))
    ss = time.strftime("%I:%M:%S", time.gmtime(JSONdata['sys']['sunset'] -21600))


    fInfo = condition + "\n" + str(temp) + "°C\n"
    fData = "Maximum Temperature: " + str(Maxtemp) + "°C" + "\n" + "Minimum Temperature: " + str(Mintemp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wspeed) + "\n" + "Sunrise: " + sr + "\n" + "Sunset: " + ss
    label1.configure(text = fInfo)
    label2.configure(text = fData)
    
#GUI
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
canvas.configure(bg='grey')

#path='c:/Users/Luisa/OneDrive/Documents/Individual CS Projects'
#isFile = os.path.isfile(path)
#photo_image = tk.PhotoImage(isFile)
#tk.Label(canvas, image=path).pack()

text = tk.Entry(canvas, borderwidth = 3)
text.pack(pady = 20)
text.focus()
text.bind('<Return>', InputWeather)

label1 = tk.Label(canvas)
label1 = tk.Label(font= ("times new roman", 35, "bold"), bg='grey')
label1.configure()
label1.pack()

label2 = tk.Label(canvas)
label2 = tk.Label(font= ("times new roman", 15, "bold"), bg='grey')
label2.configure()
label2.pack()

canvas.mainloop()


