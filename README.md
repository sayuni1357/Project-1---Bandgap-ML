# Band Gap Prediction Using Materials Informatics

## Overview
This project explores the use of machine learning to predict the electronic band gap of crystalline materials using data from the Materials Project.

## Dataset
- Source: Materials Project
- Classes: Conductors, Semiconductors, Insulators
- Features:
  - density_atomic
  - efermi
  - is_magnetic

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
