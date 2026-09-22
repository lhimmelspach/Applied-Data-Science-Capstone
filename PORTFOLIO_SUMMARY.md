# Portfolio Summary: SpaceX Falcon 9 First-Stage Landing Prediction

This repository preserves an **IBM Applied Data Science Capstone** completed by **Luke Himmelspach** through the **University of Colorado Boulder MS-DS program**. It is both an academic record and a portfolio example of end-to-end data science work on a public aerospace dataset.

## Portfolio Value

This project demonstrates that I can:
- work with imperfect public data
- move from data collection through modeling and communication
- compare multiple classification approaches
- explain technical limitations instead of overclaiming model performance
- present results in notebooks, SQL-style analysis, maps, and a dashboard

## Problem Framing

The analysis asks whether pre-launch mission attributes can help predict **Falcon 9 first-stage landing success**. That matters because landing success is central to booster reuse, which is one of the main reasons SpaceX can reduce launch costs.

## What I Contributed

Within the capstone structure, my work included:
- completing the wrangling, EDA, SQL, mapping, and modeling tasks
- interpreting relationships among payload, orbit, launch site, and landing outcome
- comparing logistic regression, SVM, decision tree, and KNN models
- documenting assumptions, caveats, and practical takeaways
- refining the repository so the project reads clearly for non-classroom audiences

## What the Repository Preserves from the Course

- IBM instructional notebook structure and prompts
- IBM-hosted dataset references used by the notebooks
- academic attribution tied to the original capstone

## Results at a Glance

The modeling notebook reports approximately:
- **84.64%** cross-validation accuracy for logistic regression
- **84.82%** cross-validation accuracy for SVM
- **87.50%** cross-validation accuracy for the tuned decision tree
- **84.82%** cross-validation accuracy for KNN
- **83.33%** test accuracy for all four models on an 18-launch test split

Those numbers should be interpreted carefully because the dataset is small, the split is random rather than chronological, and the notebook scales features before splitting.

## Why the Results Still Matter

Even with those limitations, the project is useful as a hiring artifact because it shows:
- structured exploratory analysis
- feature preparation for tabular modeling
- awareness of validation pitfalls and leakage risk
- clear communication about uncertainty

## Recommended Hiring-Manager Takeaway

This is not a production-ready launch predictor. It is a well-scoped capstone showing practical fluency with public data, notebook-based experimentation, classical machine learning, and stakeholder-oriented communication.

## Author

**Luke Himmelspach**  
GitHub: https://github.com/lhimmelspach
