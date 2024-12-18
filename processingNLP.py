import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout

# 텍스트 데이터 (예시)
sentences = [
    '자연어 처리 모델을 학습하고 있습니다.',
    'TensorFlow는 강력한 딥러닝 프레임워크입니다.',
    '딥러닝을 배우는 것은 흥미롭습니다.',
    '한국어 자연어 처리에 도전하세요.'
]

# Tokenizer 객체 생성 및 텍스트를 정수 인덱스로 변환
tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)

# 텍스트를 시퀀스로 변환
sequences = tokenizer.texts_to_sequences(sentences)

# 시퀀스의 길이를 맞추기 위해 패딩 추가
padded_sequences = pad_sequences(sequences, padding='post')

# 출력 결과
print("단어 인덱스:", tokenizer.word_index)
print("패딩된 시퀀스:\n", padded_sequences)

# 예시 라벨 (이진 분류: 0 또는 1)
labels = np.array([1, 1, 0, 1])  # 각 문장에 대한 레이블

# 모델 구축
model = Sequential()

# 임베딩 레이어: 단어 인덱스의 크기와 임베딩 차원 설정
model.add(Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=10, input_length=padded_sequences.shape[1]))

# LSTM 레이어
model.add(LSTM(64))

# 드롭아웃 레이어 (과적합 방지)
model.add(Dropout(0.5))

# 출력 레이어
model.add(Dense(1, activation='sigmoid'))

# 모델 컴파일
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 모델 요약 출력
model.summary()

# 모델 훈련
model.fit(padded_sequences, labels, epochs=10, batch_size=2)

# 예시 새로운 텍스트
new_sentences = ['딥러닝은 재밌어요!', '이 코드는 어렵습니다.']

# 텍스트 전처리 (토큰화 및 패딩)
new_sequences = tokenizer.texts_to_sequences(new_sentences)
new_padded_sequences = pad_sequences(new_sequences, padding='post', maxlen=padded_sequences.shape[1])

# 예측
predictions = model.predict(new_padded_sequences)
print("예측 결과:", predictions)
