# SpaceX Falcon 9 First-Stage Landing Prediction

> **Academic provenance:** This repository preserves an **IBM Applied Data Science Capstone** completed by **Luke Himmelspach** through the **University of Colorado Boulder MS-DS program**. It is presented here as a portfolio project, but the original course structure, instructional prompts, and public-data attribution are intentionally retained where appropriate.

## Executive Summary

This project studies whether a **SpaceX Falcon 9 first-stage booster** will land successfully after launch using publicly available mission data. It combines:

- public-data collection and web scraping
- data cleaning and SQL-style exploratory analysis
- classification modeling in scikit-learn
- visual storytelling in notebooks
- an interactive Dash dashboard for launch-site and payload filtering

For hiring managers, the strongest signal is breadth: this capstone demonstrates an end-to-end analytical workflow rather than a single model notebook.

## Why the Problem Matters

Falcon 9's cost advantage depends heavily on **booster reusability**. If the first stage lands successfully, SpaceX can refurbish and reuse it, reducing marginal launch cost and turnaround time. Predicting landing success is therefore a useful framing exercise for understanding how launch site, mission profile, payload mass, and booster history relate to recovery outcomes.

## Individual Contribution vs. Course Scaffolding

### Course / program scaffolding preserved in the repository
- IBM capstone notebook prompts, assignment flow, and instructional text
- IBM-hosted copies of public datasets used in several notebooks
- educational dashboard structure and some course-generated file names

### Luke Himmelspach's analytical work highlighted here
- completing and interpreting the data-wrangling, EDA, SQL, mapping, and modeling labs
- comparing multiple classification models with hyperparameter search
- documenting the workflow, assumptions, and results for portfolio review
- refining the repository narrative and dashboard so the project is understandable outside the classroom

## Project Question

**Can pre-launch mission attributes help predict whether a Falcon 9 first stage will land successfully?**

### Target definition
The modeling notebooks use the binary target `Class`:
- `1` = successful booster landing
- `0` = unsuccessful landing or no successful recovery

This is **not** the same as overall payload deployment success.

## Data Sources, Provenance, and Redistribution Notes

| Source | Used in | Provenance notes |
|---|---|---|
| Wikipedia: *List of Falcon 9 and Falcon Heavy launches* | `jupyter-labs-webscraping.ipynb` | Scraped from a pinned historical page revision for reproducibility. |
| Public SpaceX launch data distributed through IBM course assets | wrangling, EDA, modeling notebooks | The notebooks load IBM-hosted CSV snapshots derived from public launch information. |
| `spacex_launch_dash.csv` | Dash app | Course-provided dashboard dataset snapshot included in the repo for local app use. |
| `dataset_part_1.csv` and `dataset_part__3.csv` | reference snapshots in repo | Tracked educational data snapshots used to document the workflow and feature schema. |

### Dataset size
- `dataset_part_1.csv`: 94 tracked rows x 17 columns in the repository
- `dataset_part__3.csv`: 90 tracked rows x 80 engineered feature columns in the repository
- Modeling notebook test split: **18 launches** (20% of 90 rows), based on notebook output
- Dashboard CSV: 56 rows x 7 columns

### Attribution and redistribution caveat
These files are preserved for **educational and portfolio review purposes**. Public launch information remains attributable to its original sources, and IBM course materials remain attributable to the IBM Applied Data Science Capstone. If you reuse the data or notebooks, cite the original public-data sources and respect their terms.

## Actual Repository Structure

```text
Applied-Data-Science-Capstone/
├── README.md
├── PORTFOLIO_SUMMARY.md
├── RESULTS.md
├── DATA_DICTIONARY.md
├── requirements.txt
├── SpaceX_Machine Learning Prediction.ipynb
├── jupyter-labs-webscraping.ipynb
├── labs-jupyter-spacex-Data wrangling.ipynb
├── jupyter-labs-eda-sql-coursera_sqllite.ipynb
├── edadataviz.ipynb
├── lab_jupyter_launch_site_location.ipynb
├── spacex-dash-app.py
├── spacex_launch_dash.csv
├── dataset_part_1.csv
├── dataset_part__3.csv
├── lhimmelspach/Applied-Data-Science-Capstone
└── .gitignore
```

The repository is intentionally flat because it reflects an academic capstone submission rather than a production package layout.

## Workflow and Notebook Order

1. **`jupyter-labs-webscraping.ipynb`** - scrapes launch-history information from Wikipedia.
2. **`labs-jupyter-spacex-Data wrangling.ipynb`** - loads SpaceX launch records, cleans fields, and derives the `Class` target.
3. **`jupyter-labs-eda-sql-coursera_sqllite.ipynb`** - loads launch data into SQLite for query-based analysis.
4. **`edadataviz.ipynb`** - explores relationships among flight number, payload, orbit, launch site, and landing success.
5. **`lab_jupyter_launch_site_location.ipynb`** - maps launch sites with Folium.
6. **`SpaceX_Machine Learning Prediction.ipynb`** - compares logistic regression, SVM, decision tree, and KNN classifiers.

## Methodology

### Feature set used in the modeling notebook
The modeling notebook loads an already engineered feature matrix with numeric and one-hot encoded columns such as:
- `FlightNumber`
- `PayloadMass`
- `Flights`
- `Block`
- `ReusedCount`
- orbit indicators (for example `Orbit_GTO`, `Orbit_ISS`, `Orbit_LEO`)
- launch-site indicators
- landing-pad indicators
- booster serial indicators
- grid-fin and landing-leg flags

### Validation approach used in the original notebook
- random 80/20 train-test split with `random_state=2`
- 10-fold cross-validation inside `GridSearchCV`
- feature standardization with `StandardScaler`

## Results (with methodological caution)

The notebook output reports the following model-selection and test results on the 90-row feature matrix:

| Model | Best CV accuracy in notebook | Test accuracy in notebook |
|---|---:|---:|
| Logistic Regression | 84.64% | 83.33% |
| SVM | 84.82% | 83.33% |
| Decision Tree | 87.50% | 83.33% |
| KNN | 84.82% | 83.33% |

### How to interpret those numbers responsibly
- The test set contains only **18 launches**, so **one prediction changes accuracy by about 5.6 percentage points**.
- The notebook standardizes the full feature matrix **before** train/test splitting, which introduces preprocessing leakage and can make performance look slightly better than a strictly out-of-sample workflow.
- The split is random rather than chronological, so it is not a strong proxy for predicting future launches over time.
- Some high-signal features (for example booster serial and reuse-related indicators) may encode mission history in ways that are useful for retrospective classification but harder to operationalize in a forward-looking decision system.

**Bottom line:** the reported ~83% accuracy is appropriate to present as an educational capstone result, not as proof of production-ready launch-risk prediction.

## Key Findings Supported by the Notebooks

Across the EDA and modeling workflow, the project consistently suggests that:
- landing outcomes improve over time as Falcon 9 operations mature
- payload mass and orbit profile are related to recovery difficulty
- launch site is associated with different landing-success patterns
- reuse-related mission context is informative for classification

These are reasonable analytical findings from the notebooks, but the small sample size means they should be treated as directional rather than definitive.

## Dash Dashboard

`spacex-dash-app.py` provides an interactive view of launch outcomes by:
- launch site selection
- payload-range filtering
- launch success distribution
- payload mass vs. landing outcome

### Run locally
```bash
python spacex-dash-app.py
```

The app expects this file in the repository root:

```text
spacex_launch_dash.csv
```

## Setup

```bash
git clone https://github.com/lhimmelspach/Applied-Data-Science-Capstone.git
cd Applied-Data-Science-Capstone
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

## Limitations

- Small dataset relative to typical ML production settings
- Original notebook workflow relies on IBM-hosted external CSV snapshots for several steps
- Random splitting and pre-split scaling make the reported metrics optimistic for future-launch prediction
- External drivers such as weather, booster inspection details, and sea-state conditions are not modeled
- This repository is an educational capstone artifact, not a deployment package

## Future Work

- rebuild the modeling workflow with chronological validation and train-fold-only preprocessing
- compare the classroom models against stronger tabular baselines
- replace one-hot booster serial indicators with more operationally interpretable engineered features
- save reproducible figures and cleaned intermediate datasets with explicit provenance metadata
- package the analysis into a cleaner reproducible pipeline if the project is revisited outside the course context

## Educational Status

This repository should be read as a **graduate capstone and portfolio artifact**, not as a production launch-risk system. It demonstrates applied data science process, communication, and modeling judgment, but it should not be used to make real launch, safety, or pricing decisions.

## Author

**Luke Himmelspach**  
GitHub: https://github.com/lhimmelspach
