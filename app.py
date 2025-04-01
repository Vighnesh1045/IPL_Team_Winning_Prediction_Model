import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the trained model
pipe = pickle.load(open("pipe.pkl", "rb"))

# Title of the web app
st.title("IPL Match Win Predictor")

# Load teams and cities from dataset
teams = [
    'Sunrisers Hyderabad',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Kings XI Punjab',
    'Chennai Super Kings',
    'Rajasthan Royals',
    'Delhi Capitals'
]

cities = [
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi', 'Chandigarh',
    'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion',
    'East London', 'Johannesburg', 'Kimberley', 'Bloemfontein', 'Ahmedabad', 'Cuttack',
    'Nagpur', 'Dharamsala', 'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
    'Sharjah', 'Mohali'
]

# Input fields in Streamlit UI
batting_team = st.selectbox("Select Batting Team", teams)
bowling_team = st.selectbox("Select Bowling Team", teams)
city = st.selectbox("Match City", cities)
target = st.number_input("Target Score", min_value=1, max_value=300, step=1)
score = st.number_input("Current Score", min_value=0, max_value=300, step=1)
overs_completed = st.number_input("Overs Completed", min_value=0.0, max_value=20.0, step=0.1)
wickets_fallen = st.number_input("Wickets Fallen", min_value=0, max_value=10, step=1)

# Predict Button
if st.button("Predict Probability"):
    balls_left = 120 - (overs_completed * 6)
    runs_left = target - score
    crr = (score * 6) / (overs_completed * 6) if overs_completed > 0 else 0
    rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets': [10 - wickets_fallen],
        'total_runs_x': [target],
        'crr': [crr],
        'rrr': [rrr]
    })

    # Predict probabilities
    result = pipe.predict_proba(input_df)[0]
    loss_prob = round(result[0] * 100, 2)
    win_prob = round(result[1] * 100, 2)

    st.subheader(f"🏆 Win Probability: {win_prob}%")
    st.subheader(f"❌ Loss Probability: {loss_prob}%")
