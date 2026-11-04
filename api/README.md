# api

Python scripts that use a REST API (JSONPlaceholder) to read employee
TODO data and export it to different formats.

## Files

- 0-gather_data_from_an_API.py: prints an employee's TODO list progress
- 1-export_to_CSV.py: exports an employee's tasks to USER_ID.csv
- 2-export_to_JSON.py: exports an employee's tasks to USER_ID.json
- 3-dictionary_of_list_of_dictionaries.py: exports all employees' tasks
  to todo_all_employees.json

## Usage

    ./0-gather_data_from_an_API.py 2
    ./1-export_to_CSV.py 2
    ./2-export_to_JSON.py 2
    ./3-dictionary_of_list_of_dictionaries.py

Requires Python 3 (tested on 3.4.3). No extra packages are needed.
