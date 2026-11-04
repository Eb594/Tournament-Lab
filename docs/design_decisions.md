# TournamentLab – Design Decisions

## 1. Project Architecture

TournamentLab uses a modular architecture.

Instead of placing the entire application inside one Python file, its functionality is divided into separate modules.

### Decision

Each module handles a specific responsibility:

- `teams.py`: Team registration and team listing.
- `fixtures.py`: Round-robin fixture generation.
- `results.py`: Match result recording.
- `standings.py`: League table calculations and champion selection.
- `storage.py`: JSON data storage and validation.
- `cli.py`: Command-line interface and user interaction.
- `main.py`: Application entry point.

### Reason

This structure improves readability, maintainability, testing, and code organization.

## 2. Data Structures

### Decision

Lists and dictionaries are used to store tournament information.

A team is represented as:

```python
{
    "id": "TM001",
    "name": "Falcons"
}
```

A fixture is represented as:

```python
{
    "id": "M001",
    "home_id": "TM001",
    "away_id": "TM002",
    "status": "pending",
    "home_score": None,
    "away_score": None
}
```

### Reason

Dictionaries make it easy to access individual properties, while lists make it easy to manage multiple teams and fixtures.

## 3. Team Registration Rules

### Decision

The tournament accepts between 4 and 8 teams.

Team names are trimmed, checked for valid length, and compared without considering letter case.

### Reason

These rules prevent duplicate registrations and ensure that tournaments have a valid number of participants.

## 4. Round-Robin Fixture Generation

### Decision

Nested loops generate one fixture for every unique pair of teams.

### Reason

This ensures that every team plays every other team exactly once.

For a tournament containing N teams, the total number of fixtures is:

N × (N - 1) / 2

## 5. Match Result Validation

### Decision

Only nonnegative integer scores are accepted.

A fixture can only receive a result once.

### Reason

This prevents invalid scores and accidental modification of completed matches.

## 6. Standings Calculation

### Decision

Standings are calculated from completed fixtures rather than stored separately.

The points system is:

- Win: 3 points.
- Draw: 1 point.
- Loss: 0 points.

Teams are ranked using the following order:

1. Highest points.
2. Highest goal difference.
3. Highest goals scored.
4. Alphabetical team name.

### Reason

Calculating standings from match results reduces duplicated data and keeps the league table consistent with recorded results.

## 7. Champion Selection

### Decision

The champion is only returned when every fixture has been completed.

### Reason

This prevents a team from being declared champion before the tournament is finished.

## 8. JSON Storage

### Decision

JSON is used to save and load tournament information.

A schema version is included in the saved data.

### Reason

JSON is human-readable, supported by Python's standard library, and suitable for storing structured tournament information.

## 9. Standard Library Only

### Decision

The project uses Python's standard library without third-party packages.

### Reason

This keeps the project lightweight and avoids unnecessary dependencies.

## 10. Automated Testing

### Decision

Python's built-in `unittest` framework is used.

The project contains 20 automated tests.

### Reason

Automated tests help verify that important features work correctly and that invalid operations are rejected.

## Conclusion

These design decisions were made to keep TournamentLab modular, understandable, reliable, and easy to maintain.