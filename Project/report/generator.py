import csv
from fpdf import FPDF
from datetime import datetime

def export_tasks_csv(tasks, filepath):
    keys = ["id","name","course","task_type","difficulty","hours_required","deadline","priority","owner"]
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for t in tasks:
            writer.writerow({k: t.get(k, "") for k in keys})

def generate_plan_pdf(plan, username, filepath):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 8, f"Study Plan for: {username}", ln=True)
    pdf.cell(0, 6, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True)
    pdf.ln(4)
    for day in plan:
        pdf.set_font("Arial", "B", 11)
        pdf.cell(0, 7, day["date"], ln=True)
        if not day["slots"]:
            pdf.set_font("Arial", size=10)
            pdf.cell(0, 6, "  No allocation", ln=True)
        else:
            for s in day["slots"]:
                pdf.set_font("Arial", size=10)
                line = f"  {s['hours']}h - {s['task_name']} ({s['course']})"
                pdf.cell(0, 6, line, ln=True)
        pdf.ln(2)
    pdf.output(filepath)
