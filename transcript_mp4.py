#!/usr/bin/env python3

import os
import subprocess
import sys

from vosk import Model, KaldiRecognizer, SetLogLevel


SetLogLevel(0)

if not os.path.exists("model"):
    print("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' "
          "in the current folder.")
    exit(1)

sample_rate = 16000
model = Model("model")
rec = KaldiRecognizer(model, sample_rate)

process = subprocess.Popen(
    ['ffmpeg', '-loglevel', 'quiet', '-i', sys.argv[1], '-ar', str(sample_rate), '-ac', '1', '-f', 's16le', '-'],
    stdout=subprocess.PIPE
)

while True:
    data = process.stdout.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())

print(rec.FinalResult())
