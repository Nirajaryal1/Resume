import os

from flask import Flask, send_file, make_response
from fpdf import FPDF

app = Flask(__name__)

class PDF(FPDF):
    def header(self):
        # No header on every page for a resume usually, but we can add space
        pass

    def footer(self):
        # No footer needed for this style
        pass

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_text_color(0, 0, 0)
        self.cell(0, 6, title.upper(), 0, 1, 'L')
        self.line(10, self.get_y(), 200, self.get_y()) # Horizontal line
        self.ln(2)

    def chapter_body(self, body):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 5, body)
        self.ln()

    def add_bullet(self, text):
        self.set_font('Arial', '', 10)
        # Bullet char is chr(149) or just a standard bullet
        self.cell(5) # Indent
        self.multi_cell(0, 5, f"{chr(149)} {text}")
        
    def add_job_header(self, company, location, role, dates):
        self.set_font('Arial', 'B', 10)
        self.cell(0, 5, f"{company} | {location}", 0, 1)
        self.set_font('Arial', 'BI', 10) # Bold Italic for Role
        self.cell(140, 5, role)
        self.set_font('Arial', '', 10)
        self.cell(0, 5, dates, 0, 1, 'R')
        self.ln(1)

@app.route("/")
def index():
    return send_file('src/index.html')

@app.route("/resume")
def generate_resume():
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # --- HEADER ---
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(0, 10, 'NIRAJ ARYAL', 0, 1, 'C')
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 5, 'Palo Alto, CA | [Insert Tesla Email]@tesla.com | [Insert Personal Phone] | [Insert LinkedIn URL]', 0, 1, 'C')
    pdf.ln(5)

    # --- SUMMARY ---
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 6, 'PROJECT COORDINATOR & OPERATIONS SPECIALIST', 0, 1, 'C')
    pdf.set_font('Arial', 'I', 10)
    pdf.cell(0, 5, 'Internal Tesla Candidate | Operations & Technical Execution', 0, 1, 'C')
    pdf.ln(3)

    pdf.set_font('Arial', '', 10)
    pdf.multi_cell(0, 5, "Tesla-internal operations professional with a bias for action and a track record of connecting engineering requirements with operational execution. Currently supporting Robotics R&D programs, ensuring high-fidelity data collection and hardware testing integrity. Combines hands-on Tesla operational experience with technical project management skills (Python, SQL, AI/ML) demonstrated through founding and shipping two AI-driven platforms.")
    pdf.ln(5)

    # --- TESLA EXPERIENCE ---
    pdf.chapter_title('TESLA EXPERIENCE')

    pdf.add_job_header('TESLA', 'Palo Alto, CA', 'Data Collection Operator - Robotics Programs', 'Feb 2025 - Present')
    pdf.set_font('Arial', 'I', 10)
    pdf.multi_cell(0, 5, "Execution-focused role supporting R&D engineering through rigorous hardware testing and data pipeline management.")
    pdf.ln(1)

    pdf.add_bullet("R&D Project Execution: Execute complex robotic testing scenarios to support critical engineering milestones. Act as the bridge between abstract engineering requirements and physical real-world data collection.")
    pdf.add_bullet("Cross-Functional Coordination: Coordinate daily testing schedules across engineering, data, and operations teams to maximize hardware utilization and data throughput.")
    pdf.add_bullet("Risk & Issue Mitigation: Identify, document, and escalate hardware anomalies and software bugs in real-time to engineering, significantly reducing downtime and accelerating the iteration loop.")
    pdf.add_bullet("Process Improvement: Refined data logging protocols and operational SOPs, improving data quality consistency and reducing the need for re-runs.")
    pdf.add_bullet("Technical Feedback Loop: Provide qualitative and quantitative feedback to technical teams regarding hardware performance, directly influencing engineering adjustments.")
    pdf.ln(3)

    # --- PROJECT LEADERSHIP ---
    pdf.chapter_title('PROJECT & TECHNICAL LEADERSHIP')

    pdf.add_job_header('BAgentAI', 'Remote', 'Founder & Project Lead', '2025 - Present')
    pdf.add_bullet("End-to-End Project Management: Scoped business requirements, defined technical deliverables, and managed the full lifecycle of implementation for AI-driven workflow automation.")
    pdf.add_bullet("Stakeholder Management: Translated complex technical concepts (AI Agents, automation scripts) into clear value propositions for non-technical stakeholders.")
    pdf.add_bullet("System Implementation: Deployed automated workflows using Python and AI logic to replace manual data entry tasks, resulting in measurable time savings for clients.")
    pdf.ln(2)

    pdf.add_job_header('NepInBay', 'Remote', 'Product & Project Owner', '2025 - Present')
    pdf.add_bullet("Product Roadmap Ownership: Defined the Minimum Viable Product (MVP) scope, prioritized feature backlog, and managed the development timeline from concept to live deployment.")
    pdf.add_bullet("Technical Coordination: Orchestrated the build of data pipelines, submission workflows, and map-based search integrations (Google Maps API).")
    pdf.ln(2)

    pdf.add_job_header('VoiceJournal App', 'Remote', 'Project Owner', '2025')
    pdf.add_bullet("Scope & Delivery: Managed the development of an AI-powered journaling MVP, coordinating the integration of UI, backend logic, and cloud storage.")
    pdf.ln(3)

    # --- OPERATIONS EXPERIENCE ---
    pdf.chapter_title('OPERATIONS MANAGEMENT')

    pdf.add_job_header("YANCEY'S FANCY", 'Operations Lead', 'Production', 'Jul 2023 - Jul 2024')
    pdf.add_bullet("Production Leadership: Led daily production floor operations, managing schedules and resource allocation to meet strict output targets.")
    pdf.add_bullet("Workflow Optimization: Identified bottlenecks in the packaging line and implemented process adjustments to improve throughput.")
    pdf.ln(2)

    pdf.add_job_header("A&A RESTAURANT GROUP", 'HR & Operations Coordinator', '', 'May 2018 - Jun 2023')
    pdf.add_bullet("Multi-Site Coordination: Managed hiring, onboarding, and compliance logistics across multiple locations, ensuring operational readiness.")
    pdf.ln(3)

    # --- SKILLS ---
    pdf.chapter_title('SKILLS & TOOLS')
    pdf.set_font('Arial', '', 10)
    pdf.multi_cell(0, 5, "Project Management: Project Coordination, Agile/Waterfall, Risk Assessment, Stakeholder Communication, SOP Development.")
    pdf.multi_cell(0, 5, "Technical: Python, SQL, Pandas, Data Collection & Labeling, QA/Testing, Workflow Automation.")
    pdf.multi_cell(0, 5, "Tools: Workday, JIRA (familiarity), Tableau, Excel (Advanced), Notion, Firebase, Google Maps API.")
    pdf.ln(3)

    # --- EDUCATION ---
    pdf.chapter_title('EDUCATION & CERTIFICATIONS')
    pdf.add_job_header('Project Management Certificate', 'Florida A&M University (In Progress)', 'Focus: PMP methodologies, Agile execution', '')
    pdf.ln(1)
    pdf.add_job_header('AI Agents Intensive', 'Google x Kaggle', 'Issued Dec 2025', '')
    pdf.ln(1)
    pdf.add_job_header('B.S. Business Administration', 'San Francisco State University', 'Minor in Information Systems', '2023')

    # Generate PDF in memory
    pdf_data = pdf.output(dest='S').encode('latin-1')
    
    response = make_response(pdf_data)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=Niraj_Aryal_Tesla_Resume.pdf'
    
    return response

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
