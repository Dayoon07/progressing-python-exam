import speech_recognition as sr
import time

# Recognizer 객체 생성
recognizer = sr.Recognizer()

# 마이크로부터 음성 입력 받기
with sr.Microphone() as source:
    print("말하세요...")
    recognizer.adjust_for_ambient_noise(source, duration=1)  # 주변 소음 조정
    audio = recognizer.listen(source)  # 음성 듣기
    
    attempt = 0
    success = False

    while attempt < 3 and not success:  # 최대 3번까지 재시도
        try:
            # 음성을 텍스트로 변환
            # text = recognizer.recognize_google(audio, language="ko-KR")
            text = recognizer.recognize_sphinx(audio)
            print("당신이 말한 문장: " + text)
        except sr.UnknownValueError:
            print("음성을 인식할 수 없습니다.")
        except sr.RequestError:
            print("음성 인식 서비스에 문제가 발생했습니다.")
            attempt += 1
            time.sleep(2)  # 2초 대기 후 재시도
