"""Editable website content.

Update this file when you want to change copy, resume bullets, services, skills,
or highlighted projects without touching the Django views.
"""

SITE_CONTENT = {
    'name': 'Jonathan Dreksler',
    'location': 'Kenmore, WA',
    'email': 'jondreksler369@gmail.com',
    'phone': '+1 310 497 8153',
    'github': 'https://github.com/Jdrexx',
    'headline': 'Project Manager, Web Builder, and Operations-Focused Technologist',
    'tagline': (
        'I combine project leadership, workflow optimization, bookkeeping/data support, '
        'and practical software skills to help teams ship cleaner systems and better client experiences.'
    ),
    'summary': (
        'Innovative project manager with 4+ years of cross-industry experience in project management, '
        'scheduling, operations, and client communication. Recognized for quickly mastering new industries, '
        'streamlining workflows, leading high-pressure deadlines, and using technology to improve accuracy and adoption.'
    ),
    'cta': {
        'primary_label': 'View Projects',
        'primary_url': '/projects/',
        'secondary_label': 'Read Resume',
        'secondary_url': '/resume/',
    },
    'focus_areas': [
        {
            'title': 'Project Coordination',
            'description': 'Scheduling, stakeholder updates, budget tracking, installation planning, and risk mitigation.',
        },
        {
            'title': 'Web + Workflow Builds',
            'description': 'Responsive websites, Django/Python MVPs, WordPress updates, and clean client-facing pages.',
        },
        {
            'title': 'Data, OCR + Bookkeeping',
            'description': 'Spreadsheet cleanup, document-to-data workflows, account reconciliation, and reporting support.',
        },
    ],
    'skills': [
        'Project Coordination', 'Scheduling', 'Risk Management', 'Team Leadership', 'Stakeholder Communication',
        'Process Optimization', 'Quality Control', 'Budget Management', 'Workflow Improvement', 'Python', 'Django',
        'WordPress', 'QuickBooks', 'Procore', 'Microsoft Project', 'Google Suite', 'Adobe Acrobat', 'Adobe Illustrator',
        'ClickUp', 'MailChimp', 'Asana', 'Sage 50', 'Hermes', 'Microsoft Office',
    ],
    'experience': [
        {
            'company': 'Various Clients',
            'location': 'Various Locations, USA',
            'role': 'Freelance Web, Bookkeeping, and Data Support',
            'dates': 'January 2026 – June 2026',
            'bullets': [
                'Built and maintained responsive websites for small business clients across desktop and mobile browsers.',
                'Managed bookkeeping tasks including transaction recording, account reconciliation, receipt organization, and basic reports.',
                'Completed data entry and database cleanup projects by importing, validating, and organizing client records.',
                'Improved digital workflows by standardizing tracking processes and reducing repetitive manual tasks.',
            ],
        },
        {
            'company': 'Vertical Visual Solutions',
            'location': 'Mountlake Terrace, WA',
            'role': 'Project Manager',
            'dates': 'August 2024 – June 2025',
            'bullets': [
                'Oversaw signage installation projects through onsite pre-con meetings, contractor alignment, and schedule coordination.',
                'Prepared budget reports and tracked expenses for accuracy and compliance.',
                'Maintained client relationships with professional milestone communication and documentation.',
                'Identified risks, implemented mitigation strategies, inspected quality, and reduced rework delays.',
            ],
        },
        {
            'company': 'Commode Cappers',
            'location': 'Los Angeles, CA',
            'role': 'Project Manager',
            'dates': 'March 2021 – August 2024',
            'bullets': [
                'Directed art-accessory production projects across inventory, vendors, and worker productivity.',
                'Boosted output by 15% and improved high-demand timelines through process redesign.',
                'Led a company-wide software rollout with training that achieved full team adoption.',
                'Built and maintained the company eCommerce site with improved layouts and product listings.',
            ],
        },
        {
            'company': 'Supertutor Media, Inc.',
            'location': 'Los Angeles, CA',
            'role': 'Office Manager',
            'dates': 'April 2019 – February 2021',
            'bullets': [
                'Managed scheduling, invoicing, payroll systems, Excel tracking, and automated email campaigns.',
                'Resolved payroll tax issues through research and agency coordination, achieving compliance and avoiding penalties.',
                'Detected and reported fraudulent transactions by monitoring invoices and financial records.',
                'Maintained website content and email campaigns to increase user engagement.',
            ],
        },
    ],
    'education': 'Bachelor of Science in Computer Science | University of Maryland GC | December 2022',
    'projects': [
        {
            'name': 'ArchPlanReview',
            'description': 'Reviews architectural plans and lets users search plan documents more easily.',
            'tech': ['Python', 'Document Search', 'Plan Review'],
            'url': 'https://github.com/Jdrexx/ArchPlanReview',
        },
        {
            'name': 'ScanExcel',
            'description': 'Turns scanned documents, receipts, handwritten notes, and pasted text into reviewed spreadsheet rows.',
            'tech': ['Python', 'OCR', 'Excel Automation'],
            'url': 'https://github.com/Jdrexx/scanexcel',
        },
        {
            'name': 'KnowledgeAssistant',
            'description': 'Uploads notes/docs, chunks them, searches passages, and answers questions with citations.',
            'tech': ['Python', 'Search', 'Knowledge Base'],
            'url': 'https://github.com/Jdrexx/knowledgeassistant',
        },
        {
            'name': 'JobCRM',
            'description': 'Kanban-style job application tracker with follow-up reminders and match notes.',
            'tech': ['Python', 'CRM', 'Productivity'],
            'url': 'https://github.com/Jdrexx/jobcrm',
        },
        {
            'name': 'ExpenseTracker',
            'description': 'Imports CSV expenses, auto-categorizes spending, detects anomalies, and exports monthly insights.',
            'tech': ['Python', 'Bookkeeping', 'Data Analysis'],
            'url': 'https://github.com/Jdrexx/ExpenseTracker',
        },
        {
            'name': 'ServiceAssistant',
            'description': 'Captures service-business leads, summarizes urgency, and manages receptionist intake workflows.',
            'tech': ['Python', 'Automation', 'Lead Intake'],
            'url': 'https://github.com/Jdrexx/serviceassistant',
        },
    ],
}
