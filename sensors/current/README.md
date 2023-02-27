# 420kV SF6 circuit breaker current simulator

## Current simulator constraints:

- **_Total Range_**: 1750 A to 2750 A
- **_Desired Range_**: 2000 A to 2500 A
- **_Mean_**: 2250 A
- **_Standard Deviation_**: 2.5%
- **_Maximum sustained load_**: 3150 A

---

## How to use the current simulator

- The simulator is a python script that will be run from the command line / terminal.
- The simulator will generate sensor readings for a whole month.
- The simulated sensor readings will be generated in 1 minute intervals.

- The simulator takes 3 required arguments:
  1. The circuit breaker name
  2. The month as an integer
  3. The year as a 4 digit integer

---

## Run the following commands to generate current data for a breaker named "sf6" in January 2022.

- Switch to the "current" directory: `cd <path>/sensors/current/`
- Run the simulator: `python current-sim.py sf6 1 2022`

---

## **_Useful Information:_**

- ABB recommends the maximum continuous current for their 420kV SF/P SF6 circuit breaker to be 3150 Amperes.
- It is common for High-Voltage circuit breakers to operate at around 50% to 70% of their maximum sustained current rating for continuous operation.
