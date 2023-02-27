import argparse
import pandas as pd
import numpy as np
import time
import calendar
import os

def generate_pressure_data(name, month, year):
    # calculate number of days in the given month and year
    num_days = pd.Period(f'{year}-{month}').days_in_month

    # create datetime index for the entire month
    date_rng = pd.date_range(start=f'{year}-{month}-01 00:00:00', end=f'{year}-{month}-{num_days} 23:59:00', freq='1min')

    # set random seed for randomization
    np.random.seed(int(time.time()))

    # generate random pressure values with mean of 80 psi and standard deviation of 2.0%
    pressure_mean = 80
    pressure_std_dev = pressure_mean * 0.020
    pressure_values = np.random.normal(loc=pressure_mean, scale=pressure_std_dev, size=len(date_rng))

    # round the pressure values to 2 decimal points
    pressure_values = np.round(pressure_values, 1)

    # create DataFrame with timestamp, name, and pressure columns
    data = pd.DataFrame({'timestamp': date_rng, 'name': name, 'pressure (psi)': pressure_values})

    # create directory if it doesn't exist
    data_dir = 'data'
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)

    filename = os.path.join(data_dir, f"{name}-pressure-{calendar.month_name[args.month].lower()}-{year}.csv")

    # write DataFrame to CSV file
    data.to_csv(filename, index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate simulated pressure data for a circuit breaker.')
    parser.add_argument('name', type=str, help='name of circuit breaker')
    parser.add_argument('month', type=int, help='month for which to generate data')
    parser.add_argument('year', type=int, help='year for which to generate data')
    args = parser.parse_args()

    generate_pressure_data(args.name, args.month, args.year)