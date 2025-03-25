你可以使用 gTTS（Google Text-to-Speech）來進行文字轉語音，並結合 pygame 播放音訊，這樣可以在本機端無限播放。

若需要「線上執行」，你可以使用 ipywidgets 搭配 IPython.display.Audio 來讓 Jupyter Notebook 播放音訊。

這裡是一個簡單的 Python 程式：

方法 1：本機端執行（適合桌面環境）
python
複製
編輯
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
這段程式會持續重複播放輸入的單字，直到使用者輸入 stop 為止。

gTTS 需要網路來合成語音，但播放過後就可以離線循環播放。

方法 2：線上 Jupyter Notebook 版本
如果你需要在 Google Colab 或 Jupyter Notebook 執行，這個版本會比較合適：

python
複製
編輯
import IPython.display as ipd
import ipywidgets as widgets
from gtts import gTTS

def speak(word):
    tts = gTTS(word, lang="en")
    tts.save("word.mp3")
    return ipd.Audio("word.mp3", autoplay=True)

word_input = widgets.Text(description="單字:")
play_button = widgets.Button(description="播放")
output = widgets.Output()

def on_play_clicked(b):
    with output:
        output.clear_output()
        display(speak(word_input.value))

play_button.on_click(on_play_clicked)

display(word_input, play_button, output)
ipywidgets 讓你可以在 Jupyter Notebook 內建立互動式按鈕來播放輸入的單字。

這樣的方式可以在 Google Colab 等線上環境執行。

如果你是要開發網頁應用，可以考慮使用 Flask 或 Gradio，這樣可以透過網頁輸入單字並播放語音。
