# Band Gap Prediction and Material Classification Using Materials Informatics

## Overview
This project explores the use of machine learning to predict the electronic band gap of crystalline materials using data from the Materials Project.
It focuses on predicting the band gap of materials and classifying them into:

- Conductors
- Semiconductors
- Insulators

using Machine Learning techniques.
The dataset was collected using the Materials Project API and processed using Python.
The primary goal of the project was to explore the relationship between material descriptors and electronic
properties

## Dataset
- Source: Materials Project
- Classes: Conductors, Semiconductors, Insulators
- Features:
  - density_atomic
  - efermi
  - is_magnetic

## Model Development
Two approaches were explored:
1. Linear Regression
Used for
Band gap prediction
2. Logistic Regression
Used for
Material classification
## Methodology
- Data extraction using mp-api
- Feature preprocessing and encoding
- Linear regression model
- Train-test split and evaluation

## Results
The linear regression model achieves reasonable predictive performance and offers interpretability through learned coefficients.

## Tools Used
- Python
- pymatgen / mp-api
- scikit-learn
- pandas, numpy, matplotlib

## Future Work
- PCA / PLS regression
- Nonlinear models
- Experimental validation
