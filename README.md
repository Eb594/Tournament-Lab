# TournamentLab – The Ultimate Esports League Manager

## Overview

TournamentLab is a Python command-line application designed to manage esports tournaments. It allows tournament organizers to register teams, generate round-robin fixtures, record match results, calculate league standings, and determine the tournament champion.

The application uses JSON for data storage, allowing tournament information to be saved and loaded between sessions.

## Features

- Register between 4 and 8 teams.
- Prevent duplicate team names.
- Generate round-robin fixtures automatically.
- Display tournament fixtures and match statuses.
- Record match results.
- Calculate league standings automatically.
- Rank teams using points, goal difference, goals scored, and team name.
- Save and load tournament data using JSON.
- Simulate a demonstration tournament.
- Declare a champion only after all fixtures are completed.
- Validate user input and tournament data.

## Technologies

- Python 3
- JSON
- Python Standard Library
- unittest

No external Python packages are required.

## Project Structure

```text
Tournament-Lab/
│
├── main.py
├── README.md
├── data.json
│
├── docs/
│   ├── ai_learning_log.md
│   └── design_decisions.md
│
├── tests/
│   ├── __init__.py
│   └── test_tournament.py
│
└── tournament/
    ├── __init__.py
    ├── cli.py
    ├── teams.py
    ├── fixtures.py
    ├── results.py
    ├── standings.py
    └── storage.py
```

## Installation and Setup

Clone the repository:

```bash
git clone <repository-url>
```

Enter the project directory:

```bash
cd Tournament-Lab
```

No additional package installation is necessary.

## Running the Application

Run:

```bash
python3 main.py
```

## Application Menu

The application provides these options:

1. Register a team.
2. List all teams.
3. Generate fixtures.
4. View fixtures.
5. Record match results.
6. View league standings.
7. Save tournament.
8. Load tournament.
9. Simulate demo tournament.
10. Show champion.
0. Exit.

## Running Tests

Run the automated test suite:

```bash
python3 -m unittest discover -s tests -v
```

The project currently contains 20 automated tests covering its major features and validation rules.

## Tournament Rules

- A tournament requires between 4 and 8 teams.
- Each team plays every other team exactly once.
- A win awards 3 points.
- A draw awards 1 point to each team.
- A loss awards 0 points.
- Teams are ranked by:
  1. Points.
  2. Goal difference.
  3. Goals scored.
  4. Team name in alphabetical order.
- A champion can only be declared after every fixture has been played.

## Data Storage

TournamentLab stores tournament information in JSON format.

The saved data contains:
- A schema version.
- Registered teams.
- Tournament fixtures.
- Match statuses and scores.

## Author

TournamentLab was developed as a Python programming project to demonstrate modular programming, data validation, file handling, algorithms, and automated testing.