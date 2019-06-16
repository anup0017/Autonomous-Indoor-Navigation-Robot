## How does Automatic Run work?

### 1. Run `ManualControl.py`
- Control the robot manually using keyboard controls (arrow keys).
- Press `q` to quit.
- The output data (`direction` and `time`) of the robot is exported to the csv file (`finaldata.csv`).

### 2. Run `AutoRun.py`
- The data stored in `finaldata.csv` file is imported (_direction[]_, _time[]_).
- Using this data, the robot takes the same path which was defined previously when it was manually controlled.