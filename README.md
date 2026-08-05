# Applied Data Science Capstone: SpaceX Falcon 9 Landing Prediction

End-to-end machine learning project to predict whether a SpaceX Falcon 9 first stage will successfully land, using public launch data and web-scraped mission information.

## Project Overview
This project demonstrates a full data science workflow:
- Data collection (API + web scraping)
- Data wrangling and feature engineering
- Exploratory data analysis (EDA)
- Predictive modeling and evaluation

## Problem Statement
SpaceX launch costs depend heavily on first-stage reusability.  
The goal is to build a classification model that predicts landing success from pre-launch and mission features.

## Dataset
- SpaceX launch data from public APIs
- Supplemental mission attributes gathered via web scraping
- Target variable: **Landing outcome** (success/failure)

## Tech Stack
- Python
- Pandas, NumPy
- Matplotlib / Seaborn / Plotly
- Scikit-learn
- Jupyter Notebook

## Methodology
1. Collected launch-level data from APIs and web sources  
2. Cleaned and standardized variables  
3. Performed EDA to identify relationships (payload, orbit, launch site, etc.)  
4. Engineered model-ready features  
5. Trained and compared multiple classifiers  
6. Selected best model based on validation performance

### Key Findings
- Launch site and orbit type were strong predictors of landing success.
- Certain booster generations showed improved probability of landing.
- Payload thresholds influenced model confidence.

## Repository Structure
```text
Applied-Data-Science-Capstone/
├── data/                # Raw/interim/processed data (or instructions to fetch)
├── notebooks/           # EDA and modeling notebooks
├── src/                 # Reusable Python scripts/functions
├── reports/figures/     # Plots and visuals for README/report
├── requirements.txt
└── README.md
```

## ⚙️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/lhimmelspach/Applied-Data-Science-Capstone.git
   cd Applied-Data-Science-Capstone
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Launch notebooks:
   ```bash
   jupyter lab
   ```
5. Run notebooks in order:
   - data collection
   - wrangling
   - EDA
   - modeling
   - evaluation

## Limitations
- Public data quality and missing fields can affect model reliability.
- Some external factors (weather, operational decisions) may be underrepresented.
- Potential class imbalance may impact minority-case predictions.

## Future Improvements
- Add time-aware validation split to reduce leakage risk.
- Try gradient boosting/XGBoost with hyperparameter tuning.
- Add model explainability (SHAP) for feature impact analysis.
- Package pipeline scripts for one-command retraining.
## Author
**Luke Himmelspach**  
GitHub: https://github.com/lhimmelspach
