# 🏋️ Fan Pro Fitness Tracker

A command-line fitness tracking application built in Python as a university coursework project. The app lets users log workouts, track calories, and review their session history — all saved locally to a JSON file so data persists between runs.

---

## What It Does

- Log three workout types: **Running**, **Walking**, and **General Exercise**
- Automatically calculates calories burned based on duration and activity type
- Saves all workout records to a local JSON file (`workout.txt`)
- Displays workout history with dates, durations, distances, and calorie totals
- Supports updating and deleting existing records
- Built around an **OOP class hierarchy**: `Workout → Walking → Running`

---

## How to Run

**Requirements:** Python 3.x (no external libraries needed)

```bash
# Clone or download the repo, then:
python fitness_tracker.py
```

The app runs in your terminal. Follow the menu prompts to add, view, update, or delete workouts. Your data is saved automatically to `workout.txt` in the same folder.

**First run:** The file `workout.txt` will be created automatically if it doesn't exist.

---

## Project Structure

```
fitness-tracker/
├── fitness_tracker.py   # Main application — all logic and classes
└── workout.txt          # JSON data store (auto-generated on first run)
```

---

## What I Learned

This was my first substantial Python project, and it taught me several things I now use regularly:

- **OOP and inheritance** — designing a class hierarchy where `Running` and `Walking` extend a base `Workout` class, each with their own calorie calculation logic
- **File I/O with JSON** — reading and writing structured data so the app isn't stateless
- **Error handling** — validating user input and handling missing files gracefully
- **Separation of concerns** — keeping data classes separate from menu/display logic
- **`datetime` module** — auto-stamping each workout record with the current time

This project is what made object-oriented programming click for me. Before it, I understood the syntax; after it, I understood *why* you'd design code that way.

---

## Course Context

Built as **Coursework 1** for the Fundamentals of Python module. Graded project — full brief available in the PDF included in the original submission (not included here for brevity).
