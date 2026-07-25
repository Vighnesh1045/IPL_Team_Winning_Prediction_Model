# 🏏 IPL Match Win Predictor

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![GitHub License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

An end-to-end Machine Learning web application and data pipeline designed to predict the win and loss probabilities of Indian Premier League (IPL) cricket matches in real-time based on live match states (runs left, balls remaining, wickets fallen, and current run rate).

---

## ⚡ Project Overview

This project analyzes historical IPL match data (spanning multiple seasons of ball-by-ball delivery records and match outcomes) to build a robust predictive model. The project features:
1. **Data Engineering & Feature Extraction:** Processing raw ball-by-ball data (`deliveries.csv`) and match summaries (`matches.csv`), computing cumulative scores, target chasing stats, current run rate (CRR), and required run rate (RRR).
2. **Machine Learning Pipeline:** Utilizing a `ColumnTransformer` with `OneHotEncoder` for categorical team and city attributes, paired with a `LogisticRegression` classification model wrapped in an scikit-learn `Pipeline`.
3. **Model Persistence:** Serializing the trained pipeline into a portable format using `pickle` (`pipe.pkl`).
4. **Interactive Web Interface:** A live, user-friendly dashboard built using **Streamlit** allowing users to dynamically input match situations and instantly calculate live win/loss percentages.

---

## 📂 Project Structure

```text
IPL-Match-Win-Predictor/
│
├── app.py                      # Streamlit interactive web application
├── ipl_model.ipynb             # Jupyter Notebook for data processing & model training
├── pipe.pkl                    # Serialized scikit-learn ML pipeline
├── matches.csv                 # Historical IPL match metadata
├── deliveries.csv              # Ball-by-ball IPL delivery records
└── README.md                   # Project documentation

```

---

## 🛠️ Tech Stack & Libraries

* **Core Language:** Python
* **Machine Learning & Pipeline:** Scikit-learn (`LogisticRegression`, `Pipeline`, `ColumnTransformer`, `OneHotEncoder`, train/test splitting, accuracy metrics)
* **Data Manipulation & Analysis:** Pandas, NumPy
* **Data Visualization:** Matplotlib (for match progression curves and analysis)
* **Web Frontend & UI:** Streamlit

---

## 🚀 Getting Started & Local Setup

To run this project and local web dashboard on your machine, follow these steps:

1. **Clone the repository:**
```bash
git clone [https://github.com/Vighnesh1045/IPL-Match-Win-Predictor.git](https://github.com/Vighnesh1045/IPL-Match-Win-Predictor.git)
cd IPL-Match-Win-Predictor

```


2. **Install required dependencies:**
Make sure you have Python installed, then install the necessary packages:
```bash
pip install streamlit pandas numpy scikit-learn matplotlib

```


3. **Verify Model File:**
Ensure `pipe.pkl` is located in the root directory (or run the `ipl_model.ipynb` notebook to regenerate the model file from your local datasets).
4. **Launch the Streamlit Web Application:**
```bash
streamlit run app.py

```


5. **Access the App:**
Streamlit will automatically launch a local server and open the web app interface in your default browser at:
`http://localhost:8501`

---

## 📊 Model Details & Pipeline Features

* **Input Features Tracked:** Batting team, bowling team, match city, target score, current score, overs completed, and wickets fallen.
* **Calculated Metrics:**
* `balls_left`: Remaining legal deliveries in the second innings.
* `runs_left`: Difference between target score and current score.
* `crr` (Current Run Rate): Scoring rate achieved up to the current over.
* `rrr` (Required Run Rate): Required scoring rate per over to chase down the target.


* **Evaluation:** Optimized pipeline using `liblinear` solver with probability estimation (`predict_proba`) to display real-time percentage breakdowns for supporters.

---

## 📫 Connect with Me

* **Portfolio:** [vighnesh1045.github.io/portfolio](https://vighnesh1045.github.io/portfolio/)
* **LinkedIn:** [linkedin.com/in/vighnesh-anant-mhatre](https://www.linkedin.com/in/vighnesh-anant-mhatre/)
* **GitHub:** [github.com/Vighnesh1045](https://www.google.com/search?q=https://github.com/Vighnesh1045)

```

```
