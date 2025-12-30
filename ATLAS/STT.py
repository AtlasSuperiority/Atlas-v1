from vosk import Model, KaldiRecognizer
import sounddevice as sd
import json
import numpy as np
model = Model(r"C:\Users\s_dea\AppData\Local\Programs\Python\Python310\Lib\vosk\Model")
rec = KaldiRecognizer(model, 16000)

def callback(indata, frames, time, status):
    if status:
        print(status)
    data = np.array(indata, dtype=np.int16)
    if rec.AcceptWaveform(data.tobytes()):
        print(json.loads(rec.Result())["text"])
    else:
        print(json.loads(rec.PartialResult())["partial"])
with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    print("Say something...")
    while True:
        pass



