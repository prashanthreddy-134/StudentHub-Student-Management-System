


StudentHub — Student Management System
A practical Python internship project that demonstrates planning, database design, CRUD implementation, analytics, validation, testing considerations, and documentation in a real-world-style application.

Features
Dashboard with student count, average marks, pass count, active courses, and quick summary

Create, read, update, and delete student records

SQLite persistence (records remain after the app restarts)

Search by student ID, name, email, phone, or course

Input validation and duplicate-email protection

Academic analytics: students by course, marks distribution, pass rate

CSV export with a data preview

Responsive Streamlit layout with a custom dark interface

Technology Stack
Python 3.10+

Streamlit — application UI

SQLite — persistent relational database

Pandas — tabular data processing

Plotly — interactive charts

Project Structure
StudentHub/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── tests/
    └── test_validation.py
The SQLite database (studenthub.db) is created automatically when the app first runs. It is intentionally excluded from Git because it contains runtime data.

Setup
Windows (PowerShell)
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
If PowerShell blocks activation, run the app using:

.\.venv\Scripts\python.exe -m streamlit run app.py
Open the local URL printed by Streamlit, usually http://localhost:8501.

Database Design
Table: students

Column	Type	Rules
id	INTEGER	Primary key, auto-increment
full_name	TEXT	Required
email	TEXT	Required, unique, case-insensitive
phone	TEXT	Optional
course	TEXT	Required
marks	REAL	Required, between 0 and 100
created_at	TEXT	Record creation timestamp
updated_at	TEXT	Last update timestamp
All database writes use parameterized SQL statements. The database enforces uniqueness and marks constraints in addition to application-level validation.

Functional Requirements
The application shall create a student record with a name, email, course, marks, and optional phone.

The application shall display all student records and support text search.

The application shall update an existing student's details.

The application shall require explicit confirmation before deletion.

The dashboard shall calculate key student and academic metrics from stored records.

The analytics page shall visualize course counts and marks distribution.

The application shall export records as a UTF-8 CSV file.

Invalid input and duplicate email addresses shall produce understandable errors.

Architecture
The app is organized into three logical layers in one deployable Streamlit module:

Presentation: Streamlit pages, forms, navigation, metrics, tables, and charts.

Application logic: input validation and CRUD functions.

Persistence: SQLite connection and parameterized SQL operations.

For a larger production system, these layers can be separated into modules and authentication, authorization, audit logging, migrations, and automated deployment can be added.

Testing Checklist
Add a valid student and verify that the record appears on the dashboard and records page.

Try an invalid email and verify that the record is rejected.

Add the same email twice (including different letter casing) and verify duplicate protection.

Try marks below 0 or above 100 and verify the input is constrained.

Search using a name, email, course, phone, and student ID.

Update a record and verify that the changes persist after refreshing.

Attempt deletion without checking confirmation; verify deletion is disabled.

Confirm deletion and verify that the record disappears.

Test analytics with no records, one record, and multiple records.

Export CSV and open it to verify headers and values.

Stop and restart Streamlit; verify records remain in SQLite.

Run the included validation tests with:

python -m unittest discover -s tests -v
Known Scope / Limitations
This is a local internship project, not a production student information system.

There is no login or role-based access control.

Phone numbers are stored as text to preserve leading zeros and optional formatting.

The pass threshold is currently set to 40 marks and can be changed in app.py.

The app does not include attendance, fees, or assignment workflows.

GitHub
Create an empty GitHub repository named StudentHub-Student-Management-System, then run these commands from this project folder:

git init
git add .
git commit -m "Build StudentHub practical implementation project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/StudentHub-Student-Management-System.git
git push -u origin main
Replace YOUR-USERNAME with your GitHub username. Do not commit .venv/, studenthub.db, secrets, or personal student data.

Project Presentation
Suggested demo flow:

Explain the problem and the project objectives.

Show the dashboard and database-backed records.

Register a student, search for the record, and update it.

Demonstrate the deletion confirmation.

Show course and marks analytics.

Export a CSV and explain the SQLite schema.

Discuss validation, edge cases, and future improvements.