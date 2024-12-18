# 데이터 정의
data = [
    ["홍길동", 85, 90, 80],
    ["김철수", 70, 88, 95],
    ["이영희", 98, 92, 88],
    ["박민수", 64, 72, 78],
]

# 총점과 평균 계산
def calculate_totals_and_averages(data):
    results = []
    for student in data:
        name = student[0]
        scores = student[1:]
        total = sum(scores)
        average = total / len(scores)
        results.append((name, total, average))
    return results

# 최고 점수 학생 찾기
def find_top_student(results):
    top_student = max(results, key=lambda x: x[1])  # 총점 기준으로 최대값 찾기
    return top_student

# 분석 실행
results = calculate_totals_and_averages(data)

print("학생별 총점과 평균:")
for name, total, average in results:
    print(f"{name}: 총점 = {total}, 평균 = {average:.2f}")

top_student = find_top_student(results)
print("\n최고 점수 학생:")
print(f"{top_student[0]}: 총점 = {top_student[1]}, 평균 = {top_student[2]:.2f}")

