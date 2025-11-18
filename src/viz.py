
import matplotlib.pyplot as plt          
import numpy as np                        

# 1. Histogram
def plot_bp_histogram(df):                                             

    fig, ax = plt.subplots(figsize=(10, 6))

    systolic_bp = 'systolic_bp'

    ax.hist(df[systolic_bp], bins=30, edgecolor='black')

    
    ax.set_title("Histogram av sistolisk blodtryck")
    ax.set_xlabel("systoliskt blodtryck (mmHg)")
    ax.set_ylabel("Antal patienter")

    ax.grid(True, axis='y')

    ax.spines['left'].set_visible(True)
    ax.spines['right'].set_visible(True)
    ax.spines['top'].set_visible(True)
    ax.spines['bottom'].set_visible(True)


    plt.show()






# 2. Boxplot
def plot_weight_boxplot(df):                                                     

    
    plt.figure(figsize=(8, 6))                                                                  
    
    df.boxplot(column='weight', by='sex')                                                           

    
    plt.title('Fördelning av vikt efter kön')                                                     
    plt.xlabel('Kön')                                                                         
    plt.ylabel('vikt (kg)')                                                                        
    
    
    plt.suptitle('')                                                                             
    
    
    plt.show()                                                                                      




# 3. Bar chart
def plot_smoker_bar_chart(df):

    smoker_counts = df['smoker'].value_counts()

    plt.figure(figsize=(7, 5))


    plt.bar(smoker_counts.index, smoker_counts.values, color=['#4CAF50', '#F44336'])


    plt.title('Antal rökare vs. Antal icke-rökare')
    plt.xlabel('Rökare')
    plt.ylabel('antal patienter')

    plt.show()