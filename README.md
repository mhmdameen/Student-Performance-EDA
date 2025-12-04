Student Performance – Exploratory Data Analysis (EDA)

This project performs an end-to-end Exploratory Data Analysis (EDA) on the Student Performance dataset, focusing on academic trends, score behavior, demographic influence, and key factors affecting student outcomes.
It includes problem definition, data cleaning, preprocessing, visual analysis, insights, and final conclusions.

Project Structure
Student-Performance-EDA/
│
├── README.md                 <-- You are here
│
├── REPORTS/                  <-- Colab notebook with markdown cells
│
├── data/
│   ├── raw/                  <-- Original dataset
│   └── cleaned/              <-- student_cleaned.csv
│
├── notebooks/                <-- Colab notebook
│
├── scripts/                  <-- cleaning.py and helper scripts

Project Objectives

This project aims to:

Understand patterns in student academic performance

Analyze distributions of math, reading, and writing scores

Examine demographic and socio-economic factors affecting performance

Identify meaningful correlations between major score components

Provide insights useful for educators and academic decision-makers

Phase 1 — Problem Definition and Dataset Selection
Problem Statement

Student academic performance is influenced by a combination of personal, demographic, and socio-economic factors. Understanding these patterns helps:

Improve student learning outcomes

Identify performance gaps

Design targeted interventions

Support informed academic planning

Dataset Details

Source: Public Student Performance Dataset

Size: Approximately 1,000 records

Type: Mixed data (categorical and numerical)

Key columns include: gender, parental education, lunch type, test preparation status, math score, reading score, and writing score.

Phase 2 — Data Cleaning and Pre-processing

The dataset underwent the following cleaning steps:

Duplicate Removal

Removed duplicate entries to ensure data integrity.

Missing Value Treatment

Handled missing scores and categorical values using appropriate imputation strategies.

Format Corrections

Standardized column names

Converted score columns to numeric

Cleaned categorical labels

Removal of Irrelevant Columns

Dropped columns not contributing to EDA.

Feature Engineering

New helpful features were created:

Average Score

Performance Category

Output

The cleaned dataset is saved at:

/data/cleaned/student_perfomance_cleaned.csv

Phase 3 — Exploratory Data Analysis (EDA)

Univariate, bivariate, and multivariate analyses were performed.

Univariate Analysis

Distribution of math, reading, and writing scores

Gender distribution

Parental education levels

Lunch type distribution

Test preparation status

Bivariate Analysis

Gender vs Score

Lunch type vs Academic performance

Test preparation vs Scores

Parental education vs Performance

Multivariate Analysis

Correlation heatmap between all three scores

Combined effect of socioeconomic variables on overall performance

Visualizations Created

More than 10 plots generated using:

Matplotlib

Seaborn

Key Insights
Academic Insights

Reading and writing scores have a strong positive correlation.

Students who completed test preparation show significantly higher performance.

Standard lunch type is associated with comparatively lower scores.

Demographic Insights

Students with parents who completed higher education tend to perform better.

Gender differences exist but do not strongly impact overall academic performance.

Performance Behavior

Most students fall within the mid-performance range (60–80).

High performers often overlap with those who completed test preparation.


Conclusion

This project demonstrates a complete EDA workflow:

Clear problem framing

Professional-level data cleaning

Comprehensive exploratory analysis

Actionable insights relevant to educators and analysts

It highlights strong skills in Python, pandas, visualization, and data interpretation. The project is suitable for academic use, resumes, and GitHub showcases.

How to Use This Project

Clone the repository:

git clone https://github.com/mhmdameen/Student-Performance-EDA.git


Install requirements:

pip install -r requirements.txt


Open the notebooks in:

/notebooks/

Author

mohammed ameen a m
GitHub: https://github.com/mhmdameen
