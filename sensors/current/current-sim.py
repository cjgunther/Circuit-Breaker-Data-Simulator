import argparse
import pandas as pd
import numpy as np
import time
import calendar
import os

def generate_current_data(name, month, year):
    # calculate number of days in the given month and year
    num_days = pd.Period(f'{year}-{month}').days_in_month
    
    # create datetime index for the entire month
    date_rng = pd.date_range(start=f'{year}-{month}-01 00:00:00', end=f'{year}-{month}-{num_days} 23:59:50', freq='1min')
    
    # set random seed for randomization
    np.random.seed(int(time.time()))

    # generate random current values with mean of 2250 A and standard deviation of 2.5%
    current_mean = 2250
    current_std_dev = current_mean * 0.025
    current_values = np.random.normal(loc=current_mean, scale=current_std_dev, size=len(date_rng))

    # round the current values to 2 decimal points
    current_values = np.round(current_values, 2)

    # create DataFrame with timestamp, name, and current columns
    data = pd.DataFrame({'timestamp': date_rng, 'name': name, 'current (A)': current_values})

    # create folder for data if it doesn't exist
    data_dir = 'data'
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)

    # create filename for CSV file
    filename = os.path.join(data_dir, f"{name}-current-{calendar.month_name[args.month].lower()}-{year}.csv")

    # write DataFrame to CSV file
    data.to_csv(filename, index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate simulated current data for a circuit breaker.')
    parser.add_argument('name', type=str, help='name of circuit breaker')
    parser.add_argument('month', type=int, help='month for which to generate data')
    parser.add_argument('year', type=int, help='year for which to generate data')
    args = parser.parse_args()

    generate_current_data(args.name, args.month, args.year)