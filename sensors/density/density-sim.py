import argparse
import pandas as pd
import numpy as np
import time
import calendar

def generate_density_data(name, month, year):
    # calculate number of days in the given month and year
    num_days = pd.Period(f'{year}-{month}').days_in_month
    
    # create datetime index for the entire month
    date_rng = pd.date_range(start=f'{year}-{month}-01 00:00:00', end=f'{year}-{month}-{num_days} 23:59:50', freq='1min')
    
    # set random seed for randomization
    np.random.seed(int(time.time()))

    # generate random density values with mean of 6.75 lb/ft3 and standard deviation of 2.0%
    density_mean = 6.75
    density_std_dev = density_mean * 0.020
    density_values = np.random.normal(loc=density_mean, scale=density_std_dev, size=len(date_rng))

    # round the density values to 2 decimal points
    density_values = np.round(density_values, 2)

    # create DataFrame with timestamp, name, and density columns
    data = pd.DataFrame({'timestamp': date_rng, 'name': name, 'density (lb/ft3)': density_values})

    filename = f"{name}-density-{calendar.month_name[args.month].lower()}-{year}.csv"

    # write DataFrame to CSV file
    data.to_csv(filename, index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate simulated density data for a circuit breaker.')
    parser.add_argument('name', type=str, help='name of circuit breaker')
    parser.add_argument('month', type=int, help='month for which to generate data')
    parser.add_argument('year', type=int, help='year for which to generate data')
    args = parser.parse_args()

    generate_density_data(args.name, args.month, args.year)