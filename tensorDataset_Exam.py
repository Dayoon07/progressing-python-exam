import tensorflow_datasets as tfds

# MNIST 데이터셋 로드
dataset, info = tfds.load('mnist', with_info=True)
train_data = dataset['train']
test_data = dataset['test']

# 데이터셋 확인
for example in train_data.take(1):
    image, label = example['image'], example['label']
    print(f"Label: {label}, Image shape: {image.shape}")
