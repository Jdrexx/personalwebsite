"""Editable website content.

Update this file when you want to change copy, resume bullets, services, skills,
or highlighted projects without touching the Django views.

Content synced to Jon Dreksler's latest resume (July 2026).
"""

SITE_CONTENT = {
    'name': 'Jonathan Dreksler',
    'location': 'Kenmore, WA',
    'email': 'Jon@jdreksler.com',
    'phone': '(206) 659-9755',
    'github': 'https://github.com/Jdrexx',
    'headline': 'Technical Project Manager',
    'tagline': (
        'I combine hands-on AI agent development, API integration, and workflow '
        'automation with project leadership and operations experience to help '
        'teams ship faster, reduce manual overhead, and adopt technology that sticks.'
    ),
    'summary': (
        'Technical Project Manager with a Computer Science degree and 4+ years '
        'of cross-industry experience delivering technology-driven process improvements, '
        'workflow automations, and system integrations. Hands-on experience with LLM-based '
        'tools, API integrations, agent frameworks, and automation platforms. Proven ability '
        'to rapidly master new domains, bridge technical and business teams, and deploy '
        'software solutions that drive measurable efficiency gains. Background in project '
        'management, software rollouts, data systems, and compliance — with a focus on '
        'security, governance, and responsible AI adoption.'
    ),
    'cta': {
        'primary_label': 'View Projects',
        'primary_url': '/projects/',
        'secondary_label': 'Read Resume',
        'secondary_url': '/resume/',
    },
    'status': {
        'emoji': '⚡',
        'text': 'Currently: building AI workflow pipelines and automation systems',  # ← update this line to change what appears in the status bar
        'link': '/projects/',
        'link_label': 'See what I build',
    },
    'metrics': [
        {'value': '20+', 'label': 'GitHub Projects'},
        {'value': '4+', 'label': 'Years Experience'},
        {'value': '30+', 'label': 'Tools & Technologies'},
        {'value': '5', 'label': 'Industries Served'},
    ],
    'focus_areas': [
        {
            'title': 'AI Automation & Workflow Design',
            'description': 'LLM-based tools, agent frameworks, API integrations, and automated pipelines that reduce manual overhead and improve accuracy.',
        },
        {
            'title': 'Systems Integration & Development',
            'description': 'Responsive websites, Django/Python applications, MCP tool-calling systems, and clean data workflows across platforms.',
        },
        {
            'title': 'Project Management & Operations',
            'description': 'Scheduling, stakeholder coordination, budget tracking, risk mitigation, process redesign, and change management.',
        },
    ],
    'skills': [
        'AI Automation & Workflow Design', 'Agent-Based Solutions', 'API Integration',
        'Process Automation', 'Systems Integration', 'Project Management',
        'Risk Management', 'Change Management', 'Stakeholder Communication',
        'Process Optimization', 'AI Governance & Security', 'Quality Control',
        'Budget Management', 'Claude', 'Hermes', 'OpenAI API',
        'MCP / Tool-Calling Frameworks', 'Python', 'Django', 'GitHub', 'Ubuntu',
        'WordPress', 'Google Suite', 'QuickBooks', 'Microsoft Office',
        'ClickUp', 'Asana', 'MailChimp', 'Procore', 'Adobe Acrobat',
        'Adobe Illustrator', 'Zendesk', 'Sage 50',
    ],
    'experience': [
        {
            'company': 'Freelance Technical Consultant',
            'location': 'Various Locations, USA',
            'role': 'Freelance Technical Consultant',
            'dates': 'January 2026 – Present',
            'bullets': [
                'Designed and deployed responsive websites integrated with business systems, managing full lifecycle from requirements gathering through testing and deployment across desktop and mobile.',
                'Built automated data workflows for bookkeeping, transaction reconciliation, and financial reporting, reducing manual processing time and improving accuracy.',
                'Engineered database cleanup and validation pipelines, improving data integrity and system reliability for client records.',
                'Integrated digital tools and standardized workflows across platforms, reducing repetitive tasks and administrative overhead through process automation.',
                'Maintained clear client communication, gathered requirements, and adjusted priorities to keep work aligned with budgets, timelines, and business objectives.',
            ],
        },
        {
            'company': 'Vertical Visual Solutions',
            'location': 'Mountlake Terrace, WA',
            'role': 'Project Manager',
            'dates': 'August 2024 – June 2025',
            'bullets': [
                'Coordinated multi-stakeholder installation projects, integrating scheduling systems and vendor coordination workflows to meet build deadlines.',
                'Managed budgets and cost tracking systems, implementing detailed reconciliations for accuracy and compliance across all project phases.',
                'Optimized project workflows through systematic process improvements, reducing delays and subcontractor friction.',
                'Led cross-functional communication between clients, trade partners, and internal teams, ensuring alignment on milestones and deliverables.',
                'Implemented risk identification and mitigation strategies, ensuring on-time, on-budget delivery across concurrent projects.',
                'Conducted quality inspections and addressed issues immediately, reducing rework and maintaining contractual standards.',
            ],
        },
        {
            'company': 'Commode Cappers',
            'location': 'Los Angeles, CA',
            'role': 'Project Manager',
            'dates': 'March 2021 – August 2024',
            'bullets': [
                'Led company-wide software rollout achieving 100% team adoption through structured training programs, change management, and hands-on user support.',
                'Built and maintained company eCommerce platform on WordPress, integrating product listings, payment systems, and order fulfillment workflows.',
                'Analyzed production data to identify bottlenecks and implemented process redesign that compressed timelines by 1 week during peak demand.',
                'Directed vendor coordination, inventory management, and production scheduling, boosting overall output by 15%.',
                'Created data-driven stakeholder presentations by analyzing project metrics and visualizing key insights for faster decision-making.',
            ],
        },
        {
            'company': 'Supertutor Media, Inc.',
            'location': 'Los Angeles, CA',
            'role': 'Office Manager',
            'dates': 'April 2019 – February 2021',
            'bullets': [
                'Integrated Excel-based tracking systems with automated email campaigns, enhancing data accuracy and response times across operations.',
                'Self-studied tax code to resolve complex payroll compliance issues, achieving full regulatory compliance and avoiding penalties.',
                'Detected and reported fraudulent transactions through systematic financial monitoring, preventing thousands in losses.',
                'Maintained website content and coordinated targeted email marketing campaigns, raising user engagement and retention.',
            ],
        },
        {
            'company': 'Various Positions',
            'location': 'California',
            'role': 'Customer Service Representative',
            'dates': 'May 2007 – April 2019',
            'bullets': [
                'Managed customer needs and coordinated staff priorities across diverse retail and service environments, consistently achieving company-wide sales goals.',
                'Trained and onboarded new employees with structured orientation programs, accelerating team readiness and productivity.',
            ],
        },
    ],
    'education': 'Bachelor of Science in Computer Science | University of Maryland Global Campus | December 2022',
    'projects': [
        {
            'name': 'ArchPlanReview',
            'description': 'Reviews architectural plans and lets users search plan documents more easily.',
            'tech': ['Python', 'Document Search', 'Plan Review'],
            'url': 'https://github.com/Jdrexx/ArchPlanReview',
            'status': 'active',
            'details': 'A search engine for architectural plan documents. Users upload or reference plan sets and query them by room, fixture, dimension, or specification. Built with Python, focused on making construction documentation accessible to non-experts.',
        },
        {
            'name': 'ScanExcel',
            'description': 'Turns scanned documents, receipts, handwritten notes, and pasted text into reviewed spreadsheet rows.',
            'tech': ['Python', 'OCR', 'Excel Automation'],
            'url': 'https://github.com/Jdrexx/scanexcel',
            'status': 'active',
            'details': 'OCR pipeline that extracts text from scans and handwritten notes, then structures it into editable spreadsheet rows. Reduces manual data entry for bookkeeping, inventory, and document digitization workflows.',
        },
        {
            'name': 'KnowledgeAssistant',
            'description': 'Uploads notes/docs, chunks them, searches passages, and answers questions with citations.',
            'tech': ['Python', 'Search', 'Knowledge Base'],
            'url': 'https://github.com/Jdrexx/knowledgeassistant',
            'status': 'active',
            'details': 'RAG-style knowledge base that chunks uploaded documents, indexes passages, and answers queries with source citations. Designed for teams that need to search internal documentation without a commercial vector database.',
        },
        {
            'name': 'JobCRM',
            'description': 'Kanban-style job application tracker with follow-up reminders and match notes.',
            'tech': ['Python', 'CRM', 'Productivity'],
            'url': 'https://github.com/Jdrexx/jobcrm',
            'status': 'active',
            'details': 'A kanban job tracker that organizes applications by stage (saved, applied, interviewing, offer, rejected). Includes follow-up reminders and interview note templates. Built to streamline the job search workflow.',
        },
        {
            'name': 'ExpenseTracker',
            'description': 'Imports CSV expenses, auto-categorizes spending, detects anomalies, and exports monthly insights.',
            'tech': ['Python', 'Bookkeeping', 'Data Analysis'],
            'url': 'https://github.com/Jdrexx/ExpenseTracker',
            'status': 'active',
            'details': 'CSV-based expense analyzer that auto-categorizes transactions, flags anomalies, and generates monthly spending summaries. Useful for freelancers and small businesses tracking cash flow.',
        },
        {
            'name': 'ServiceAssistant',
            'description': 'Captures service-business leads, summarizes urgency, and manages receptionist intake workflows.',
            'tech': ['Python', 'Automation', 'Lead Intake'],
            'url': 'https://github.com/Jdrexx/serviceassistant',
            'status': 'active',
            'details': 'Lead intake system for service businesses that captures incoming requests, scores urgency, and routes them to the right team member. Designed to replace manual receptionist triage with automated workflows.',
        },
    ],
}
