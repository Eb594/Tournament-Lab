# AI Learning Log – TournamentLab

## Introduction

During the development of TournamentLab, I used AI as a learning assistant to understand Python concepts, plan the application structure, solve programming problems, and improve the quality of the project.

The goal was not simply to obtain working code but to understand how the different components work together.

## Concepts Learned

### 1. Python Functions

I learned how to create functions to perform specific tasks, pass arguments, and return results.

Examples include:
- `register_team()`
- `generate_fixtures()`
- `record_result()`
- `calculate_standings()`

### 2. Lists and Dictionaries

I learned how lists can store multiple teams and fixtures, while dictionaries can represent individual records using key-value pairs.

### 3. Input Validation

I learned how to validate user input and raise `ValueError` when invalid information is provided.

Examples include:
- Rejecting duplicate team names.
- Rejecting invalid team names.
- Preventing negative match scores.
- Preventing a match result from being recorded twice.

### 4. Algorithms and Loops

I learned how nested loops can generate round-robin fixtures by pairing every team with every other team exactly once.

I also learned how to calculate standings by processing completed matches.

### 5. Sorting

I learned how Python's `sorted()` function and sorting keys can rank teams using multiple conditions.

The tournament ranking system considers:
- Points.
- Goal difference.
- Goals scored.
- Alphabetical team name.

### 6. File Handling and JSON

I learned how to use Python's `json` module to save tournament data and load it again.

I also learned why saved data must be validated before it is used.

### 7. Modular Programming

I learned how to divide an application into separate modules so that each module handles a specific responsibility.

### 8. Automated Testing

I learned how to use Python's `unittest` framework to test application functionality.

I created 20 automated tests covering team registration, fixtures, results, standings, champion protection, and data storage.

## Challenges Encountered

Some of the challenges I encountered included:

- Understanding how to divide the project into modules.
- Generating unique round-robin fixtures.
- Calculating standings accurately.
- Preventing invalid match results.
- Saving and restoring tournament information.
- Understanding why automated tests were not initially discovered.

I addressed these challenges by reviewing the code, testing individual functions, and correcting implementation issues.

## How AI Assisted My Learning

AI helped me:
- Understand programming concepts.
- Break large tasks into smaller steps.
- Identify errors and possible improvements.
- Understand the purpose of individual functions.
- Develop test cases.
- Improve project documentation.

I reviewed and ran the code to verify its behaviour rather than relying only on suggested solutions.

## Conclusion

Building TournamentLab improved my understanding of Python functions, data structures, loops, validation, algorithms, JSON file handling, modular architecture, and automated testing.

The project also helped me develop a better approach to solving programming problems independently.