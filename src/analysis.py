import pandas as pd                                                                            
import numpy as np                                                                              
from scipy.stats import ttest_ind


def get_descriptive_stats (df):                                                                 

    
    columns_list = ['age', 'weight', 'height', 'systolic_bp', 'cholesterol']                    

    
    selected_data = df[columns_list]                                                            


   
    stats = selected_data.describe()                                                            

    
    return stats                                                                                




def run_disease_simulation(df, num_simulations=1000):   
   
    
    real_probability = df['disease'].mean()
    
    np.random.seed(42)
    
    simulation_results = np.random.binomial(1, real_probability, num_simulations)
    
    
    simulated_probability = simulation_results.mean()
    
    
    return real_probability, simulated_probability


def calculate_bp_confidence_interval(df, confidence_level=0.95): #
    
   
    mean = df['systolic_bp'].mean()
    std_dev = df['systolic_bp'].std()
    n = len(df)
    
    
    z_score = 1.96 
    
    
    margin_of_error = z_score * (std_dev / np.sqrt(n))
    
    
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error
    
    
    return lower_bound, upper_bound


def test_smoker_blood_pressure(df):


    smokers_bp = df[df['smoker'] == 'Yes']['systolic_bp']

    non_smokers_bp = df[df['smoker'] == 'No']['systolic_bp']

    t_statistic, p_value = ttest_ind(smokers_bp, non_smokers_bp, equal_var=False)

    return t_statistic, p_value




