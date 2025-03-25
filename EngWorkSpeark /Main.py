import os
import time
import pygame
from gtts import gTTS


def text_to_speech(word):
    tts = gTTS(word, lang="en")
    tts.save("word.mp3")


def play_audio_loop():
    pygame.mixer.init()
    pygame.mixer.music.load("word.mp3")
    pygame.mixer.music.play(-1)  # -1 表示無限循環播放


def main():
    word = input("請輸入單字: ")
    text_to_speech(word)
    play_audio_loop()

    while True:
        cmd = input("輸入 'stop' 停止播放: ")
        if cmd.lower() == "stop":
            pygame.mixer.music.stop()
            break


if __name__ == "__main__":
    main()
