import pyAudioAnalysis
import madmom
import matplotlib.pyplot as plt
import numpy as np 
import scipy
import librosa
import librosa.display
import wave
import io
from pydub import AudioSegment
import pylab
from scipy.io import wavfile
import pydub
import os
import json








def MP32WAV(mp3_path,wav_path):
    """
    这是MP3文件转化成WAV文件的函数
    :param mp3_path: MP3文件的地址
    :param wav_path: WAV文件的地址
    """
    pydub.AudioSegment.converter = "C:\\Users\\wangz\\.conda\envs\\audio\\Library\\bin\\ffmpeg.exe"            #说明ffmpeg的地址
    MP3_File = AudioSegment.from_mp3(file=mp3_path)
    MP3_File.export(wav_path,format="wav")

def Read_WAV(wav_path):
    """
    这是读取wav文件的函数，音频数据是单通道的。返回json
    :param wav_path: WAV文件的地址
    """
    wav_file = wave.open(wav_path,'r')
    numchannel = wav_file.getnchannels()          # 声道数
    samplewidth = wav_file.getsampwidth()      # 量化位数
    framerate = wav_file.getframerate()        # 采样频率
    numframes = wav_file.getnframes()           # 采样点数
    print("channel", numchannel)
    print("sample_width", samplewidth)
    print("framerate", framerate)
    print("numframes", numframes)
    Wav_Data = wav_file.readframes(numframes)
    Wav_Data = np.fromstring(Wav_Data,dtype=np.int16)
    Wav_Data = Wav_Data*1.0/(max(abs(Wav_Data)))        #对数据进行归一化
    # 生成音频数据,ndarray不能进行json化，必须转化为list，生成JSON
    dict = {"channel":numchannel,
            "samplewidth":samplewidth,
            "framerate":framerate,
            "numframes":numframes,
            "WaveData":list(Wav_Data)}
    return json.dumps(dict)

def DrawSpectrum(wav_data,framerate):
    """
    这是画音频的频谱函数
    :param wav_data: 音频数据
    :param framerate: 采样频率
    """
    Time = np.linspace(0,len(wav_data)/framerate*1.0,num=len(wav_data))
    plt.figure(1)
    plt.plot(Time,wav_data)
    plt.grid(True)
    plt.show()
    plt.figure(2)
    Pxx, freqs, bins, im = plt.specgram(wav_data,NFFT=1024,Fs = 16000,noverlap=900)
    plt.show()
    print(Pxx)
    print(freqs)
    print(bins)
    print(im)

def run_main():
    """
        这是主函数
    """
    # MP3文件和WAV文件的地址
    path1 = 'D:/audiosource'
    path2 = "D:/audiosource"
    paths = os.listdir(path1)
    mp3_paths = []
    # 获取mp3文件的相对地址
    for mp3_path in paths:
        mp3_paths.append(path1+"/"+mp3_path)
    print(mp3_paths)

    # 得到MP3文件对应的WAV文件的相对地址
    wav_paths = []
    for mp3_path in mp3_paths:
       wav_path = path2+"/"+mp3_path[1:].split('.')[0].split('/')[-1]+'.wav'
       wav_paths.append(wav_path)
    print(wav_paths)

    # 将MP3文件转化成WAV文件
    for(mp3_path,wav_path) in zip(mp3_paths,wav_paths):
        MP32WAV(mp3_path,wav_path)
    for wav_path in wav_paths:
        Read_WAV(wav_path)

    # 开始对音频文件进行数据化
    for wav_path in wav_paths:
        wav_json = Read_WAV(wav_path)
        print(wav_json)
        wav = json.loads(wav_json)
        wav_data = np.array(wav['WaveData'])
        framerate = int(wav['framerate'])
        DrawSpectrum(wav_data,framerate)

if __name__ == '__main__':
    run_main()