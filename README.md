# High-Voltage 420kV SF6 Circuit Breaker Data Simulator

## How to use the cb data simulator

- The simulator is a python script that will be run from the command line / terminal.
- The simulator will generate sensor readings for a whole month.
- The simulated sensor readings will be generated in 1 minute intervals.
- The generated data will be written to a local file named "{name}-data-{month}-{year}.csv" in a local directory named "data".

- The simulator takes 3 required arguments:
  1. The circuit breaker name
  2. The month as an integer
  3. The year as a 4 digit integer

## Run the following command to generate circuit breaker data for a breaker named "sf6" in January 2022.

- Run the simulator: `python cb-data-gen.py sf6 1 2022`

---

## Voltage:

- **_Total Range_**: 360 kV to 420 kV,
- **_Desired Range_**: 360 kV to 400 kV
- **_Mean_**: 380
- **_Standard Deviation_**: 2.0%

---

## Current:

- **_Total Range_**: 1750 A to 2750 A
- **_Desired Range_**: 2000 A to 2500 A
- **_Mean_**: 2250 A
- **_Standard Deviation_**: 2.5%
- **_Maximum sustained load_**: 3150 A

---

## Temperature:

- **_Total Range_**: -40 F to 104 F
- **_Desired Range_**: 60 F A to 80 F
- **_Mean_**: 70 F
- **_Standard Deviation_**: 2.5%

---

## Moisture:

- **_Total Range_**: 0 ppm to 50 ppm,
- **_Desired Range_**: 0 ppm to 20 ppm
- **_Mean_**: 10ppm
- **_Standard Deviation_**: 20.0%

---

## Density:

- **_Total Range_**: 6.00 lb/ft3 to 8.00 lb/ft3
- **_Desired Range_**: 6.25 lb/ft3 to 7.25 lb/ft3
- **_Mean_**: 6.75 (lb/ft3)
- **_Standard Deviation_**: 2.0%

---

## Pressure:

- **_Total Range_**: 70 psi to 90 psi,
- **_Desired Range_**: 75 psi to 85 psi
- **_Mean_**: 80 psi
- **_Standard Deviation_**: 2.0%
