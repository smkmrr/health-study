# Health Study Data Analysis

## Overview
This project performs a statistical analysis on a health dataset to explore relationships between age, weight, smoking status, systolystic blood pressure, cholesterol.

The analysis is presented in a Jupyter Notebook (`report.ipynb`). To maintain a clean and modular codebase, all data processing, statistical calculations, and visualization logic are separated into Python modules within the `src/` directory.

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
    
## Features & Methodology

The analysis covers the following key statistical areas:

1.  **Descriptive Analysis**: Calculation of Mean, Median, Min, and Max for key health variables.
2.  **Data Visualization**:
      * **Histogram**: To analyze the distribution of Systolic Blood Pressure.
      * **Boxplot**: To compare weight distributions between genders.
      * **Bar Chart**: To visualize the ratio between smokers and non-smokers.
3.  **Simulation**: Using `numpy.random` with seed to validate the observed disease prevalence against a simulated population ($N=1000$).
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
