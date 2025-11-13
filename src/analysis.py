

#Import the pandas library
import pandas as pd                                                                             ##IMPORT pandas as pd

#Define a function that takes one input (the DataFrame)
def get_descriptive_stats (df):                                                                 ##FUNCTION get_descriptive_stats(df):

    #Create a list of the specific columns we want
    columns_list = ['age', 'weight', 'height', 'systolic_bp', 'cholesterol']                    ##SET columns_list TO ['age', 'weight', 'height', 'systolic_bp', 'cholesterol']

    ##Select only those columns from the data
    selected_data = df[columns_list]                                                            ##SET selected_data TO df[columns_list]


    #Calculate the statistics for the selected data
    stats = selected_data.describe()                                                            ##SET stats TO selected_data.describe()


    #Calculate the statistics for the selected data
    return stats                                                                                ##RETURN stats