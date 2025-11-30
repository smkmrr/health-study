import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
from sklearn.linear_model import LinearRegression 

class HealthAnalyzer:

    """ 
    A class for analyzing health data. 
    """
    
    def __init__(self, data_frame):

        """
        Initialize the analyzer with a pandas DataFrame.
        """
       
        self.df = data_frame



    def get_descriptive_stats(self):

        """
        Calculates descriptive statistics (mean, median, min, max) for selected columns.
        """

        
        columns_list = ['age', 'weight', 'height', 'systolic_bp', 'cholesterol']
        selected_data = self.df[columns_list]
        
        
        return selected_data.describe().loc[['mean', '50%', 'min', 'max']]
    
    



    def run_disease_simulation(self, num_simulations=1000, seed=42):


        """
        Calculates the probability of having the disease using a 1000 simulation.
        """


       
        real_probability = self.df['disease'].mean()

        
        np.random.seed(seed)
        simulation_results = np.random.binomial(1, real_probability, num_simulations)

        
        simulated_probability = simulation_results.mean()
        
        return real_probability, simulated_probability
    


    def calculate_bp_confidence_interval(self, confidence_level=0.95):

        """
        Calculates 95% cinfidence interval for systolisc blood pressure.
        """
        

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
        compare blood pressure between somekers and non-smokers.
        """
        
        smokers_bp = self.df[self.df['smoker'] == 'Yes']['systolic_bp']
        non_smokers_bp = self.df[self.df['smoker'] == 'No']['systolic_bp']
        

        t_statistic, p_value = ttest_ind(smokers_bp, non_smokers_bp, equal_var=False, alternative='greater')

        
        return t_statistic, p_value
    


    def predict_blood_pressure(self):

        """
        Performs a linear regression to predict blood pressure. Tests the accuracy of the model
        """
        
        
        X = self.df[['age', 'weight']]
        y = self.df['systolic_bp']
        
        
        model = LinearRegression()
        model.fit(X, y)
        
        
        
        coefficients = model.coef_
        intercept = model.intercept_


        
        return coefficients, intercept