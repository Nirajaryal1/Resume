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
    pdf.multi_cell(0, 4.2, "Operations and HR leader with proven expertise in process optimization, R&D project coordination, and workforce management at Tesla and Fortune 500 companies. Unique combination of operational excellence, AI automation, and entrepreneurial leadership driving measurable impact across complex, cross-functional initiatives.")
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
    pdf.bullet_point('Coordinated and executed 40+ complex robotic testing scenarios weekly, serving as primary liaison between R&D engineering and operations to consistently meet project deadlines.')
    pdf.bullet_point('Managed daily testing schedules and allocated resources across 5+ hardware units, achieving 95%+ operational uptime and accelerating data collection milestones.')
    pdf.bullet_point('Identified and escalated 50+ hardware/software risks in real-time, reducing project downtime by 20% and strengthening cross-team communication protocols.')
    pdf.ln(2)

    # Yancey's Fancy
    pdf.job_header("YANCEY'S FANCY, Corfu, NY", 'Operations Lead', 'Jul 2022 - Jul 2024')
    pdf.bullet_point('Directed daily production floor operations for 25-person team, managing schedules and allocating resources to achieve 100% output targets across peak seasons.')
    pdf.bullet_point('Engineered packaging line workflow optimizations, eliminating 3 critical bottlenecks and increasing throughput by 18% while reducing material waste by 12%.')
    pdf.bullet_point('Designed and deployed 8+ standard operating procedures (SOPs) and comprehensive cross-training program, reducing operational downtime by 25% and improving team flexibility.')
    pdf.ln(2)

    # A&A Restaurant Group
    pdf.job_header('A&A RESTAURANT GROUP, San Francisco, CA', 'HR Coordinator', 'May 2018 - Jun 2022')
    pdf.bullet_point('Administered full-cycle recruitment, payroll processing, and compliance documentation across 7 locations, ensuring 100% regulatory compliance with federal and state labor laws.')
    pdf.bullet_point('Architected and launched comprehensive onboarding program and engagement initiatives across 200+ employees, improving retention rates by 22% and boosting workforce satisfaction scores.')
    pdf.ln(3)

    # Projects
    pdf.section_title('PROJECTS')

    # Tesla Tee Time
    pdf.job_header('TESLA TEE TIME, Palo Alto, CA', 'Founder & Project Lead', '2025 - Present')
    pdf.bullet_point('Architected an AI-powered recommendation agent for Tesla employees, delivering personalized golf course matches based on office location, schedules, team outings, and EV charging infrastructure.')
    pdf.bullet_point('Built comprehensive knowledge base covering 14+ Bay Area courses, 5 Tesla offices, and 50+ course attributes (twilight rates, difficulty, Supercharger proximity), enabling use cases from quick 9-hole rounds to corporate event planning.')
    pdf.bullet_point('MVP production-ready; designed for seamless expansion to other regions and activity categories; positioned to enhance employee engagement across Tesla workforce.')
    pdf.ln(2)

    # Nepinbay
    pdf.job_header('NEPINBAY, CA', 'Founder & Developer', '2024 - Present')
    pdf.bullet_point('Architected and launched community web platform connecting 50+ Nepali-owned businesses, 30+ professionals, and local events in the Bay Area.')
    pdf.bullet_point('Built full-stack features including business directory, expert profiles, event listings, and interactive map-based search using React, Firebase, and Google Maps API.')
    pdf.bullet_point('Engineered data pipelines and submission workflows enabling community members to self-populate platform; achieved 40+ initial business registrations in first 2 months.')
    pdf.bullet_point('Spearheaded branding, marketing, and community outreach to drive adoption and engagement within Nepali Bay Area community.')
    pdf.ln(2)

    # Skills Summary
    pdf.section_title('TECHNICAL SKILLS')
    pdf.set_font('Helvetica', '', 9.5)
    pdf.multi_cell(0, 4.5, 'Python | SQL | Pandas | React | Firebase | Google Maps API | JIRA | Tableau | Notion | Workflow Automation | Generative AI | ML Fundamentals')
    pdf.ln(2)

    # Education
    pdf.section_title('EDUCATION & CERTIFICATIONS')
    pdf.set_font('Helvetica', 'B', 9.5)
    pdf.cell(0, 4.5, 'Florida A&M University | Project Management Certificate | Expected 2026', 0, 1)
    pdf.cell(0, 4.5, 'Google x Kaggle | AI Agents Intensive Certificate | Completed Dec 2025', 0, 1)
    pdf.cell(0, 4.5, 'San Francisco State University | B.S. Business Administration, Minor in Information Systems | 2023', 0, 1)

    pdf.output('optimized_resume_niraj_aryal.pdf')
    print("Resume generated: optimized_resume_niraj_aryal.pdf")

if __name__ == '__main__':
    generate_resume()