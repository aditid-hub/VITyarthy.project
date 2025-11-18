# Smart Academic Planner & Load Calculator

## 📌 Overview
The **Smart Academic Planner** is logic-based productivity tool built using **Python and Streamlit**.  
It helps students manage academic tasks, calculate study load, and generate an organized study plan based on deadlines, difficulty, and available study hours.

This project showcases **core Python concepts**:
- User management (Signup/Login)
- Data input & processing
- JSON-based data storage
- Modular programming
- File handling
- PDF & CSV generation
- UI development using Streamlit


---

## ⭐ Features
- 👤 **User Authentication** (Register/Login system)
- 📝 **Task Management**
  - Add tasks  
  - View all tasks  
  - Duplicate tasks  
  - Delete tasks  
- 📊 **Workload Calculation**
  - Uses difficulty, hours required, and deadline
  - Categorizes tasks into Low / Moderate / High / Overload
- 📅 **Smart Study Planner**
  - Logic-based plan generation  
  - Plans days based on available hours  
- 📤 **Export Options**
  - Export tasks as **CSV**
  - Export study plan as **PDF**
  - Export study plan as **JSON**  
- 🗂️ **Fully Modular Codebase**
  - `models/`, `core/`, `report/`, `utils/` packages

---

## 🛠 Technologies & Tools Used

-   Python 3
-   Streamlit
-   ReportLab
-   JSON
-   UUID
-   Datetime

## 🗂️ Folder Structure
 
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


## 🚀 Installation & Running the Project

### 1. Clone

    git clone
    cd academic-planner

### 2. Install Dependencies

    pip install streamlit reportlab

### 3. Run

    streamlit run app.py

## 🧪 Testing Instructions

-   Register & login\
-   Add tasks\
-   Manage tasks\
-   Generate plan\
-   Export CSV/PDF

## 👨‍💻 Author

Aditi Dubey\
VIT Bhopal
