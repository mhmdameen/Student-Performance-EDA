```md
# Student Performance – Exploratory Data Analysis (EDA)

This project performs an end-to-end Exploratory Data Analysis (EDA) on the Student Performance dataset, focusing on academic trends, score behavior, demographic influence, and key factors affecting student outcomes.  
It includes problem definition, data cleaning, preprocessing, visual exploration, insights, and final conclusions.

---

## Project Structure
```

Student-Performance-EDA/
│
├── README.md
│
├── REPORTS/                  # Colab notebook with markdown
│
├── data/
│   ├── raw/                  # Original dataset
│   └── cleaned/              # student_performance_cleaned.csv
│
├── notebooks/                # Colab notebook(s)
│
├── scripts/                  # cleaning.py and helper utilities

```

---

## Project Objectives

This project aims to:

- Understand patterns in student academic performance  
- Analyze distributions of math, reading, and writing scores  
- Examine demographic and socio-economic factors affecting performance  
- Identify correlations between major score components  
- Provide insights useful for educators and academic planners  

---

## Phase 1 — Problem Definition and Dataset Selection

### Problem Statement
Student academic performance is influenced by several demographic, personal, and socio-economic factors. Understanding these relationships helps:

- Improve student learning outcomes  
- Identify performance gaps  
- Design targeted academic interventions  
- Support informed educational decision-making  

### Dataset Details

- **Source:** Public Student Performance Dataset  
- **Size:** Approximately 1,000 student records  
- **Type:** Mixed data (categorical and numerical)  
- **Key columns include:**  
  Gender, parental education, lunch type, test preparation status, math score, reading score, writing score.

---

## Phase 2 — Data Cleaning and Pre-processing

The dataset underwent the following steps:

### Duplicate Removal  
Eliminated duplicate entries for accuracy.

### Missing Value Treatment  
Handled missing values in both categorical and numerical fields using sensible imputation or removal depending on context.

### Format Corrections  
- Standardized column names  
- Converted score fields to numeric types  
- Cleaned categorical labels  

### Removal of Irrelevant Columns  
Dropped columns not required for analysis.

### Feature Engineering  
Created additional useful columns:

- **Average Score** — mean of math, reading, and writing scores  
- **Performance Category** — categorical label based on average score (e.g., Low, Medium, High)

### Output  
The cleaned dataset is saved at:

```

/data/cleaned/student_performance_cleaned.csv

```

---

## Phase 3 — Exploratory Data Analysis (EDA)

Analyses performed include univariate, bivariate, and multivariate techniques.

### Univariate Analysis
- Score distributions (math, reading, writing)  
- Gender distribution  
- Parental education distribution  
- Lunch type distribution  
- Test preparation status distribution  

### Bivariate Analysis
- Gender vs Scores  
- Lunch type vs Performance  
- Test preparation vs Score improvement  
- Parental education vs Scores  

### Multivariate Analysis
- Correlation heatmap among all score columns  
- Combined effects of socioeconomic variables (parental education, lunch, test preparation) on overall performance  

### Visualizations  
More than 10 visualizations created using:

- Matplotlib  
- Seaborn  

---

## Key Insights

### Academic Insights
- Reading and writing scores have a strong positive correlation.  
- Students who completed test preparation show higher average scores across subjects.  
- Students with standard lunch type tend to have comparatively lower average scores.

### Demographic Insights
- Students whose parents have higher education levels generally perform better.  
- Gender-related differences are present in some score categories but are not the primary driver of overall performance.

### Performance Behavior
- Most students are in the mid-score range (approximately 60–80).  
- High-performing students frequently overlap with those who completed test preparation.

---

## Conclusion

This project demonstrates a complete exploratory data analysis workflow:

- Clear problem framing  
- Systematic data cleaning and preprocessing  
- Detailed univariate, bivariate, and multivariate analysis  
- Actionable insights for educators and analysts  

The project highlights skills in Python, pandas, Matplotlib, Seaborn, and data interpretation. It is suitable for academic evaluation, resume portfolios, and GitHub showcases.

---

## How to Use This Project

1. Clone the repository:
```

git clone [https://github.com/mhmdameen/Student-Performance-EDA.git](https://github.com/mhmdameen/Student-Performance-EDA.git)

```

2. Install requirements:
```

pip install -r requirements.txt

```

3. Open the notebooks:
All analysis steps are included in the `notebooks/` folder. Open the Colab notebook(s) or local Jupyter notebooks to run the analysis.

---

## Files of Interest

- `notebooks/student_performance_eda.ipynb` — main Colab notebook with all EDA steps and visualizations (example name; adjust to actual file)  
- `scripts/cleaning.py` — data cleaning and preprocessing utilities  
- `scripts/helpers.py` — plotting and EDA helper functions  
- `data/cleaned/student_performance_cleaned.csv` — cleaned dataset used for analysis

---

## Author

mohammed ameen a m  
GitHub: https://github.com/mhmdameen

---

## Optional additions (available on request)

- `requirements.txt` with exact package versions  
- LICENSE file (MIT, Apache-2.0, etc.)  
- Short project summary for resume or portfolio (1–2 sentences)  
- CI workflow to run basic tests or linting on notebooks and scripts

If you want any of the above added, tell me which and I will generate them.
```
