import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
@st.cache
def load_data():
    df = pd.read_csv("data/clean_student_performance.csv")
    return df

df = load_data()

st.title("Student Performance Dashboard")
st.write("Explore the factors influencing student performance.")

## Tile 1: Pass/Fail Distribution
st.header("Pass/Fail Distribution")
pass_fail_counts = df['pass_fail'].value_counts()

fig1, ax1 = plt.subplots()
sns.barplot(x=pass_fail_counts.index, y=pass_fail_counts.values, palette="viridis", ax=ax1)
ax1.set_xlabel("Pass/Fail")
ax1.set_ylabel("Count")
ax1.set_title("Number of Students: Pass vs Fail")
st.pyplot(fig1)

## Tile 2: Study Hours vs Final Exam Score
st.header("Study Hours vs Final Exam Score")
fig2, ax2 = plt.subplots()
sns.scatterplot(data=df, x="study_hours_per_week", y="final_exam_score", hue="pass_fail", ax=ax2)
ax2.set_title("Study Hours vs Final Exam Score")
st.pyplot(fig2)
