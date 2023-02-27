import argparse
import pandas as pd
import numpy as np
import time
import calendar
import os

def generate_moisture_data(name, month, year):
    # calculate number of days in the given month and year
    num_days = pd.Period(f'{year}-{month}').days_in_month

    # create datetime index for the entire month
    date_rng = pd.date_range(start=f'{year}-{month}-01 00:00:00', end=f'{year}-{month}-{num_days} 23:59:50', freq='1min')

    # set random seed for randomization
    np.random.seed(int(time.time()))

    # generate random moisture values with mean of 10 ppm and standard deviation of 20%
    moisture_mean = 10
    moisture_std_dev = moisture_mean * 0.20
    moisture_values = np.random.normal(loc=moisture_mean, scale=moisture_std_dev, size=len(date_rng))

    # round the moisture values to 0 decimal points
    moisture_values = np.round(moisture_values, 0)

    # create DataFrame with timestamp, name, and moisture columns
    data = pd.DataFrame({'timestamp': date_rng, 'name': name, 'moisture (ppm)': moisture_values})

    # create directory if it doesn't exist
    data_dir = 'data'
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)

    filename = os.path.join(data_dir, f"{name}-moisture-{calendar.month_name[args.month].lower()}-{year}.csv")

    # write DataFrame to CSV file
    data.to_csv(filename, index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate simulated moisture data for a circuit breaker.')
    parser.add_argument('name', type=str, help='name of circuit breaker')
    parser.add_argument('month', type=int, help='month for which to generate data')
    parser.add_argument('year', type=int, help='year for which to generate data')
    args = parser.parse_args()

    generate_moisture_data(args.name, args.month, args.year)