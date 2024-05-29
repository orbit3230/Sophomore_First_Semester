import pandas as pd
from collections import Counter

df_raw = pd.read_csv('./creditcard.csv')
df=df_raw.drop(['Time','Class'], axis=1)

feature_list=list(df.columns)

def IQR_method(df, n, features):
    """
    This function prints the number of outliers for every feature
    This function returns a list of indexes that contains more than n outliers according to the IQR
    df: DataFrame
    n: number of outliers
    features: list of feature
    returns: a list of indexes that contains more than n outliers according to the IQR
    
    hint: df.index returns indexes of data in the dataframe
    """
    outlier_list=[]
    for column in features:
        ###
        #writedown your code from here






        #to here
        ###        
        print('Total number of outliers is:', df1.shape[0]+df2.shape[0])

    #selecting observations containing more than n outliers\
    outlier_list = Counter(outlier_list)
    ###writedown your code from here 
    multiple_outliers = 
    #to here
    ###
    

    return multiple_outliers
  
    
# detecting outliers
Outliers_IQR = IQR_method(df,1,feature_list)
# dropping outliers
df_out = df.drop(Outliers_IQR, axis = 0).reset_index(drop=True)