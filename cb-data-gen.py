import argparse
import pandas as pd
import numpy as np
import time
import calendar
import os

def generate_breaker_data(name, month, year):
    # calculate number of days in the given month and year a create a date range
    num_days = 1#pd.Period(f'{year}-{month}').days_in_month
    date_rng = pd.date_range(start=f'{year}-{month}-01 00:00:00', end=f'{year}-{month}-{num_days} 23:59:00', freq='1min')

    # set random seed for randomization
    np.random.seed(int(time.time()))

    # generate random voltage values with mean of 375 kV and standard deviation of 2.5%
    voltage_mean = 375
    voltage_std_dev = voltage_mean * 0.025
    voltage_values = np.random.normal(loc=voltage_mean, scale=voltage_std_dev, size=len(date_rng))

    # generate random current values with mean of 2250 Amperes and standard deviation of 2.5%
    current_mean = 2250
    current_std_dev = current_mean * 0.025
    current_values = np.random.normal(loc=current_mean, scale=current_std_dev, size=len(date_rng))

    # generate random temperature values with mean of 70 degrees farenheit and standard deviation of 2.5%
    temp_mean = 70.0
    temp_std_dev = temp_mean * 0.025
    temp_values = np.random.normal(loc=temp_mean, scale=temp_std_dev, size=len(date_rng))

    # generate random moisture values with mean of 10 ppm and standard deviation of 20.0%
    moisture_mean = 10
    moisture_std_dev = moisture_mean * 0.200
    moisture_values = np.random.normal(loc=moisture_mean, scale=moisture_std_dev, size=len(date_rng))

    # generate random density values with mean of 6.75 lb/ft3 and standard deviation of 2.0%
    density_mean = 6.75
    density_std_dev = density_mean * 0.020
    density_values = np.random.normal(loc=density_mean, scale=density_std_dev, size=len(date_rng))

    # generate random moisture values with mean of 10ppm and standard deviation of 2.0%
    pressure_mean = 80
    pressure_std_dev = pressure_mean * 0.020
    pressure_values = np.random.normal(loc=pressure_mean, scale=pressure_std_dev, size=len(date_rng))

    # apply correlations
    voltage_values += voltage_values * np.random.normal(loc=0, scale=0.05, size=len(date_rng)) * (current_values/current_mean - 1)
    current_values += current_values * np.random.normal(loc=0, scale=0.05, size=len(date_rng)) * (voltage_values/voltage_mean - 1)
    temp_values += temp_values * np.random.normal(loc=0, scale=0.05, size=len(date_rng)) * (current_values/current_mean - 1)
    moisture_values += moisture_values * np.random.normal(loc=0, scale=0.05, size=len(date_rng)) * (temp_values/temp_mean - 1)
    density_values += density_values * np.random.normal(loc=0, scale=0.05, size=len(date_rng)) * (moisture_values/moisture_mean - 1)
    pressure_values += pressure_values * np.random.normal(loc=0, scale=0.05, size=len(date_rng)) * (moisture_values/moisture_mean - 1)

    # round values
    voltage_values = np.round(voltage_values, 1)
    current_values = np.round(current_values, 0)
    temp_values = np.round(temp_values, 1)
    moisture_values = np.round(moisture_values, 0)
    density_values = np.round(density_values, 2)
    pressure_values = np.round(pressure_values, 1)

    # create DataFrame with timestamp, name, current and voltage columns
    data = pd.DataFrame({
        'timestamp': date_rng,
        'name': name,
        'voltage (kV)': voltage_values,
        'current (A)': current_values,
        'temperature (F)': temp_values,
        'moisture (ppm)': moisture_values,
        'density (lb/ft3)': density_values,
        'pressure (psi)': pressure_values
    })

    # create directory if it doesn't exist
    data_dir = 'data'
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)

    filename = os.path.join(data_dir, f"{name}-data-{calendar.month_name[args.month].lower()}-{year}.csv")

    # save data to csv file
    data.to_csv(filename, index=False)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate simulated data for a circuit breaker.')
    parser.add_argument('name', type=str, help='name of circuit breaker')
    parser.add_argument('month', type=int, help='month for which to generate data')
    parser.add_argument('year', type=int, help='year for which to generate data')
    args = parser.parse_args()

    generate_breaker_data(args.name, args.month, args.year)