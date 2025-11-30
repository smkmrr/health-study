import pandas as pd                                                                            
import numpy as np                                                                              
from scipy.stats import ttest_ind


def get_descriptive_stats (df):              

    """
    Calculates descriptive statistics (mean, median, min, max) for selected columns.
    """                                                   

    
    columns_to_analyze = ['age', 'weight', 'height', 'systolic_bp', 'cholesterol']                    

    
    selected_data = df[columns_to_analyze]                                                
    
    all_stats = selected_data.describe()        

    required_stats = all_stats.loc[['mean', '50%', 'min', 'max']]                                               

    
    return required_stats                               




def run_disease_simulation(df, num_simulations=1000):   

    """
    Calculates the probability of having the disease using a 1000 simulation.
    """
   
    
    real_probability = df['disease'].mean()
    
    np.random.seed(42)
    
    simulation_results = np.random.binomial(1, real_probability, num_simulations)
    
    
    simulated_probability = simulation_results.mean()
    
    
    return real_probability, simulated_probability


def calculate_confidence_interval(df, confidence_level=0.95):   

    """
    Calculates 95% cinfidence interval for systolisc blood pressure.
    """
    
   
    mean = df['systolic_bp'].mean()
    std_dev = df['systolic_bp'].std()
    n = len(df)
    
    
    z_score = 1.96 
    
    
    margin_of_error = z_score * (std_dev / np.sqrt(n))
    
    
    lower_bound = mean - margin_of_error

    upper_bound = mean + margin_of_error
    
    
    return lower_bound, upper_bound


def test_smoker_blood_pressure(df):

    """
    compare blood pressure between smokers and non-smokers.
    """


    smokers_bp = df[df['smoker'] == 'Yes']['systolic_bp']

    non_smokers_bp = df[df['smoker'] == 'No']['systolic_bp']


    t_statistic, p_value = ttest_ind(smokers_bp, non_smokers_bp, equal_var=False)


    return t_statistic, p_value


def calculate_ci_bootstrap(data, confidence_level=0.95, num_simulations=10000):

    """
    calculates the confidence interval using the Bootstrap method.
    """


    
    data_array = data.to_numpy()
    n = len(data_array)


    
    
    simulated_means = []
    
    
    for _ in range(num_simulations):
        
        resample = np.random.choice(data_array, size=n, replace=True)
        
        
        simulated_means.append(resample.mean())
        
    
    alpha = (1 - confidence_level) / 2
    lower_bound = np.percentile(simulated_means, alpha * 100)
    upper_bound = np.percentile(simulated_means, (1 - alpha) * 100)
    

    
    return lower_bound, upper_bound

