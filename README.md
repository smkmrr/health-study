# Health Data Analysis Study

This project implements a statistical analysis and machine learning pipeline using a health dataset. It is designed to explore relationships between health metrics (such as age, weight, and smoking habits), cardiovascular health (systolic blood pressure), and gender.

The project uses **Object-Oriented Programming (OOP)** principles to organize analysis logic and utilizes **Linear Algebra** via `scikit-learn` for predictive modeling.

The primary goal of this analysis is to derive insights from patient data using various statistical methods and machine learning techniques.

---

## Key Analysis Steps:

### 1. Descriptive Analysis:
- Calculation of summary statistics (Mean, Median, Min, Max) for age, weight, height, blood pressure, and cholesterol.
- Identification of hypertension prevalence (systolic BP > 140 mmHg).

### 2. Simulation:
- Monte Carlo-style simulation to compare disease prevalence in the dataset against a simulated population of 1000 individuals.

### 3. Statistical Inference:
- **Confidence Intervals:** Calculation of the 95% confidence interval for mean systolic blood pressure using both Normal Approximation and Bootstrap methods.
- **Hypothesis Testing:** A two-sample t-test to determine if there is a statistically significant difference in blood pressure between smokers and non-smokers.
- **Power Analysis:** Simulation to determine the statistical power of the hypothesis test.

### 4. Predictive Modeling (Linear Algebra):
- **Linear Regression:** A model predicting systolic blood pressure based on Age and Weight.
- **Visualization:** Scatter plot with a regression trendline to visualize correlations.

---

## Visualizations

The notebook generates several visualizations to interpret the data:
- **Histogram:** Distribution of systolic blood pressure.
- **Boxplot:** Weight distribution comparisons by gender.
- **Bar Chart:** Proportion of smokers vs. non-smokers.
- **Scatter Plot:** Age vs. Blood Pressure with a linear regression trendline.

---

## Project Structure

The code is modularized into the `src` directory:


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

---
## How to Run

### Prerequisites
* Python 3.13+ installed.
* Git installed.

### Installation

To ensure reproducibility, please use a virtual environment and install the exact dependencies.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/smkmrr/health-study.git
    cd health-study
    ```

2.  **Set up the Virtual Environment:**
    ```bash
    # Create the environment
    python -m venv venv

    # Activate the environment (Windows Git Bash)
    source venv/Scripts/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Analysis
1.  Open the project folder in **VS Code**.
2.  Open the `report.ipynb` file.
3.  Click the **"Run All"** button at the top of the notebook to execute the full analysis pipeline.
