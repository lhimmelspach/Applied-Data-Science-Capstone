# Applied Data Science Capstone: SpaceX Falcon 9 Landing Prediction

This project was completed as part of my master's program capstone. It demonstrates an end-to-end data science workflow using public SpaceX launch information to predict whether a Falcon 9 first-stage booster would successfully land.

## Portfolio Summary

I built a machine learning workflow for predicting landing success using public launch data and mission features. The project includes data collection, cleaning, feature engineering, exploratory analysis, model comparison, and evaluation. It also includes a dashboard and SQL-style analysis to explore key drivers such as launch site, booster version, payload characteristics, and mission profile.

This project is a strong example of my ability to:

- collect and clean real-world data
- perform exploratory data analysis
- engineer model-ready features
- compare multiple classification models
- evaluate performance with cross-validation and test metrics
- communicate results through visualizations and dashboards

## Academic Context and Attribution

This project was completed in the context of a graduate capstone course and includes course-provided instructional materials, assignment structure, and original attribution required by the academic program. The repository preserves the original academic context while highlighting the work completed as part of this project.

My focus within this capstone included:

- preparing and organizing the data
- exploring relationships among mission variables
- testing multiple classification models
- tuning hyperparameters with cross-validation
- evaluating results and summarizing key findings
- documenting the workflow and project conclusions

## Problem Statement

SpaceX advertises Falcon 9 launches at significantly lower cost than many competitors, largely because of its focus on first-stage reusability. The goal of the project was to predict whether a Falcon 9 first stage would successfully land using mission features available before launch.

This is a realistic classification problem with practical implications for operations, launch planning, and understanding the relationship between mission characteristics and booster recovery success.

## Data and Methods

### Data Sources

- Public SpaceX launch data
- Supplemental mission data gathered from public web sources

### Target Variable

- Landing outcome: success or failure

### Methods Used

- Data cleaning and preprocessing
- Exploratory data analysis (EDA)
- Feature engineering
- Model comparison across several classifiers
- Cross-validation and test-set evaluation
- SQL-style analysis for launch insights
- Visualization and dashboarding

## Results

The notebook and project summary report results for the following models:

| Model | Cross-Validation Accuracy | Test Accuracy |
|---|---:|---:|
| Logistic Regression | 84.64% | 83.33% |
| Support Vector Machine (SVM) | 84.82% | 83.33% |
| Decision Tree | Not clearly reported in the notebook output | 83.33% |
| K-Nearest Neighbors (KNN) | 84.82% | 83.33% |

The project notebooks report that all four models achieved approximately 83.33% test accuracy on this dataset. Cross-validation accuracy was approximately 84.6% to 84.8%, depending on the model. These are promising results for a small dataset and demonstrate a workable predictive workflow, although the test set is limited in size.

### Key Findings

From the project analysis and summary document:

- Launch site had a measurable relationship with landing success.
- Booster version and engineering improvements appeared to influence reliability.
- Payload mass affected landing outcomes, with heavier payloads generally corresponding to lower success rates.
- Mission characteristics such as orbit type and launch profile were useful predictors.

## Technical Stack

- Python
- pandas
- NumPy
- scikit-learn
- matplotlib
- seaborn
- Plotly
- SQL
- Jupyter Notebook
- Dash

## Repository Structure

```text
Applied-Data-Science-Capstone/
├── README.md
├── RESULTS.md
├── SpaceX_Machine Learning Prediction.ipynb
├── dataset_part_1.csv
├── dataset_part__3.csv
├── spacex_launch_dash.csv
├── spacex-dash-app.py
├── requirements.txt
├── DATA_DICTIONARY.md
├── 기타 course-related notebooks / academic files
├── data/
├── notebooks/
├── src/
├── reports/
├── docs/
└── .gitignore
```

> Note: Some files in this repository retain the original course assignment structure and attribution because this project was completed as part of a graduate capstone. The README is written as a portfolio-facing overview of the project and my work.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/lhimmelspach/Applied-Data-Science-Capstone.git
   cd Applied-Data-Science-Capstone
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Open the notebooks in Jupyter:
   ```bash
   jupyter notebook
   ```

5. Run the workflow in order from data collection through model evaluation.

## Limitations

- The dataset is small relative to many real-world machine learning projects.
- Public data sources may contain missing or incomplete information.
- The project does not yet capture many operational variables that may affect launch outcomes.
- A larger and more time-aware validation setup would improve the reliability of the results.

## Future Improvements

- Add a more robust time-aware validation strategy
- Compare more advanced models and ensemble approaches
- Include model explainability and feature importance summaries
- Streamline the repository structure for clearer portfolio presentation
- Add a more polished dashboard or deployment-ready interface

## Conclusion

This capstone project demonstrates a solid end-to-end data science workflow and is a useful portfolio project for a junior data science or analytics role. It shows that I can work with real-world data, apply machine learning, compare models, and communicate findings in a structured way.

## Author

Luke Himmelspach

GitHub: https://github.com/lhimmelspach

---

This repository includes course-related materials and academic attribution because it was completed as part of a master's capstone assignment. It remains preserved as a record of the original academic project while also serving as a portfolio example of my analytical and modeling work.
