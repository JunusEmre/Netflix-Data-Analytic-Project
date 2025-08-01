# Netflix Data Exploration Project

A data science analysis of a Netflix dataset using Python, with insights extracted via visualizations and a custom content-based recommender system.

## Project Overview

This project explores patterns in Netflix's content — uncovering genre distributions, cast frequencies, release year trends, and regional contributions. It also includes a recommender system that suggests similar shows based on textual similarity from genre and description.

## Files Included

| File | Description |
|------|-------------|
| `Netflix.csv` | Original dataset |
| `Netflix_Analysis.ipynb` | Jupyter notebook with full visualizations and analysis |
| `dashboard_app.py` | Streamlit app for interactive genre/country filtering |
| `presentation.pdf` | High-level summary for general audiences |
| `README.md` | Project documentation (you’re reading it!) |

## Visualizations Included

- Distribution of content types (Movies vs TV Shows)
- Release year trends
- Top Producing Countries
- Most Common Ratings
- Popular Categories / Genres
- TV Show Duration Analysis
- Actor appearance frequency
- Genre-based word cloud

## Recommender System

A content-based model using TF-IDF vectorization of genre + description to suggest similar titles to any chosen one.

Example:
```python
recommend("Kota Factory")


### Dashboard App

Welcome to my interactive dashboard built with Streamlit!  
Explore data insights and visualizations in real time.

**[Launch the App](https://dashboardapppy-uejcdhsrqjfpyphazuzu2v.streamlit.app/)**


#### Tech Stack
- Python
- Streamlit
- Pandas / Plotly / [add any other libraries you used]

#### Features
- Interactive charts
- Real-time data filtering
- Clean and responsive UI


## Requirements

This project uses the following Python packages:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- xgboost
- lightgbm
- tensorflow
- keras
- statsmodels
- plotly
- streamlit
- joblib
- openpyxl


Feel free to fork, explore, and reach out with feedback!
