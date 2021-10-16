from pydub import AudioSegment
from pydub.playback import play
import os

def insert_silence(audio_file): # 在音频前后插入1秒静音
    # create 1 sec of silence audio segment
    one_sec_segment = AudioSegment.silent(duration=1000)  #duration in milliseconds
    #read wav file to an audio segment
    song = AudioSegment.from_wav(audio_file)
    #Add above two audio segments    
    final_song = one_sec_segment + song + one_sec_segment
    #Either save modified audio
    final_song.export(audio_file, format="wav")

dir = input('音频文件夹路径拖进来然后回车:')
# 路径格式是 "C:\dir1\dir2\"
for i in os.listdir(dir):
    if i.split('.')[1]=='wav':
        insert_silence(dir+i)
        print("已经在"+i+"中插入静音")