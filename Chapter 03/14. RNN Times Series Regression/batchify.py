import numpy as np
import pandas as pd

def next_stock_batch(batch_size, n_steps, df_base, n_features):
    t_min = 0
    t_max = df_base.shape[0]
  
    # The inputs will be formed by 8 sequences taken from
    # 7 time series [ISE.1,SP,DAX,FTSE,NIKKEI,BOVESPA,EU]
    x = np.zeros((batch_size,n_steps,n_features))
    
    # We want to predict the returns of the Istambul stock
    # taken into consideration the previous n_steps days
    y = np.zeros((batch_size,n_steps,))

    # We chose batch_size random points from time series x-axis

    starting_points = np.random.randint(0,t_max-n_steps-1,size=batch_size)    
    #print(starting_points)
    df = df_base.drop('date', axis=1)
    feat = df.values

    # We create the batches for x using all time series (8) between t and t+n_steps    
    for i, sp in enumerate(starting_points):
        x[i] = feat[sp:sp+n_steps]
        y[i] = feat[sp+1:sp+n_steps+1, 1]
        
    # We create the batches for y using only one time series between t+1 and t+n_steps+1
    
    #Save on x and y the time series data sequence and the prediction sequence

    return x,y

df = pd.read_csv('data_akbilgic.csv')

x, y = next_stock_batch(32, 10, df, 9)

print(x[0])