import speech_recognition as sr
from pyautogui import press


r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        audio = r.listen(source)
    texto = r. recognize_google(audio, language='pt-BR')
    print("Você disse: " + texto)
    if texto== 'aqui':
        press('z')
