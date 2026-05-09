# IOT temperature Anomaly Detection System
IOT 환경에서 온도 데이터를 생성하고, Threshold 기반 + ML 기반 이상 탐지를 수행하는 프로젝트입니다.

## 1. 프로젝트 목적
기존 단순 threshold 방식 한계를 확인하고, 머신러닝 기반 이상 탐지(Isolation Forest)와 비교하기 위해 프로젝트를 진행했습니다.
또한 Flask 기반 웹 시각화를 통해 실시간 데이터 분석 흐름을 구현했습니다
.
## 2. 프로젝트 흐름
온도 데이터 생성
->CSV 파일 저장
->Threshold 기반 이상 탐지
->통계 기반 이상 탐지
->ML 기반 이상 탐지
->그래프 시각화
->Flask 웹 서비스 출력

## 3. 사용 기술
-Python
-Pandas
-Matplotlib
-Scikit-learn
-Flask
-CSV

## 4. 주요 기능 설명
(1) 데이터 생성
-랜덤 온도 생성
-CSV 저장
-time stamp 기록
-anmaly 데이터 포함

(2) Threshold 기반 이상 탐지
온도가 특정값(28도)을 초과하면 이상 데이터로 판단했습니다.

(3) 통계 기반 탐지
평균 및 표준편차 기반으로 비정상 데이터를 탐지했습니다.

(4)ML 기반 탐지
-Isolation Forest 모델을 사용하여 비지도 학습 기반 이상 탐지를 수행했습니다.
-Threshold 방식과 달리 패턴 기반 이상 탐지가 가능하도록 구현했습니다.

(5)Flask 웹 시각화
Flask 웹 서버를 통해 분석 결과와 그래프를 시각화했습니다.

## 5. 결과 이미지
### Threshold and Statistical Anomaly Detection
![Threshold and Statistical Detection](static/anomaly_graph.png)
### ML-based Detection
![ML Detection](static/ml_anomaly_graph.png)


## 2. 프로젝트 개요
IOT 환경에서 발생할 수 있는 온도 데이터를 생성하고, 이상 온도를 탐지하는 시스템이다.



## 3. 프로젝트 흐름
1. 온도 데이터 생성
2. CSV 저장
