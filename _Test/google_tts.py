from gtts import gTTS #pip install gTTs
import playsound #pip install playsound
#language code : http://www.lingoes.net/en/translator/langcode.htm

def speak_ko():
    txt = "안녕하세요! 반갑습니다!"
    tts_kr = gTTS(text=txt, lang='ko', slow=False)
    tts_kr.save("voice.mp3")
    playsound.playsound("voice.mp3")

def speak_en():
    txt = "hello! nice to meet you!"
    tts_kr = gTTS(text=txt, lang='en', slow=False)
    tts_kr.save("voice.mp3")
    playsound.playsound("voice.mp3")

def speak_ja():
    txt = "こんにちは！お会いできて嬉しいです！"
    tts_kr = gTTS(text=txt, lang='ja', slow=False)
    tts_kr.save("voice.mp3")
    playsound.playsound("voice.mp3")

def speak_zh():
    txt = "你好！很高兴见到你！"
    tts_kr = gTTS(text=txt, lang='zh', slow=False)
    tts_kr.save("voice.mp3")
    playsound.playsound("voice.mp3")

if __name__ == "__main__":
    speak_ko()
    speak_en()
    speak_ja()
    speak_zh()