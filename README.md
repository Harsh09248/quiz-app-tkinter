# Quiz App using Tkinter

A modern, GUI-based quiz application built with Python's Tkinter module. This educational app presents multiple-choice questions, evaluates user answers in real-time, and stores high scores using a local SQLite database.

---



## Table of Contents

- [ Features](#-features)
- [ File Structure](#-file-structure)
- [How to Run](#-how-to-run)
- [Requirements](#-requirements)
- [License](#-license)

## Features

- **Multiple-Choice Questions**  
  Presents a series of quiz questions, each with four possible answers.

- **Real-Time Feedback**  
  Checks the user's answer instantly and provides immediate response indicating correctness.

- **Score Tracking**  
  Continuously updates and displays the user’s score throughout the quiz.

- **User-Friendly Interface**  
  Developed using Python’s Tkinter module to provide a clean and responsive graphical interface.

- **Persistent Score Storage**  
  Uses a local SQLite database (`quiz.scores.db`) to store and retrieve user scores.

- **Restart and Replay Options**  
  Allows users to retake the quiz without restarting the application.

- **Modular Codebase**  
  Organized into separate Python modules for GUI, logic, question model, data management, and database operations.
  ## File Structure

The project follows a modular structure to keep the code clean and maintainable.

```text
quiz-app-tkinter/
├── main.py              # Main entry point of the application
├── ui.py                # GUI components and layout (Tkinter)
├── data.py              # Contains or generates quiz question data
├── question_model.py    # Defines the structure of a quiz question
├── quiz_brain.py        # Handles quiz logic and progression
├── score_db.py          # Manages SQLite database for score storage
├── quiz.scores.db       # Local database file (auto-created)
└── README.md            # Project documentation

```
  ## How to Run

Follow these steps to run the Quiz App on your local machine:

1. **Ensure Python is installed**  
   This application requires Python 3.6 or higher.  
   You can download it from the official website: https://www.python.org/downloads/

2. **Clone or download the repository**

   If you are using Git:
   ```bash
   git clone https://github.com/YOUR_USERNAME/quiz-app-tkinter.git
   cd quiz-app-tkinter


## Requirements

This application is built using only standard Python libraries, so no external installations are needed beyond Python itself.

### Software Requirements

- Python 3.6 or higher

### Python Standard Libraries Used

- `tkinter` – for the graphical user interface (GUI)
- `sqlite3` – for local database storage
- `random` – for shuffling or selecting questions (if used)

> Note: `tkinter` and `sqlite3` are included by default with standard Python installations.


## License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this software for personal or commercial purposes, provided that proper credit is given to the original author.




