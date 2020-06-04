import pyaudio
import wave
from aip import AipSpeech
import os
from xpinyin import Pinyin

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "audio.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

APP_ID = '19165946'
API_KEY = 'D7BqfDPOj9ORbG85FL5jOQjh'
SECRET_KEY = 'skL4Mag0dGquseo08RaVsDgM1ABMxGN7'
client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)

def record():
    stream.start_stream()
    print("* 开始录音......")

    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def recognize():
    with open('audio.wav', 'rb') as fp:
            wave=fp.read()

    print("* 正在识别......",len(wave))
    result = client.asr(wave, 'wav', 16000, {'dev_pid':1537})
    # print(result)
    if result["err_no"] == 0:
        for t in result["result"]:
            print(t)
            return t
    else:
        print("没有识别到语音\n",result["err_no"])


if __name__ == "__main__":
    while True:
        record()
        recognize()
