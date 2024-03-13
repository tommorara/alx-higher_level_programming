# 0x0D. SQL - Introduction

This project, "0x0D. SQL - Introduction," is focused on introducing the fundamentals of SQL and MySQL. Guided by Guillaume, this project aims to equip participants with the knowledge and skills necessary to manage and manipulate databases effectively. Scheduled to start on March 12, 2024, and conclude by March 13, 2024, this project is an essential step for anyone looking to excel in database management.

## Concepts

Participants will delve into key concepts such as:
- Databases
- Relational Databases

## Resources

To excel in this project, the following resources are recommended:
- [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
- [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial)
- [Basic SQL statements: DDL and DML](https://www.sqlshack.com/basic-sql-ddl-dml-commands-examples/) (excluding the "Privileges" chapter)
- [Basic queries: SQL and RA](http://www.mathcs.emory.edu/~cheung/Courses/377/Syllabus/8-RelAlg/SQL-RA.html)
- [SQL technique: functions](https://www.w3schools.com/sql/sql_functions.asp)
- [SQL technique: subqueries](https://www.w3schools.com/sql/sql_subqueries.asp)
- [What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/11321491/when-to-use-single-quotes-double-quotes-and-backticks-in-mysql)
- [MySQL Cheat Sheet](https://websitesetup.org/wp-content/uploads/2019/09/MySQL-Cheat-Sheet.pdf)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-syntax.html)
- [Installing MySQL in Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)

## Learning Objectives

By the end of this project, participants will be able to:

- Understand what a database and a relational database are.
- Explain what SQL stands for and the purpose of MySQL.
- Create a database in MySQL.
- Understand what DDL (Data Definition Language) and DML (Data Manipulation Language) stand for.
- Create or alter a table using SQL.
- Select data from a table.
- Insert, update, or delete data in a database.
- Use subqueries in SQL.
- Utilize MySQL functions effectively.

## Copyright - Plagiarism

- Participants are encouraged to find solutions independently to meet the learning objectives.
- Copying and pasting someone else’s work will not help in achieving the learning outcomes and is strictly prohibited.
- Publishing any content from this project is not allowed.
- Plagiarism will lead to removal from the program.

## General Requirements

- Use `vi`, `vim`, or `emacs` as your text editor.
- Execute all files on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25).
- Ensure all files end with a new line.
- Include a comment before each SQL query describing its purpose.
- Begin all files with a comment that describes the task.
- Use uppercase for all SQL keywords (e.g., SELECT, WHERE).
- A `README.md` file at the root of the project folder is mandatory.
- The length of your files will be tested using `wc`.

## More Info

### Comments for your SQL file example:

```sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;

