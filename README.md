# Student Management System

A Python-based Student Management System built using Streamlit and SQLite. The application provides a simple web interface to manage student records and perform essential student management operations.

## Project Overview

The Student Management System is designed to simplify student record management through a user-friendly web application. It uses Python for application logic, Streamlit for the frontend, and SQLite for database storage.

The project also includes automated testing to verify database operations and support software quality assurance.

## Features

- Add and manage student records.
- View student information.
- Store student data using SQLite.
- Interactive web interface built with Streamlit.
- Persistent database storage.
- Automated testing using pytest.
- Modular application structure.
- Local deployment.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web interface |
| SQLite | Database management |
| Pandas | Data processing |
| Pytest | Automated testing |
| Git | Version control |
| GitHub | Source code hosting |

## Project Structure

```text
Student_Management_System/
│
├── app.py
├── database.py
├── students.db
├── test_student.py
├── requirements.txt
├── README.md
├── .gitignore
└── .venv/
```

**File descriptions:**

- `app.py` — Main Streamlit application.
- `database.py` — Database connection and student data operations.
- `students.db` — SQLite database containing student records.
- `test_student.py` — Automated tests for the project.
- `requirements.txt` — Python dependencies.
- `README.md` — Project documentation.
- `.gitignore` — Files and directories excluded from Git.

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Student_Management_System
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux / Ubuntu:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python -m streamlit run app.py
```

Open the following URL in your browser:

```text
http://localhost:8501
```

## Testing and Quality Assurance

The project includes automated testing using pytest to verify application functionality and database operations.

### Testing Framework

- **Framework:** Pytest
- **Test file:** `test_student.py`
- **Purpose:** Verify application and database functionality.
- **Testing approach:** Automated unit testing.

### Run the tests

Install pytest if it is not already installed:

```bash
python -m pip install pytest
```

Run the test suite:

```bash
python -m pytest -v
```

### Testing Results

Test execution results should be recorded after running the test suite.

| Testing Activity | Status |
|---|---|
| Test file created | Completed |
| Automated test execution | Run using pytest |
| Test results | Update after execution |
| Application testing | Verify locally |
| Database testing | Verify using automated tests |

**Note:** Update this section with the actual number of tests passed, failed, or skipped after executing the test suite.

## Software Quality Assurance

The project follows basic software quality assurance practices:

1. **Functional Testing:** Verify that the application performs its intended student management operations.
2. **Database Testing:** Check database operations and student record handling.
3. **Automated Testing:** Use pytest to execute repeatable tests.
4. **Code Organization:** Separate application logic and database operations into different Python files.
5. **Version Control:** Use Git to track changes and GitHub to maintain the project repository.
6. **Documentation:** Maintain installation, execution, and testing instructions in this README.

## Version Control and GitHub

Git is used to manage project versions and track source code changes. GitHub is used to host the project and maintain its development history.

To upload the latest changes:

```bash
git add app.py database.py test_student.py requirements.txt README.md .gitignore
git commit -m "Update testing and project documentation"
git push origin main
```

## Running the Project in Ubuntu (WSL)

The project can also be executed using Windows Subsystem for Linux (WSL).

```bash
cd ~/Student_Management_System
source .venv/bin/activate
python3 -m streamlit run app.py
```

Open the application at:

```text
http://localhost:8501
```

## Learning Outcomes

This project provides practical experience in:

- Python application development.
- Building interactive web applications with Streamlit.
- Database integration using SQLite.
- Writing automated tests using pytest.
- Managing project dependencies.
- Applying basic software testing and quality assurance practices.
- Using Git and GitHub for version control and project submission.

## Future Enhancements

- Add student search and filtering.
- Introduce role-based authentication.
- Add student attendance management.
- Generate student reports.
- Improve input validation and error handling.
- Expand automated test coverage.

## Author

**Prashanth Reddy S**

Information Science and Engineering Student  
Brindavan College of Engineering, Bengaluru

## License

This project is developed for educational and internship purposes.