import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
from sklearn.linear_model import LinearRegression 

class HealthAnalyzer:
    """
    A class to analyze health study data.
    """
    
    def __init__(self, data_frame):
        """
        Initialize the analyzer with a pandas DataFrame.
        """
        # This is where we store the data inside the class
        self.df = data_frame

    def get_descriptive_stats(self):
        """
        Calculates descriptive statistics (mean, median, min, max) for key metrics.
        """
        # Notice we use 'self.df' to access the data now
        columns_list = ['age', 'weight', 'height', 'systolic_bp', 'cholesterol']
        selected_data = self.df[columns_list]
        
        # Return specific rows
        return selected_data.describe().loc[['mean', '50%', 'min', 'max']]
    
    # ... (paste this below your get_descriptive_stats method) ...

    def run_disease_simulation(self, num_simulations=1000, seed=42):
        """
        Calculates real disease probability and runs a binomial simulation.
        """
        # Use self.df
        real_probability = self.df['disease'].mean()
        
        np.random.seed(seed)
        simulation_results = np.random.binomial(1, real_probability, num_simulations)
        
        simulated_probability = simulation_results.mean()
        
        return real_probability, simulated_probability

    def calculate_bp_confidence_interval(self, confidence_level=0.95):
        """
        Calculates 95% CI for systolic_bp using normal approximation.
        """
        # Access specific column from self.df
        data = self.df['systolic_bp']
        
        mean = data.mean()
        std_dev = data.std()
        n = len(data)
        
        z_score = 1.96 
        margin_of_error = z_score * (std_dev / np.sqrt(n))
        
        lower_bound = mean - margin_of_error
        upper_bound = mean + margin_of_error
        
        return lower_bound, upper_bound

    def test_smoker_blood_pressure(self):
        """
        Tests if smokers have different BP than non-smokers.
        """
        # Filter data using self.df
        smokers_bp = self.df[self.df['smoker'] == 'Yes']['systolic_bp']
        non_smokers_bp = self.df[self.df['smoker'] == 'No']['systolic_bp']
        
        t_statistic, p_value = ttest_ind(smokers_bp, non_smokers_bp, equal_var=False, alternative='greater')
        
        return t_statistic, p_value
    
    def predict_blood_pressure(self):
        """
        Performs a simple linear regression to predict systolic_bp from age and weight.
        Returns the model coefficients (impact of age/weight) and the intercept.
        """
        # 1. Prepare the data (X = Inputs, y = Target)
        # Scikit-learn expects X to be a list of columns (2D array)
        X = self.df[['age', 'weight']]
        y = self.df['systolic_bp']
        
        # 2. Create and train the model
        model = LinearRegression()
        model.fit(X, y)
        
        # 3. Get the results (The math formula it found)
        # Coefficient: How much BP goes up for every 1 year of age / 1 kg of weight
        coefficients = model.coef_
        intercept = model.intercept_
        
        return coefficients, intercept