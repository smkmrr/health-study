
import matplotlib.pyplot as plt          
import numpy as np                        

# 1. Histogram
def plot_bp_histogram(df):             


    """
    Plots a histogram of systolic blood presure
    """                      
    

    fig, ax = plt.subplots(figsize=(10, 6))

    systolic_bp = 'systolic_bp'

    ax.hist(df[systolic_bp], bins=30, edgecolor='black')

    
    ax.set_title("Histogram of systolic blood pressure")
    ax.set_xlabel("systolic blood pressure (mmHg)")
    ax.set_ylabel("Total number of patients")


    ax.grid(True, axis='y')


    ax.spines['left'].set_visible(True)
    ax.spines['right'].set_visible(True)
    ax.spines['top'].set_visible(True)
    ax.spines['bottom'].set_visible(True)


    plt.show()






# 2. Boxplot
def plot_weight_boxplot(df):               
    """
    Plots a boxplot of weight by gender
    """                                      

    
    plt.figure(figsize=(8, 6))                                                                  
    
    df.boxplot(column='weight', by='sex')                                                           

    
    plt.title('Distribution of weight by sex')                                                     
    plt.xlabel('Gender')                                                                         
    plt.ylabel('Weight (kg)')                                                                        
    
    
    plt.suptitle('')                                                                             
    
    
    plt.show()                                                                                      




# 3. Bar chart
def plot_smoker_bar_chart(df):

    """
    Plots a bar chart of the number of smokers and non-smokers
    """

    smoker_counts = df['smoker'].value_counts()

    plt.figure(figsize=(7, 5))


    plt.bar(smoker_counts.index, smoker_counts.values, color=['#4CAF50', '#F44336'])


    plt.title('number of smokers vs. number of non-smokers')
    plt.xlabel('Smokers')
    plt.ylabel('Number of patients')

    plt.show()


# 4. Scatter plot
def plot_age_vs_bp(df):


    """
    Plots a scatter plot of age vs. systolic blood pressure
    """

   
    plt.figure(figsize=(10, 6))
    
    
    plt.scatter(df['age'], df['systolic_bp'], alpha=0.5, label='Patients')
    
    
    m, b = np.polyfit(df['age'], df['systolic_bp'], 1)
    
    
    plt.plot(df['age'], m*df['age'] + b, color='red', linewidth=2, label=f'Trend (Slope: {m:.2f})')
    
    
    plt.title('Relationship: Age vs. Systolic Blood Pressure')
    plt.xlabel('Age (years)')
    plt.ylabel('Systolic BP (mmHg)')
    plt.legend()
    plt.grid(True, alpha=0.3)


    
    plt.show()