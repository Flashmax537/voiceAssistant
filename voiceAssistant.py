from tkinter import *
import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)

def talk(words):
    lbl.configure(text=words)
    engine.say(words)
    engine.runAndWait()
    engine.stop()

def clicked():
    r = sr.Recognizer()

    # Начинаем прослушивать микрофон и записываем данные в source
    with sr.Microphone() as source:
        # Просто вывод, чтобы мы знали когда говорить
        lbl.configure(text="Говорите")
        # Устанавливаем паузу, чтобы прослушивание
        # началось лишь по прошествию 1 секунды
        r.pause_threshold = 1
        # используем adjust_for_ambient_noise для удаления
        # посторонних шумов из аудио дорожки
        r.adjust_for_ambient_noise(source, duration=1)
        # Полученные данные записываем в переменную audio
        # пока мы получили лишь mp3 звук
        audio = r.listen(source)

    try:
        zadanie = r.recognize_google(audio, language="ru-RU").lower()
        lbl.configure(text="Вы сказали: " + zadanie)
        talk("Вы сказали: " + zadanie)
        makeSomething(zadanie)

    except sr.UnknownValueError:
        talk("Я вас не поняла")
        zadanie = clicked()


def makeSomething(zadanie):
	if 'открыть сайт' in zadanie:
		talk("Уже открываю")
		url = 'http://myvorobev.pythonanywhere.com'
		webbrowser.open(url)
	elif 'стоп' in zadanie:
		talk("Да, конечно, без проблем")
		sys.exit()
	elif 'имя' in zadanie:
		talk("Меня зовут Сири")

window = Tk()
window.title("voiceAssistant")
window.geometry('400x100')
lbl = Label(window, text="Привет, чем я могу помочь вам?")
lbl.grid(column=0, row=0)
talk("Привет, чем я могу помочь вам?")
btn = Button(window, text="Слушать", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()