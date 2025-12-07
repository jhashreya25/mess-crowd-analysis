# mess-crowd-analysis
Mess Hall Crowd Analytics — Data-driven Forecasting (Python)

This project analyzes weekly mess hall crowd fluctuations using a multi-factor dataset.
The goal is to discover patterns, identify influencing variables, visualize insights, and build a predictive model to better manage unpredictable rushes.

The problem is based on a simulation dataset containing metrics such as holidays, temperature, menu score, event intensity, and academic stress.

- Objectives

Understand weekly crowd variations

Identify key factors influencing crowd size

Perform EDA and visualize trends

Build a predictive model

Suggest actionable recommendations for better mess management

-Dataset Description

The dataset includes the following columns:

Column	Meaning
Mess_ID	Unique mess identifier
Date	Week start date
Weekly_Crowd	Number of dinners served per week
Is_Holiday	Whether week included a holiday (0/1)
Temperature	Avg temperature (°F)
Menu_Score	Menu popularity score
Event_Intensity_Index	Strength of campus events
Stress_Level	Academic stress index

(As defined in the problem PDF) 

- Project Structure
notebook/
    mess_crowd_analysis.ipynb

data/
    dataset.csv

report/
    analysis_report.pdf
    key_graphs/

video/
    explanation_video_link.txt

README.md
requirements.txt

 -Approach
 1. Data Cleaning

Standardized date format

Checked for missing values

Normalized numerical columns

- 2. Exploratory Data Analysis (EDA)

Week-on-week changes

Correlation heatmap

Trends in temperature vs crowd

Impact of holidays, events, and academic stress

- 3. Insights

Key observations include:

Strong positive correlation between menu score and crowd

Weeks with events or holidays show higher attendance

Crowds dip in weeks with extreme weather

Academic stress impacts mess usage

-4. Predictive Modeling

Built a Regression Model (or Random Forest — whichever you implemented) to predict weekly crowd based on features.

Evaluated using:

RMSE

R² score

 5. Recommendations

Examples (you should fine-tune):

Improve menu on expected low-crowd weeks

Utilize event-heavy weeks for promotions

Increase staffing in holiday/event weeks

Temperature-based planning for outdoor/indoor dining

- Visualizations

The notebook includes:

Line trends

Heatmaps

Scatterplots

Feature importance

Seasonal patterns

Prediction vs Actual graph

Graphs are saved in /report/key_graphs/.

- Explanation Video

The explanation video is available here:

(Your link inside the .txt file)

- Tech Stack

Python

Pandas

NumPy

Matplotlib / Seaborn

Scikit-Learn

Jupyter Notebook

- How to Run
pip install -r requirements.txt


Open Jupyter Notebook:

jupyter notebook


Run mess_crowd_analysis.ipynb.

