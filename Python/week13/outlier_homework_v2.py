import pandas as pd
from collections import Counter

df_raw = pd.read_csv('./creditcard.csv')
df=df_raw.drop(['Time','Class'], axis=1)

feature_list=list(df.columns)

def IQR_method(df, n, features):
    """
    This function prints the number of outliers for every feature
    This funciton also returns a list which has indexes that containing more than n outliers according to the IQR
    df: DataFrame
    n: number of outliers
    features: a list of feature
    returns: a list corresponding to the observations containing more than n outliers according to the TukeY IQR
    
    hint: df.index returns indexes of all data
    """
    outlier_list=[]
    for column in features:
        #This loop calculates the outliers at the current column
        Q1 = df[column].quantile(0.25)  # 25% percentile
        Q3 = df[column].quantile(0.75)  # 75% percentile
        IQR = Q3 - Q1                   # InterQuartile Range
        
        outlier_step = 1.5 * IQR
        # Q1 - outlier_step : minimum value
        # Q3 + outlier_step : maximum value
        # if the value is off the range, OUTLIER-!
        df_outliers = df[(df[column] < Q1 - outlier_step) | (df[column] > Q3 + outlier_step)]
        outlier_list.extend(df_outliers.index)
               
        print('Total number of outliers is:', df_outliers.shape[0])

    #selecting data containing more than n outliers
    multiple_outliers = [k for k, v in Counter(outlier_list).items() if v > n]
    
    return multiple_outliers
    
# detecting outliers
n=1
Outliers_IQR = IQR_method(df,n,feature_list)
print(f'Type of Outliers_IQR is: {type(Outliers_IQR)}')
# dropping outliers
df_out = df.drop(Outliers_IQR, axis = 0).reset_index(drop=True)
print(f'When n is {n}, {df_out.shape[0]} data is available')

# detecting outliers
n=3
Outliers_IQR = IQR_method(df,n,feature_list)
# dropping outliers
df_out = df.drop(Outliers_IQR, axis = 0).reset_index(drop=True)
print(f'When n is {n}, {df_out.shape[0]} data is available')

# detecting outliers
n=4
Outliers_IQR = IQR_method(df,n,feature_list)
# dropping outliers
df_out = df.drop(Outliers_IQR, axis = 0).reset_index(drop=True)
print(f'When n is {n}, {df_out.shape[0]} data is available')
