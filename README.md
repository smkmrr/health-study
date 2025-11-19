# Health Study Data Analysis

## Overview
This project performs a statistical analysis on a health dataset to explore relationships between lifestyle factors (age, weight, smoking status) and health metrics (systolystic blood pressure, cholesterol).

The analysis is presented in a Jupyter Notebook (`report.ipynb`). To maintain a clean and modular codebase, all data processing, statistical calculations, and visualization logic are separated into Python modules within the `src/` directory.

## Project Structure
The repository is organized as follows:

```text
├── data/
│   └── health_study_dataset.csv   # The raw dataset used for analysis
├── src/
│   ├── analysis.py                # Statistical functions (Descriptive stats, T-tests, CI)
│   ├── io_utils.py                # Data loading and handling
│   └── viz.py                     # Visualization functions (Histograms, Boxplots)
├── report.ipynb                   # The main analysis notebook (Presentation layer)
├── requirements.txt               # List of Python dependencies
└── README.md                      # Project documentation
```

## Features & Methodology

The analysis covers the following key statistical areas:

1.  **Descriptive Analysis**: Calculation of Mean, Median, Min, and Max for key health variables.
2.  **Data Visualization**:
      * **Histogram**: To analyze the distribution of Systolic Blood Pressure.
      * **Boxplot**: To compare weight distributions between genders and identify outliers.
      * **Bar Chart**: To visualize the class imbalance between smokers and non-smokers.
3.  **Simulation**: A **Monte Carlo simulation** (using `numpy.random` with seed) to validate the observed disease prevalence against a simulated population ($N=1000$).
4.  **Confidence Interval**: Calculation of a 95% Confidence Interval for the population mean of systolic blood pressure.
5.  **Hypothesis Testing**: A **Two-sample T-test** to evaluate the hypothesis: *"Smokers have higher blood pressure than non-smokers."*

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
