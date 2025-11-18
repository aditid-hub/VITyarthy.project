import streamlit as st
from models.user import create_user, verify_user
from models.task import new_task_dict, load_tasks, save_task, delete_task
from core.load_engine import calculate_load_factor, classify_load
from core.planner import generate_daily_plan
from report.generator import export_tasks_csv
import os
import io
import json
from fpdf import FPDF

st.set_page_config(page_title="Smart Academic Planner", layout="wide")

# ------------------------
# SESSION MANAGEMENT
# ------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "plan" not in st.session_state:
    st.session_state.plan = None


# ------------------------
# LOGIN PAGE
# ------------------------
def login_view():
    st.title("Smart Academic Planner — Login / Register")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Login")
        uname = st.text_input("Username", key="login_user")
        pwd = st.text_input("Password", type="password", key="login_pwd")

        if st.button("Login"):
            if verify_user(uname, pwd):
                st.session_state.logged_in = True
                st.session_state.username = uname
                st.success(f"Logged in as {uname}")
                st.rerun()
            else:
                st.error("Invalid credentials")

    with col2:
        st.subheader("Register")
        r_uname = st.text_input("New Username", key="reg_user")
        r_pwd = st.text_input("New Password", type="password", key="reg_pwd")

        if st.button("Register"):
            if create_user(r_uname, r_pwd):
                st.success("User created successfully. Please login.")
                st.rerun()
            else:
                st.error("Username already exists")


# ------------------------
# DASHBOARD VIEW
# ------------------------
def dashboard_view():

    username = st.session_state.username
    st.sidebar.title(f"Welcome, {username}")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.plan = None
        st.rerun()

    menu = st.sidebar.radio("Menu", ["Dashboard", "Add Task", "All Tasks", "Planner & Reports"])

    st.title("Smart Academic Planner & Load Calculator")

    # --------------------
    # DASHBOARD PAGE
    # --------------------
    if menu == "Dashboard":
        st.header("Dashboard Overview")
        tasks = load_tasks(username)

        if not tasks:
            st.info("No tasks yet. Add new tasks from 'Add Task'.")
        else:
            for t in tasks:
                t["load_factor"] = calculate_load_factor(
                    t["difficulty"], t["hours_required"], t["deadline"]
                )
                t["status"] = classify_load(t["load_factor"])

            st.subheader("Task Overview")
            st.table(tasks)

            st.subheader("Load Summary")
            st.write(f"🟢 Low Load: **{len([t for t in tasks if t['status']=='Low'])}**")
            st.write(f"🟡 Moderate Load: **{len([t for t in tasks if t['status']=='Moderate'])}**")
            st.write(f"🟠 High Load: **{len([t for t in tasks if t['status']=='High'])}**")
            st.write(f"🔴 Overload: **{len([t for t in tasks if t['status']=='Overload'])}**")

    # --------------------
    # ADD TASK PAGE
    # --------------------
    elif menu == "Add Task":
        st.header("Add New Task")

        with st.form("task_form"):
            name = st.text_input("Task Name")
            course = st.text_input("Course Name")
            task_type = st.selectbox("Task Type", ["Assignment", "Quiz", "Exam", "Project", "Other"])
            difficulty = st.slider("Difficulty (1 easy → 5 hard)", 1, 5, 3)
            hours_required = st.number_input("Estimated Hours", min_value=0.5, step=0.5)
            deadline = st.date_input("Deadline")
            priority = st.slider("Priority (1 high → 5 low)", 1, 5, 3)

            sub = st.form_submit_button("Add Task")

            if sub:
                if not name.strip():
                    st.error("Task name cannot be empty.")
                else:
                    task = new_task_dict(
                        name=name,
                        course=course or "General",
                        task_type=task_type,
                        difficulty=difficulty,
                        hours_required=hours_required,
                        deadline=str(deadline),
                        priority=priority,
                        owner=username
                    )
                    save_task(task)
                    st.success("Task added successfully!")
                    # st.rerun()

    # --------------------
    # ALL TASKS PAGE
    # --------------------
    elif menu == "All Tasks":
        st.header("Your Tasks")
        tasks = load_tasks(username)

        if not tasks:
            st.info("No tasks available.")
        else:
            for t in tasks:
                t["load_factor"] = calculate_load_factor(
                    t["difficulty"], t["hours_required"], t["deadline"]
                )
                t["status"] = classify_load(t["load_factor"])

            st.table(tasks)

            st.subheader("Manage Tasks")

            for t in tasks:
                with st.expander(f"{t['name']} — Due: {t['deadline']}"):
                    col1, col2 = st.columns(2)

                    if col1.button("Delete", key=f"del_{t['id']}"):
                        delete_task(t["id"])
                        st.success("Task deleted.")
                        st.rerun()

                    if col2.button("Duplicate", key=f"dup_{t['id']}"):
                        dup = new_task_dict(
                            name=t["name"] + " (copy)",
                            course=t["course"],
                            task_type=t["task_type"],
                            difficulty=t["difficulty"],
                            hours_required=t["hours_required"],
                            deadline=t["deadline"],
                            priority=t["priority"],
                            owner=username,
                        )
                        save_task(dup)
                        st.success("Task duplicated!")
                        st.rerun()

    # --------------------
    # PLANNER & REPORTS
    # --------------------
    elif menu == "Planner & Reports":
        st.header("Study Planner & Reports")

        tasks = load_tasks(username)

        if not tasks:
            st.info("Add tasks first!")
            return

        daily_hours = st.number_input("Daily Study Hours", min_value=1.0, max_value=24.0, value=4.0)
        days_span = st.number_input("Generate Plan For (Days)", min_value=1, max_value=60, value=14)

        if st.button("Generate Plan"):
            st.session_state.plan = generate_daily_plan(tasks, daily_hours, days_span)
            st.success("Study Plan Generated!")
            st.rerun()

        if st.session_state.plan:
            st.subheader("Generated Plan")

            for day in st.session_state.plan:
                st.write(f"### 📅 {day['date']} — Remaining Hours: {day['available_hours']}")
                st.table(day["slots"] if day["slots"] else [])

            st.subheader("Export Options")

            if st.button("Export Tasks CSV"):
                path = os.path.join("storage", f"tasks_{username}.csv")
                export_tasks_csv(tasks, path)
                st.success(f"Tasks exported to: {path}")

            # -------------------------
            # DOWNLOAD PDF (FPDF)
            # -------------------------
            if st.button("Download Study Plan (PDF)"):

                pdf = FPDF()
                pdf.set_auto_page_break(auto=True, margin=15)
                pdf.add_page()

                pdf.set_font("Arial", "B", 16)
                pdf.cell(0, 10, f"Study Plan for {username}", ln=True)

                pdf.ln(5)
                pdf.set_font("Arial", size=12)

                for day in st.session_state.plan:
                    pdf.set_font("Arial", "B", 14)
                    pdf.cell(0, 10, f"{day['date']} (Remaining Hours: {day['available_hours']})", ln=True)

                    pdf.set_font("Arial", size=12)

                    if not day["slots"]:
                        pdf.cell(0, 8, " - No study assigned", ln=True)
                    else:
                        for slot in day["slots"]:

                            task_name = (
                                slot.get("task_name")
                                or slot.get("name")
                                or slot.get("task")
                                or "Unnamed Task"
                            )
                            hours = slot.get("hours", "?")

                            pdf.cell(0, 8, f" - {task_name} ({hours} hr)", ln=True)

                    pdf.ln(3)

                pdf_bytes = pdf.output(dest="S").encode("latin-1")

                st.download_button(
                    label="📄 Download PDF",
                    data=pdf_bytes,
                    file_name=f"study_plan_{username}.pdf",
                    mime="application/pdf"
                )

            # -------------------------
            # DOWNLOAD JSON
            # -------------------------
            plan_json = json.dumps(st.session_state.plan, indent=4)

            st.download_button(
                label="📥 Download Study Plan (JSON)",
                data=plan_json,
                file_name=f"study_plan_{username}.json",
                mime="application/json"
            )


# ------------------------
# RUN
# ------------------------
if not st.session_state.logged_in:
    login_view()
else:
    dashboard_view()
