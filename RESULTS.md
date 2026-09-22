# Results Summary: SpaceX Falcon 9 First-Stage Landing Prediction

## Executive Summary

The modeling notebook compares four scikit-learn classifiers on a small engineered dataset of Falcon 9 launches. All four models achieve the same held-out test accuracy in the saved notebook output, but the evaluation setup has limitations that make the result **directional rather than definitive**.

## What Is Directly Supported by Notebook Output

`SpaceX_Machine Learning Prediction.ipynb` reports:

- a 90-row engineered feature matrix (`dataset_part_3.csv` in the original IBM course asset flow; a similar snapshot is tracked here as `dataset_part__3.csv`)
- an 80/20 random train-test split
- an 18-row test set
- 10-fold grid-search cross-validation for each model

### Reported model metrics

| Model | Best parameters reported in notebook | Best CV accuracy | Test accuracy |
|---|---|---:|---:|
| Logistic Regression | `C=0.01`, `penalty='l2'`, `solver='lbfgs'` | 84.64% | 83.33% |
| SVM | `C=1.0`, `gamma=0.03162277660168379`, `kernel='sigmoid'` | 84.82% | 83.33% |
| Decision Tree | `criterion='entropy'`, `max_depth=18`, `max_features='sqrt'`, `min_samples_leaf=2`, `min_samples_split=10`, `splitter='random'` | 87.50% | 83.33% |
| KNN | `algorithm='auto'`, `n_neighbors=10`, `p=1` | 84.82% | 83.33% |

## Interpretation

The identical test accuracy across all four models suggests the assignment dataset is small enough that different algorithms can land on the same result for the same 18-example test split. With a test set that small:

- each single prediction changes accuracy by about **5.6 percentage points**
- confidence intervals around 83.33% are wide
- a different random split could materially change the ranking

## Methodological Cautions

These findings should be presented honestly:

1. **Preprocessing leakage**  
   The saved notebook applies `StandardScaler().fit_transform(X)` before `train_test_split(...)`. In a stricter workflow, scaling would be fit only on each training fold.

2. **Random rather than temporal validation**  
   Launches are time ordered, but the assignment uses a random split. That is acceptable for a classroom demonstration, but weaker for forecasting future launches.

3. **Feature operationalization risk**  
   The engineered feature matrix includes booster serial indicators, landing-pad indicators, and reuse-related features. Those can be predictive, but they may not correspond cleanly to a simple pre-launch decision policy outside the educational exercise.

4. **Target scope**  
   The target is **booster landing success**, not overall mission success or launch reliability.

## Findings That Are Reasonable but Should Stay Qualitative

The EDA notebooks support a few broad takeaways without requiring over-precise business claims:
- landing success appears to improve over time
- launch site is associated with different success patterns
- payload mass and orbit type relate to recovery difficulty
- reuse context carries predictive signal

## Findings Removed or Softened from Earlier Documentation

Earlier versions of this repository made stronger claims than the evidence justified, including:
- precise site success percentages not traced to saved outputs here
- business-readiness language such as "ready for deployment"
- unsupported cost-estimation claims
- detailed confusion-matrix interpretations not verified in the saved repository artifacts

Those claims have been intentionally removed or reframed.

## Recommended Portfolio Framing

A fair summary for prospective hiring managers is:

> This capstone demonstrates an end-to-end applied data science workflow on public aerospace data and achieves roughly 83% accuracy on a small held-out set, while also revealing important limitations around dataset size, leakage risk, and temporal validation.
