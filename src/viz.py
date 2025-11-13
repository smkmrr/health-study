
#Import the plotting library
import matplotlib.pyplot as plt                                         #IMPORT matplotlib.pyplot as plt

#Define a function that takes the DataFrame
def plot_bp_histogram(df):                                              #FUNCTION plot_bp_histogram(df):

    #Create a new figure and set its size
    plt.figure(figsize=(10, 6))                                         #CREATE figure(figsize=(10, 6))
    
    #Create a histogram of the 'systolic_bp' column. Use 30 "bins" (bars) and add a black edge
    plt.hist(df['systolic_bp'], bins=30, edgecolor='black')             #PLOT histogram(df['systolic_bp'], bins=30, edgecolor='black')


    # 1. Calculate the mean and median
    mean_bp = df['systolic_bp'].mean()                                  #SET mean_bp TO the average value of the 'systolic_bp' column
    median_bp = df['systolic_bp'].median()                              #SET median_bp TO the middle value (median) of the 'systolic_bp' column
    
    # 2. Add a vertical line (axvline) for the mean
    plt.axvline(mean_bp, color='yellow', linestyle='dashed', linewidth=2, label=f'Mean: {mean_bp:.2f}')   #SET line color to 'yellow'; SET line style to 'dashed'; SET line width to 2; SET line label to "Mean: [value of mean_bp]"
    
    # 3. Add a vertical line for the median
    plt.axvline(median_bp, color='red', linestyle='dashed', linewidth=2, label=f'Median: {median_bp:.2f}')      #DRAW a vertical line on the plot at the 'median_bp' position; SET line color to 'red'; SET line style to 'dashed'; SET line width to 2; SET line label to "Median: [value of median_bp]"
    
    # 4. Add a legend to explain what the lines are
    plt.legend()                                                                                                #DISPLAY the plot's legend (to show what the 'Mean' and 'Median' lines are)

    # Add a line showing the "high" threshold
    plt.axvline(140, color='black', linestyle='dotted', linewidth=2, label='Hög blodtryck (140)')       #DRAW a vertical line on the plot at the 140 position; SET line color to 'black'; SET line style to 'dotted'; SET line width to 2; SET line label to "Hög blodtryck (140)"

    #This adds a horizontal grid, making the y-axis easier to read.
    plt.grid(axis='y', linestyle='--', alpha=0.7)                                                   #DISPLAY a grid on the plot's Y-axis; SET grid line style to 'dashed'; SET grid transparency to 0.7

    #Add the required labels
    plt.title('Fördelning av systoliskt blodtryck')                    #SET title TO 'fördelning av systolisk blodtryck'
    plt.xlabel('Systolic BP (mmHg)')                                    #SET x-label TO 'Systolic BP (mmHg)'
    plt.ylabel('Antal patienter')                                       #SET y-label TO 'Antal patientr'


    #Display the plot
    plt.show()                                                          #SHOW plot

#END



#Define function
def plot_weight_boxplot(df):                                                                    #FUNCTION plot_weight_boxplot(df):

    #Create a new figure
    plt.figure(figsize=(8, 6))                                                                      #CREATE figure(figsize=(8, 6))
    
    # Use the built-in pandas boxplot function that automatically groups the data
    df.boxplot(column='weight', by='sex')                                                           #CALLdf.boxplot(column='weight', by='sex') 
    
    # Add labels to make the plot clear
    plt.title('Fördelning av vikt efter kön')                                                       #SET title TO 'fördelning av vikt efter kön'
    plt.xlabel('Kön')                                                                               #SET x labels titel as 'kön'
    plt.ylabel('vikt (kg)')                                                                         #SET y-label's title as 'vikt(kg)'
    
    # This line removes the extra "Boxplot grouped by sex" title (pandas bring the default suptitle??)
    plt.suptitle('')                                                                                #CALL plt.suptitle('')
    
    # Display the plot
    plt.show()                                                                                      #SHOW plot





def plot_smoker_bar_chart(df):

    smoker_counts = df['smoker'].value_counts()

    plt.figure(figsize=(7, 5))


    plt.bar(smoker_counts.index, smoker_counts.values, color=['#4CAF50', '#F44336'])


    plt.title('Antal rökare vs. Antal icke-rökare')
    plt.xlabel('Rökare')
    plt.ylabel('antal patienter')

    plt.show()