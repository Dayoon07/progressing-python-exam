from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# 모델과 토크나이저 로드
model_name = "gpt2"  # 기본 GPT-2 모델
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# 모델을 평가 모드로 전환 (학습하지 않음)
model.eval()

def chat_with_gpt2(user_input):
    # 사용자 입력 텍스트 토큰화
    inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")

    # 모델에 입력 텍스트를 넣어 응답 생성
    with torch.no_grad():
        outputs = model.generate(inputs, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2)

    # 응답 토큰을 텍스트로 변환
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # 응답에서 사용자 입력 부분을 제거 (중복 방지)
    response = response[len(user_input):]
    
    return response.strip()

# 테스트: 사용자 입력 받기
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    response = chat_with_gpt2(user_input)
    print(f"AI: {response}")

