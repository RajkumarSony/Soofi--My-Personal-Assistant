
from tools.speaker import speak
import random
import os

def play_music():
    music_dir = 'C:\\Users\\rkson\\Music\\'
    songs = os.listdir(music_dir)
    #print(songs)
    n = random.randint(1, 26)
    speak("Music is starting to play now..")
    speak('Please wait..... and enjoy!!')
    # print("Music is starting to play now..")
    try:
        os.startfile(os.path.join(music_dir, songs[n]))
    except:
        speak('Sorry, Musics file are not found...')
