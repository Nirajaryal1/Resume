from fpdf import FPDF

class ResumePDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 15)
        self.cell(0, 6, 'NIRAJ ARYAL', 0, 1, 'C')
        self.set_font('Helvetica', '', 9.5)
        self.cell(0, 4, 'Palo Alto, CA | 650-619-8773 | aryalniraj1@gmail.com | linkedin.com/in/aryalniraj1', 0, 1, 'C')
        self.ln(3)

    def section_title(self, title):
        self.set_font('Helvetica', 'B', 10)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 5, title, 0, 1, 'L', fill=True)
        self.ln(1)

    def bullet_point(self, text):
        self.set_font('Helvetica', '', 9.5)
        self.cell(3)
        self.multi_cell(0, 4.2, chr(149) + " " + text)

    def job_header(self, company_loc, title, date):
        self.set_font('Helvetica', 'B', 10)
        self.cell(140, 4.5, company_loc, 0, 0, 'L')
        self.set_font('Helvetica', 'B', 9.5)
        self.cell(0, 4.5, date, 0, 1, 'R')
        self.set_font('Helvetica', 'I', 9.5)
        self.cell(0, 4.5, title, 0, 1, 'L')

def generate_resume():
    pdf = ResumePDF()
    # Adjusted margins to fit everything elegantly onto 1 page
    pdf.set_margins(12, 10, 12)
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.add_page()

    # Professional Title & Summary
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(0, 5, 'OPERATIONS, HR & PROJECT MANAGEMENT PROFESSIONAL', 0, 1, 'C')
    pdf.ln(1)
    pdf.set_font('Helvetica', '', 9.5)
    pdf.multi_cell(0, 4.2, "Versatile professional with a strong foundation in operations, human resources, and project management, currently executing complex R&D projects at Tesla. Combines hands-on experience in workforce planning, process optimization, and cross-functional coordination with a proven ability to drive project milestones. Passionate about leveraging automation, AI agents, and data-driven insights to enhance operational efficiency, ensure compliance, and boost employee engagement.")
    pdf.ln(3)

    # Core Competencies & Skills
    pdf.section_title('CORE COMPETENCIES & SKILLS')
    
    competencies = [
        ('Operations & Proj Mgt:', 'Stakeholder Communication, Risk Assessment, Agile & Waterfall, Scope Mgt, SOP Development, Resource Allocation'),
        ('HR & Workforce Mgt:', 'Full-Cycle Recruitment, Onboarding & Retention, Payroll Processing, Employee Relations, Labor Law Compliance'),
        ('Technical & AI Tools:', 'Python, SQL, Pandas, Workflow Automation, JIRA, Notion, Tableau, AI Agent Development, React, Firebase')
    ]

    for label, desc in competencies:
        pdf.set_font('Helvetica', 'B', 9.5)
        pdf.cell(42, 4.5, label)
        pdf.set_font('Helvetica', '', 9.5)
        pdf.multi_cell(0, 4.5, desc)
    pdf.ln(2)

    # Experience
    pdf.section_title('PROFESSIONAL EXPERIENCE')

    # Tesla
    pdf.job_header('TESLA, Palo Alto, CA', 'Data Collection Specialist - Optimus', 'Feb 2025 - Present')
    pdf.bullet_point('Coordinated and executed complex robotic testing scenarios, acting as the key liaison between R&D engineering and operational teams to meet project deadlines.')
    pdf.bullet_point('Managed daily testing schedules and resources, maximizing hardware utilization and data throughput to accelerate engineering milestones.')
    pdf.bullet_point('Identified and escalated hardware and software risks in real-time, improving the engineering feedback loop and reducing project downtime.')
    pdf.ln(2)

    # Yancey's Fancy
    pdf.job_header("YANCEY'S FANCY, Corfu, NY", 'Operations Lead', 'Jul 2022 - Jul 2024')
    pdf.bullet_point('Directed daily production floor operations, managing schedules and allocating resources to consistently meet output targets.')
    pdf.bullet_point('Analyzed and optimized packaging line workflows, identifying and resolving bottlenecks to improve overall throughput.')
    pdf.bullet_point('Implemented standard operating procedures (SOPs) and cross-training initiatives, enhancing team versatility and reducing operational downtime.')
    pdf.ln(2)

    # A&A Restaurant Group
    pdf.job_header('A&A RESTAURANT GROUP, San Francisco, CA', 'HR Coordinator', 'May 2018 - Jun 2022')
    pdf.bullet_point('Administered full-cycle recruitment, payroll processing, and compliance documentation across multiple locations in accordance with federal and state labor laws.')
    pdf.bullet_point('Developed and enhanced onboarding programs and employee engagement initiatives, improving retention and workforce satisfaction across teams.')
    pdf.ln(3)

    # Projects
    pdf.section_title('PROJECTS')

    # Tesla Tee Time
    pdf.job_header('TESLA TEE TIME, Palo Alto, CA', 'Founder & Project Lead', '2025 - Present')
    pdf.bullet_point('Developed an AI-powered agent tailored for Tesla employees, providing personalized golf course recommendations based on office locations, after-work schedules, team outings, and EV charging needs.')
    pdf.bullet_point('Curated a comprehensive knowledge base with 14 Bay Area courses, Tesla office details, and attributes (e.g., twilight rates, difficulty levels, Supercharger proximity), enabling use cases like quick 9-hole rounds and corporate event planning.')
    pdf.bullet_point('Impact: Enhances employee engagement; structured for easy expansion to other regions or activities.')
    pdf.ln(2)

    # Nepinbay
    pdf.job_header('NEPINBAY, CA', 'Founder & Developer', '2024 - Present')
    pdf.bullet_point('Designed and launched a community web platform to connect Nepali-owned businesses, professionals, and events in the Bay Area.')
    pdf.bullet_point('Built features including business directory, expert profiles, and event listings using React, Firebase, and Google Maps API.')
    pdf.bullet_point('Implemented submission forms, data pipelines, and interactive map-based search to enhance usability.')
    pdf.bullet_point('Led branding, marketing, and community outreach strategy to drive user adoption.')
    pdf.ln(3)

    # Education
    pdf.section_title('EDUCATION & CERTIFICATIONS')
    pdf.set_font('Helvetica', 'B', 9.5)
    pdf.cell(0, 4.5, 'Florida A&M University | Project Management Certificate (In Progress)', 0, 1)
    pdf.cell(0, 4.5, 'Google x Kaggle | AI Agents Intensive Certificate (Issued Dec 2025)', 0, 1)
    pdf.cell(0, 4.5, 'San Francisco State University | B.S. in Business Administration, Minor in Information Systems (2023)', 0, 1)

    pdf.output('optimized_resume_niraj_aryal.pdf')
    print("Resume generated: optimized_resume_niraj_aryal.pdf")

if __name__ == '__main__':
    generate_resume()