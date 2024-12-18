from gtts import gTTS
import playsound

# 텍스트 정의
text = "안녕? 지피티 버전 투. 나는 머신러닝 개발자야"
file = "text.mp3"

# TTS 객체 생성
tts = gTTS(text=text, lang='ko')

# 음성 파일 저장
tts.save(file)

playsound.playsound(file)
print(playsound.playsound(text))

