# 420kV SF6 circuit breaker density simulator

## Density simulator constraints:

- **_Total Range_**: 6.00 lb/ft3 to 8.00 lb/ft3
- **_Desired Range_**: 6.25 lb/ft3 to 7.25 lb/ft3
- **_Mean_**: 6.75 (lb/ft3)
- **_Standard Deviation_**: 2.0%

---

## How to use the density simulator

- The simulator is a python script that will be run from the command line / terminal.
- The simulator will generate sensor readings for a whole month.
- The simulated sensor readings will be generated in 1 minute intervals.
- The generated data will be written to a local file named "{name}-density-{month}-{year}.csv"

- The simulator takes 3 required arguments:
  1. The circuit breaker name
  2. The month as an integer
  3. The year as a 4 digit integer

---

## Run the following commands to generate density data for a breaker named "sf6" in January 2022.

- Switch to the "density" directory: `cd <path>/sensors/density/`
- Run the simulator: `python density-sim.py sf6 1 2022`
