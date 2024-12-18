import tensorflow as tf
import numpy as np
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input

def extract_image_features(image_name):
    # 사전 훈련된 InceptionV3 모델 로드
    model = InceptionV3(weights='imagenet', include_top=False, pooling='avg')
    
    # 이미지 로드 및 전처리
    img = image.load_img(image_name, target_size=(299, 299))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    
    # 모델을 사용하여 특징 추출
    features = model.predict(img_array)
    
    print(f"Extracted features: {features.shape}")
    
    return features

# 함수 호출
features = extract_image_features("ai-generated-8513489.jpg")
