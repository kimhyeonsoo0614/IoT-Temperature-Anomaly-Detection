import random
import time
import csv
from datetime import datetime

def generate_explanation(temp):
    return f"""
[AI-style Explanation]
현재 온도: {temp:.2f}°C

가능한 원인:
- 장비 부하 증가
- 주변 온도 상승
- 냉각 장치 이상 가능성

대응 방안:
- 장비 상태 확인
- 냉각 시스템 점검
- 온도 변화 추이를 추가 모니터링
"""

threshold = 28

with open('data.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)

    writer.writerow(["time", "temperature", "status", "explanation"])

    for i in range(100):

        if random.random() < 0.8:
            temp = random.uniform(22, 26)
        else:
            temp = random.uniform(28, 32)

        now = datetime.now()

        if temp > threshold:
            status = "ANOMALY"
            print(f"WARNING! High Temp: {temp:.2f}")

            explanation = generate_explanation(temp)
            print(explanation)
        else:
            status = "NORMAL"
            explanation = ""

        writer.writerow([now, temp, status, explanation])

        time.sleep(0.01)