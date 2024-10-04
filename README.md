# Focus Timer

## Overview

The **Focus Timer** is a productivity tool developed in Python using the Tkinter library for the graphical user interface (GUI). The timer helps users follow the Pomodoro technique by managing alternating periods of work and rest. The timer is customizable, and it notifies users with sound alerts and pop-up messages when it's time to take a break or get back to work.

## Features

- **Customizable Timer**: Users can set their own work time, rest time, and number of cycles.
- **Visual Interface**: A simple and clean interface with a black background and green font to display the countdown.
- **Sound Notifications**: Audio alerts at the end of work and rest periods to keep the user informed.
- **Settings**: Allows users to adjust work and rest durations, as well as the number of cycles.
- **Pop-up Alerts**: Informative pop-ups notify users when it's time to take a break or resume work.

## Project Structure

The project consists of the following key files:

- **promaofocus.py**: The main Python script that contains the logic for the Focus Timer.
- **requirements.txt**: A list of the required Python packages to run the project.

## Requirements

To run the Focus Timer, ensure you have the following Python packages installed:

- `playsound==1.3.0` (for playing sound notifications)
- `tk==0.1.0` (for the Tkinter GUI)
- `ttkthemes==3.2.2` (for additional themes, though not currently utilized)

Install these packages by running:

```bash
pip install -r requirements.txt
```

## Usage

1. **Running the Program**:

   Run the Python script with the following command:

   ```bash
   python promofocus.py
   ```

2. **Timer Display**: The timer starts at 00:00. Click the Start button to begin the countdown. The default work time is 25 minutes, and the rest time is 5 minutes, but these can be changed in the settings.

3. **Settings**: Click the Settings button to modify the work time, rest time, and the number of cycles. Enter the desired values in the pop-up dialog boxes.

4. **Reset Timer**: If you want to reset the timer at any point, press the Reset button. The timer will stop, and the display will reset to 00:00.

5. **Sound Notification**: When the timer completes a cycle (work or rest), a sound will play to notify the user.

6. **Pop-ups**: At the end of each work cycle, a pop-up message will notify the user to take a break. After the rest period, another message will alert the user to return to work.

## Known Issues
- Reset Behavior: If the reset button is pressed mid-cycle, no further notifications will appear for that cycle.

- Sound File Path: When running as an executable, ensure the sound file is correctly bundled or placed in the appropriate directory.

## Future Enhancements
- Theme Support: Implement support for different themes using the ttkthemes package.
- Progress Tracking: Add a progress bar to visually track the number of cycles completed.

## License
This project is open-source under the <b> MIT License </b>.