# CIS261 WK10 VIBE

Welcome to the `CIS261_WK10_VIBE` project! This small Python program is a student grade manager built around a `Student` class and a simple text file for storage. It is designed to be easy to use while also giving you practice with file I/O, object-oriented programming, and terminal menus.

## What it does

`VIBE.py` lets you:

- Add new students with an ID and three test scores
- Automatically calculate each student’s average score and letter grade
- Display all saved student records in a neat table
- Search students by name (case-insensitive)
- Generate class statistics with the highest and lowest average
- Save records to `student_grades.txt`

## File structure

- `VIBE.py` — the main Python script
- `student_grades.txt` — the data file where student records are stored

## How to run

From the project folder, run:

```bash
python3 VIBE.py
```

Then use the menu options to manage student records.

## Menu options

The app includes a clean text menu with:

1. Add new student
2. Display all students
3. Search student by name
4. Class statistics
5. Save records now
6. Exit

## Student record format

Each saved student record includes:

- Name
- ID
- Test 1 score
- Test 2 score
- Test 3 score
- Average score
- Letter grade

Records are stored in `student_grades.txt` using a pipe-separated format.

## Why this project is fun

This program is a great way to practice real-world coding concepts like:

- Creating and using custom classes
- Reading and writing text files
- Validating user input
- Formatting output for terminal display
- Working with simple menus and control flow

## Notes

- Enter `ESC` at any prompt to cancel an action.
- Scores must be between `0` and `100`.
- The app saves the current data automatically when you exit.

Enjoy using `VIBE.py` — and feel free to customize the menu, grading rules, or file format to make it your own!
