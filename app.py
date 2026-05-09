from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    data = pd.read_csv("data.csv")

    total = len(data)
    anomaly = data[data["status"] == "ANOMALY"]

    anomaly_count = len(anomaly)
    ratio = (anomaly_count / total) * 100

    mean_temp = data["temperature"].mean()
    max_temp = data["temperature"].max()

    if ratio > 20:
        result = "이상 온도 비율이 높습니다."
    elif ratio > 10:
        result = "일부 이상 발생"
    else:
        result = "정상 상태"

    return render_template(
        "index.html",
        total=total,
        anomaly_count=anomaly_count,
        ratio=f"{ratio:.2f}",
        mean_temp=f"{mean_temp:.2f}",
        max_temp=f"{max_temp:.2f}",
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)