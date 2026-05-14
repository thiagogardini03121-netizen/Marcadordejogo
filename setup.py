from vosk import Model, KaldiRecognizer
import sounddevice as sd
import keyboard
import queue
import json

q = queue.Queue()

# modelo
model = Model("vosk-model-small-pt-0.3")

# reconhecimento
rec = KaldiRecognizer(model, 16000)

def callback(indata, frames, time, status):
    q.put(bytes(indata))

# microfone contínuo
with sd.RawInputStream(
    samplerate=16000,
    blocksize=8000,
    dtype='int16',
    channels=1,
    callback=callback
):

    print("Ouvindo...")

    while True:
        data = q.get()

        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())

            texto = result.get("text", "").lower()

            print("Você disse:", texto)

            # comandos
            if "pular" in texto:
                keyboard.press_and_release("space")

            elif "atacar" in texto:
                keyboard.press_and_release("f")

            elif "cura" in texto:
                keyboard.press_and_release("1")