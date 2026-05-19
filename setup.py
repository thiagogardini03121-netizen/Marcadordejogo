from vosk import Model, KaldiRecognizer
import sounddevice as sd
import queue
import json
import keyboard

q = queue.Queue()

# modelo
model = Model(r'C:\Users\User\Desktop\marcadorjogo\vosk-model-small-pt-0.3')

# comandos permitidos
comandos = [
    "aqui",
    "[unk]"
]

grammar = json.dumps(comandos)

# reconhecedor
rec = KaldiRecognizer(model, 16000, grammar)

def callback(indata, frames, time, status):
    q.put(bytes(indata))

with sd.RawInputStream(
    samplerate=16000,
    blocksize=2000,
    dtype='int16',
    channels=1,
    callback=callback
):

    print("Fale 'aqui'...")

    while True:

        data = q.get()

        if rec.AcceptWaveform(data):

            result = json.loads(rec.Result())

            texto = result.get("text", "")

            if texto:

                print("Comando:", texto)

                # se falar "aqui"
                if texto == "aqui":

                    print("Tecla Z pressionada")

                    # aperta a tecla Z
                    keyboard.press_and_release("z")