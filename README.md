# CSE1021-Vityarthi-pythonproject
Digital Voting System 🗳️

A simple Digital Voting System made using Python.

This is a beginner-level Python project created to practice basic Python programming concepts and build a simple menu-driven application.

📌 About the Project

The Digital Voting System allows users to:

View available candidates

Cast a vote using a voter ID

Prevent the same voter ID from voting more than once

View live election results

Calculate the percentage of votes

Show the current leading candidate

Save election results to a text file

👥 Candidates

The project currently contains three candidates:

candidate-1

candidate-2

candidate-3

⚙️ Features

1. View Candidates

Displays the available candidates with their candidate numbers.

2. Cast a Vote

The user enters a voter ID and selects a candidate.

The program checks whether the voter ID has already been used. A voter ID can only be used once.

3. View Live Results

The program displays:

Votes received by each candidate

Percentage of votes

Total votes

Current leader

A simple # bar showing the number of votes

4. Save Results

The election results can be saved in:

voting_results.txt

The file contains the vote count, percentage, and total number of votes.

🛠️ Python Concepts Used

This project uses basic Python concepts such as:

Variables

Lists

Dictionaries

Functions

if-elif-else

for loop

while loop

User input

String formatting

Basic input validation

File handling

📂 Project Structure

Digital-Voting-System/

│
├── main.py

├── README.md

├── statement.md

├── voting_results.txt

└── Testing screenshots/
    └── Testing screenshots

Files and Folders

main.py — Main Python program

README.md — Project documentation

statement.md — Project statement and objectives

voting_results.txt — Saved voting results

Testing screenshots/ — Screenshots showing the program testing and output

▶️ How to Run

1. Install Python

Make sure Python 3 is installed on your computer.

Check the Python version:

python --version

2. Open the Project

Open the project folder in VS Code or a terminal.

3. Run the Program

python main.py

💻 Program Menu

When the program starts, it displays:

===== DIGITAL VOTING SYSTEM =====
1. View candidates
2. Cast a vote
3. View live results
4. Save results to file
5. Exit

🧪 Testing

Testing screenshots are available in the Testing screenshots folder of this repository.

The screenshots demonstrate different parts of the program, such as:

Main menu

Viewing candidates

Casting a vote

Duplicate vote prevention

Live results

Saving results to a file

📊 Example

Candidates:
  1. candidate-1
  2. candidate-2
  3. candidate-3

Enter the number of the candidate you want to vote for: 1

Vote recorded for candidate-1.
Thank you for voting!

Example results:

----- LIVE RESULTS -----

candidate-1 |   2 votes ( 50.0%) ##

candidate-2 |   1 votes ( 25.0%) #

candidate-3 |   1 votes ( 25.0%) #

Total votes cast: 4

Current leader: candidate-1

🎯 Learning Objective

The main objective of this project is to practice basic Python programming by creating a small practical application.

Through this project, I learned how to:

Use lists and dictionaries

Create and use functions

Take input from users

Use loops and conditions

Perform basic calculations

Validate user input

Save information into a text file

Create a menu-driven Python program

⚠️ Disclaimer

This project is made for educational purposes only.

It is a simple Python simulation and is not intended for use in real public elections.

👨‍💻 Author

Hardik Vivek Gupta

Reg no-26MEI10085

Integrated M.Tech — Cybersecurity

