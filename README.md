The Smart Academic Planner serves as a logic-based productivity tool. It uses Python and Streamlit to help students. Students can manage academic tasks with it. They calculate study load and generate organized plans. These plans come from deadlines, difficulty levels, and available study hours.

This project highlights core Python concepts. It includes user management for signup and login. Data input and processing play a big role. JSON handles data storage. Modular programming keeps things organized. File handling supports various operations. PDF and CSV generation adds export features. UI development relies on Streamlit for the interface.

Features stand out in several ways. User authentication handles register and login systems. Task management lets users add tasks. They view all tasks easily. Duplicating tasks saves time. Deleting tasks keeps lists clean.

Workload calculation uses difficulty ratings, required hours, and deadlines. It categorizes tasks into low, moderate, high, or overload levels.

The smart study planner generates logic-based plans. It schedules days according to available hours.

Export options include tasks as CSV files. Study plans export as PDF or JSON formats.

The codebase remains fully modular. Packages like models, core, report, and utils structure the code neatly.

Technologies and tools include Python 3 as the base. Streamlit builds the app. ReportLab creates PDFs. JSON manages data. UUID generates unique identifiers. Datetime handles time-related functions.

The folder structure starts with academic_planner as the main directory. It contains app.py as the Streamlit main file. The models folder holds user.py, task.py, and course.py. Core includes load_engine.py, planner.py, and validator.py. Storage has users.json, tasks.json, and courses.json. Utils covers file_handler.py and date_utils.py. Report contains generator.py. README.md sits at the root.

Installation and running the project follow simple steps. First, clone the repository with git clone. Then change directory to academic-planner.

Next, install dependencies using pip install streamlit reportlab.

To run it, use streamlit run app.py.

Testing instructions involve registering and logging in. Add tasks to start. Manage tasks as needed. Generate a plan afterward. Export in CSV or PDF format.

The author is Aditi Dubey from VIT Bhopal.
