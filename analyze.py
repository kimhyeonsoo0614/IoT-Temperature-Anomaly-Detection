import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

# 1. threshold/status 기반 이상 데이터
anomaly = data[data["status"] == "ANOMALY"]

# 2. 통계 기반 이상 데이터
mean_temp = data["temperature"].mean()
std_temp = data["temperature"].std()
upper = mean_temp + 2 * std_temp
lower = mean_temp - 2 * std_temp

stat_anomaly = data[
    (data["temperature"] > upper) |
    (data["temperature"] < lower)
]

# 3. 결과 요약
total = len(data)
anomaly_count = len(anomaly)
stat_anomaly_count = len(stat_anomaly)

ratio = (anomaly_count / total) * 100
stat_ratio = (stat_anomaly_count / total) * 100

max_temp = data["temperature"].max()
min_temp = data["temperature"].min()

print("===== 결과 요약 =====")
print(f"총 데이터 수: {total}")
print(f"이상 데이터 수 (threshold/status 기준): {anomaly_count}")
print(f"이상 데이터 수 (통계 기준): {stat_anomaly_count}")
print(f"이상 비율 (threshold/status 기준): {ratio:.2f}%")
print(f"이상 비율 (통계 기준): {stat_ratio:.2f}%")
print(f"평균 온도: {mean_temp:.2f}°C")
print(f"최고 온도: {max_temp:.2f}°C")
print(f"최저 온도: {min_temp:.2f}°C")

print("\n===== 결과 해석 =====")
if ratio > 20:
    print("threshold 기준으로 이상 온도 비율이 높습니다. 냉각 시스템 점검이 필요합니다.")
elif ratio > 10:
    print("threshold 기준으로 일부 이상 온도가 발생했습니다. 지속적인 모니터링이 필요합니다.")
else:
    print("threshold 기준으로 전체적으로 안정적인 상태입니다.")

if stat_anomaly_count > 0:
    print("통계 기준에서도 평균 범위를 벗어난 데이터가 확인되었습니다.")
else:
    print("통계 기준에서는 큰 이상 패턴이 확인되지 않았습니다.")

# 4. 그래프 저장
plt.figure()
plt.plot(data["temperature"], label="Temperature")

plt.scatter(
    anomaly.index,
    anomaly["temperature"],
    label="Threshold Anomaly"
)

plt.scatter(
    stat_anomaly.index,
    stat_anomaly["temperature"],
    label="Statistical Anomaly"
)

plt.title("Temperature Anomaly Detection")
plt.xlabel("Index")
plt.ylabel("Temperature")
plt.legend()

plt.savefig("static/anomaly_graph.png")
print("\nanomaly_graph.png saved")
