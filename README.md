# Smart Academic Planner & Load Calculator

Overview
The **Smart Academic Planner** is a logic-based productivity tool built using **Python and Streamlit**.

It allows students to prioritize academic activities, estimate study load, and systematically generate a study plan according to the deadline, difficulty, and number of hours available for studying.
Projects highlighting the following **core Python concepts:
- User management (Signup/Login)
- Data input & processing
JSON-based data storage
- Modular programming
File handling


- Generating PDF & CSV

Streamlit-based UI development
---
Features ■
- **User Authentication** (Register/Login system)
-  **Task Management
- Adding tasks
- View all tasks
- Duplicate tasks
- Delete tasks
-  **Workload Calculation
Difficulty, hours required, deadline
Classification of activities as Low/ Moderate/ High / Overload
-  **Smart Study Planner**
- Logic-based plan generation
- Plans days based on available hours
-  **Export Options
- Export tasks as **CSV**
- Export study plan as **PDF**

- Export study plan as **JSON**

-**Fully Modular Codebase**

- `models/`, `core/`, `report/`, `utils/` packages
It is basically the application of management approaches to individual and organizational human resources in order to meet the needs of the firm and manage the workforce effectively.
## Technologies & Tools Used
Requirements
-   Python 3
- Streamlit

-   ReportLab
- JSON
- UUID
-   Datetime
Folder Structure
academic_planner/
│
├── app.py                    # Streamlit main file
├── models/
│   ├── user.py
│   ├── task.py
│   ├── course.py
│
├── core/
│   ├── load_engine.py
│   ├── planner.py
│   ├── validator.py
│
├── storage/
│   ├── users.json
│   ├── tasks.json
│   ├── courses.json
│
├── utils/
│   ├── file_handler.py
│   ├── date_utils.py


│

├── report/

│   └── generator.py

│

└── README.md

Installation & Running the Project

1. Clone

git clone

cd academic-planner
Install Dependencies
pip install streamlit reportlab
3. Execute

streamlit run app.py

Testing Instructions -   Register & login\. -   Add tasks; -   Manage tasks -   Create a plan - Export CSV/PDF 
## Author: Aditi Dubey
## Registration No. - 25BCE10906
