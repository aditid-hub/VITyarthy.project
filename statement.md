# Smart Academic Planner & Load Calculator  
## Project Statement Document

## 📌 Problem Statement
Students often struggle to manage multiple academic responsibilities such as assignments, quizzes, exams, and projects.  
Common challenges include:
- Tracking deadlines across subjects  
- Estimating the time required for each task  
- Understanding which tasks carry higher workload  
- Prioritizing tasks effectively  
- Planning a structured study schedule  

Without a clear system, students experience stress, last-minute rush, and inconsistent productivity.  
There is a need for a **simple, rule-based** that helps students plan their academics efficiently.

---

## 📘 Scope of the Project
The scope of the **Smart Academic Planner** includes the following:

### **Included**
- User account creation and login  
- Adding tasks (assignments, quizzes, projects, exams, etc.)  
- Storing tasks using JSON  
- Load calculation using:
  - Task difficulty  
  - Estimated hours  
  - Deadline urgency  
- Categorizing load: Low, Moderate, High, Overload  
- Generating a daily study plan using logical rules  
- Exporting:
  - Tasks as CSV  
  - Study plan as PDF  
- Fully modular Python code

---

## 🎯 Target Users
The project is intended for:

- **College Students** managing multiple subjects & deadlines  
- **School Students** preparing for tests, assignments, and projects  
- **Learners in coaching institutes** planning study routines  
- **Anyone needing a structured academic planning tool**  

The tool is especially helpful for students handling high workload semesters.

---

## 🚀 High-Level Features

### **1. User Management**
- Register new users  
- Login using stored credentials  
- Separate data for each user  

### **2. Task Management**
- Add tasks with:
  - Name  
  - Course  
  - Difficulty  
  - Hours required  
  - Deadline  
  - Priority  
- View all tasks  
- Duplicate tasks  
- Delete tasks  

### **3. Load Calculation Engine**
- Rule-based calculation using:
  - Difficulty  
  - Hours required  
  - Days remaining  
- Classifies tasks into:
  - Low  
  - Moderate  
  - High  
  - Overload  

### **4. Study Plan Generator**
- Generates a multi-day plan based on available hours  
- Allocates tasks smartly using priority and urgency  
- Shows daily breakdown of work  

### **5. Report Generation**
- Export tasks as **CSV**  
- Export study plan as **PDF**  
- Stores files inside project directory  

---

