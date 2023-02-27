# 420kV SF6 circuit breaker pressure simulator

## Pressure simulator constraints:

- **_Total Range_**: 70 psi to 90 psi,
- **_Desired Range_**: 75 ppm to 85 ppm
- **_Mean_**: 80 psi
- **_Standard Deviation_**: 2.0%

---

## How to use the pressure simulator

- The simulator is a python script that will be run from the command line / terminal.
- The simulator will generate sensor readings for a whole month.
- The simulated sensor readings will be generated in 1 minute intervals.
- The generated data will be written to a csv file named "{name}-pressure-{month}-{year}.csv" in a local data directory.

- The simulator takes 3 required arguments:
  1. The circuit breaker name
  2. The month as an integer
  3. The year as a 4 digit integer

---

## Run the following commands to generate pressure data for a breaker named "sf6" in January 2022.

- Switch to the "pressure" directory: `cd <path>/sensors/pressure/`
- Run the simulator: `python pressure-sim.py sf6 1 2022`
