# priority-queue-task-manager

## Overview
This is a Command-Line Interface (CLI) Task Manager application built in Python.  
It allows users to manage tasks with priorities, enabling them to add, view, delete, and save tasks efficiently.

## Features
- Add tasks with a numeric priority (higher number means higher priority)  
- View all tasks sorted by priority  
- Delete tasks by selecting the task number  
- Save tasks to a JSON file (`tasks.json`) and load them on startup  
- Handles input validation and error cases gracefully  

## Technologies Used
- Python 3  
- `heapq` module for implementing priority queue
- `json` module for file persistence  
