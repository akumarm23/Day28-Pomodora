# Pomodora Application

[![License: MIT](https://img.shields.io/badge/License-MIT-maroon.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8-yellow.svg)](https://www.python.org/downloads/)
![Version](https://img.shields.io/badge/version-v0.1-brightgreen)

## Overview

The Pomodora Application (`main.py`) is a simple timer application built with Tkinter, a GUI library for Python. It follows the Pomodoro Technique, a time management method developed by Francesco Cirillo, to improve productivity and focus during work or study sessions.

## Features

- Customizable work and break durations.
- Automatic transitions between work sessions and breaks.
- Visual and audio cues for session changes.
- Option to reset the timer.

## Constants

- `PINK`, `RED`, `GREEN`, `YELLOW`, `PURPLE`, `WHITE`, `BLACK`: Color constants used for styling.
- `FONT_NAME`: Font constant for consistent text styling.
- `WORK_MIN`, `SHORT_BREAK_MIN`, `LONG_BREAK_MIN`: Default durations for work, short breaks, and long breaks.
- `reps`: Counter for tracking the number of work and break sessions.
- `timer`: Variable to store the timer instance.

## Timer Mechanism

- `start_timer()`: Initiates the timer based on the current session (work, short break, or long break).
- `reset_timer()`: Resets the timer and session counter.

## Countdown Mechanism

- `count_down(count)`: Updates the timer display and manages the countdown logic.

## UI Setup

- Labels, buttons, and canvas elements for creating the user interface.
- Buttons to start and reset the timer.
- Checkmark label to display completed work sessions.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/akumarm23/Day28-Pomodora.git
   cd Day28-Pomodora
   ```

2. Run the script:

   ```bash
   python main.py
   ```

3. Start and reset the timer as needed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Feel free to contribute and enhance the functionality of this Pomodora Application! Happy coding!
