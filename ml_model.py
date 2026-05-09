import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# 데이터 불러오기
data = pd.read_csv("data.csv")

# 머신러닝 모델에 넣을 데이터
X = data[["temperature"]]

# IsolationForest 모델 생성
model = IsolationForest(contamination=0.2, random_state=42)

# 모델 학습 및 예측
data["ml_result"] = model.fit_predict(X)

# -1이면 이상값, 1이면 정상
ml_anomaly = data[data["ml_result"] == -1]

# 기존 threshold 방식 결과
threshold_anomaly = data[data["status"] == "ANOMALY"]

# 결과 출력
print("===== ML 기반 이상 탐지 결과 =====")
print(f"전체 데이터 수: {len(data)}")
print(f"ML 이상 데이터 수: {len(ml_anomaly)}")
print(f"ML 이상 비율: {(len(ml_anomaly) / len(data)) * 100:.2f}%")

print("\n===== 기존 방식과 비교 =====")
print(f"Threshold 기준 이상 데이터 수: {len(threshold_anomaly)}")
print(f"ML 기준 이상 데이터 수: {len(ml_anomaly)}")

print("\n===== 결과 해석 =====")
if len(ml_anomaly) > len(threshold_anomaly):
    print("ML 모델이 기존 threshold 방식보다 더 많은 이상 데이터를 탐지했습니다.")
elif len(ml_anomaly) < len(threshold_anomaly):
    print("ML 모델이 기존 threshold 방식보다 더 엄격하게 이상 데이터를 판단했습니다.")
else:
    print("ML 모델과 threshold 방식이 비슷한 수의 이상 데이터를 탐지했습니다.")

# 그래프 생성
plt.figure()
plt.plot(data["temperature"], label="Temperature")

plt.scatter(
    threshold_anomaly.index,
    threshold_anomaly["temperature"],
    label="Threshold Anomaly"
)

plt.scatter(
    ml_anomaly.index,
    ml_anomaly["temperature"],
    label="ML Anomaly"
)

plt.title("ML-based Temperature Anomaly Detection")
plt.xlabel("Index")
plt.ylabel("Temperature")
plt.legend()

plt.savefig("static/ml_anoamly_graph.png")
print("\nml_anomaly_graph.png saved")