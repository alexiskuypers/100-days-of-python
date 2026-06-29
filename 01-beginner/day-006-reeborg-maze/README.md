# Day 6 — Reeborg's Maze

A maze-solving challenge completed in Reeborg's World as part of the *100 Days of Code: Python* course.

## Challenge

The goal is to guide Reeborg through a maze and reach the exit.

The robot starts at an unknown position and must make decisions based on the walls around it. The solution uses conditional logic and a loop to continue moving until the goal is reached.

## Try the game

Open the official challenge in your browser:

[Play Reeborg's Maze](https://reeborg.ca/reeborg.html?lang=en&menu=worlds%2Fmenus%2Freeborg_intro_en.json&mode=python&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)

Copy the code from the project file into the Reeborg's World editor, then run the program.

## How the game works

Reeborg can:

* move forward;
* turn left;
* detect whether the path ahead is clear;
* detect whether the path to the right is clear;
* detect whether it has reached the goal.

These commands are provided by Reeborg's World.

The program combines them to decide which direction the robot should take at each step.

## Concepts practised

* Defining and calling functions
* `while` loops
* `if`, `elif`, and `else`
* Logical conditions
* Code indentation
* Problem-solving with repeated decisions

## Project files

```text
day-006-reeborg-maze/
├── README.md
└── maze.py
```

## Note

This project uses functions provided by the Reeborg's World environment. It is intended to be executed in the browser-based game rather than directly with the standard Python interpreter.
