# 420kV SF6 circuit breaker moisture simulator

## Density simulator constraints:

- **_Total Range_**: 0 ppm to 50 ppm,
- **_Desired Range_**: 0 ppm to 20 ppm
- **_Mean_**: 10ppm
- **_Standard Deviation_**: 20.0%

---

## How to use the moisture simulator

- The simulator is a python script that will be run from the command line / terminal.
- The simulator will generate sensor readings for a whole month.
- The simulated sensor readings will be generated in 1 minute intervals.
- The generated data will be written to a local file named "{name}-density-{month}-{year}.csv"

- The simulator takes 3 required arguments:
  1. The circuit breaker name
  2. The month as an integer
  3. The year as a 4 digit integer

---

## Run the following commands to generate moisture data for a breaker named "sf6" in January 2022.

- Switch to the "moisture" directory: `cd <path>/sensors/moisture/`
- Run the simulator: `python moisture-sim.py sf6 1 2022`
