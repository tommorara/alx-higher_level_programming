# 0x0F. Python - Object-relational mapping

## Overview

This project explores database interaction with Python using `MySQLdb` for direct SQL and `SQLAlchemy` for ORM. It covers connecting, querying, and manipulating data in MySQL using both approaches. The goal is to understand ORM benefits like abstraction and database independence.

## Objectives

You'll learn to:

*   Connect to MySQL with Python.
*   Execute SQL queries using `MySQLdb`.
*   Use SQLAlchemy for object-relational mapping.
*   Map Python classes to database tables.
*   Create and use Python virtual environments.

## Project Details

*   **Language:** Python
*   **Topics:** OOP, SQL, MySQL, ORM, SQLAlchemy
*   **Start Date:** Dec 19, 2024
*   **End Date:** Jan 7, 2025
*   **Auto Review:** At deadline

## Setup

*   MySQL server on version 8.0.
*   Install `python3.8-venv`, `mysqlclient`, `SQLAlchemy`.
*   Create a virtual environment and install dependencies.

## Tasks

### MySQLdb Tasks

*   **0. Get all states:** List all states from `hbtn_0e_0_usa`.
*   **1. Filter states:** List states starting with "N".
*   **2. Filter states by input:** List states matching user input (SQL vulnerable).
*   **3. Safe filter states:** List states matching input, SQL injection safe.
*   **4. Cities by states:** List all cities from `hbtn_0e_4_usa`.
*   **5. All cities by state:** List cities for a given state.

### SQLAlchemy Tasks

*   **6. First state model:** Define `State` class mapping to `states` table.
*   **7. All states via SQLAlchemy:** List all `State` objects from `hbtn_0e_6_usa`.
*   **8. First state:** Print the first `State` object.
*   **9. Contains `a`:** List `State` objects containing 'a'.
*   **10. Get a state:** Print a `State` object by name.
*   **11. Add a new state:** Add "Louisiana" and print its ID.
*   **12. Update a state:** Update state with `id = 2` to "New Mexico".
*   **13. Delete states:** Delete `State` objects with names containing 'a'.
*   **14. Cities in state:** Define `City` class, list cities with state names.

## General Requirements

*   Use specified editors (vi, vim, emacs).
*   Ubuntu 20.04 LTS.
*   Python 3.8.5.
*   `mysqlclient` 2.0.x, `SQLAlchemy` 1.4.x.
*   Files end with newline, start with `#!/usr/bin/python3`.
*   README.md mandatory.
*   pycodestyle for code style.
*   All files must be executable.
*   Comprehensive docstrings for modules, classes, and functions.
*   No direct `execute` with sqlalchemy.

