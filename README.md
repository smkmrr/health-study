# Health Study Data Analysis

## Overview
This project implements a statistical analysis and machine learning pipeline using a health dataset. It is designed to explore relationships between health metrics (such as age, weight, and smoking habits) and cardiovascular health (systolic blood pressure).

The project uses **Object-Oriented Programming (OOP)** principles to organize analysis logic and utilizes **Linear Algebra** via `scikit-learn` for predictive modeling.

---

## Key Analysis Steps

### 1. Descriptive Analysis
* Calculation of summary statistics (Mean, Median, Min, Max) for age, weight, height, blood pressure, and cholesterol.
* Identification of hypertension prevalence.

### 2. Simulation
* Monte Carlo-style simulation to compare disease prevalence in the dataset against a simulated population of 1,000 individuals.

### 3. Statistical Inference
* **Confidence Intervals:** Calculation of the 95% confidence interval for mean systolic blood pressure using both Normal Approximation and Bootstrap methods.
* **Hypothesis Testing:** A two-sample t-test to determine if there is a statistically significant difference in blood pressure between smokers and non-smokers.
* **Power Analysis:** Simulation to determine the statistical power of the hypothesis test.

### 4. Predictive Modeling (Linear Algebra)
* **Linear Regression:** A model predicting systolic blood pressure based on Age and Weight.
* **Visualization:** Scatter plot with a regression trendline to visualize correlations.

---


## Project Structure

The code is modularized into the `src` directory:

```text
├── report.ipynb                 # Main analysis notebook
├── requirements.txt             # List of dependencies
├── .gitignore                   # Specifies files to ignore in Git
├── data/
│   └── health_study_dataset.csv # Input dataset
└── src/                         # Custom source code modules
    ├── analysis.py              # Functional statistical calculations (Part 1 logic)
    ├── health_analyzer.py       # OOP class for health analysis (Part 2 logic)
    ├── io_utils.py              # Data loading functions
    └── viz.py                   # Plotting and visualization functions
```
    

## Installation and Usage

### 1. Prerequisites

Ensure you have Python 3.13.7 installed. It is recommended to use a virtual environment.

### 2. Install Dependencies

Run the following command to install the required libraries:

```bash
pip install -r requirements.txt
```

### 3. Run the Analysis

Open the Jupyter Notebook to view the report and results:

```bash
jupyter notebook report.ipynb
```
