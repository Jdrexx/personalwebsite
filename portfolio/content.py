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
            'case_study': {
                'problem': 'Architectural plans are dense, hard to navigate, and scattered across PDFs. Finding a specific room dimension, fixture spec, or notation means manually flipping through pages of blueprints — slow and error-prone for project managers and contractors.',
                'steps': [
                    {'title': 'Upload plans', 'desc': 'Upload architectural plan PDFs or reference existing plan sets. Each document is parsed and stored with project metadata.'},
                    {'title': 'Index rooms & fixtures', 'desc': 'Text is extracted and structured into searchable passages keyed by room, fixture, dimension, and specification. Every result links back to its source plan page.'},
                    {'title': 'Search naturally', 'desc': 'Type queries like "conference room dimensions" or "third-floor electrical specs" and get relevant passages with source citations.'},
                ],
                'decisions': [
                    {'title': 'Text-first search', 'desc': 'Prioritized text extraction over CAD rendering — most plan documents contain readable labels and callouts that text search can index directly.'},
                    {'title': 'Keyword + semantic hybrid', 'desc': 'Combines traditional keyword matching with semantic similarity to handle both exact specs ("24x36 window") and natural language queries ("biggest conference room").'},
                ],
                'results': [
                    {'icon': '🔍', 'text': 'Find any room or spec in seconds instead of flipping through pages'},
                    {'icon': '📐', 'text': 'Construction teams can verify dimensions without printing and measuring'},
                    {'icon': '📋', 'text': 'Plan version tracking — know exactly which spec applies to which revision'},
                ],
                'next': ['CAD file support for native .dwg/.dxf parsing', 'Auto-dimension extraction from plan callouts', 'Markup and annotation sharing across team members'],
            },
        },
        {
            'name': 'ScanExcel',
            'description': 'Turns scanned documents, receipts, handwritten notes, and pasted text into reviewed spreadsheet rows.',
            'tech': ['Python', 'OCR', 'Excel Automation'],
            'url': 'https://github.com/Jdrexx/scanexcel',
            'status': 'active',
            'details': 'OCR pipeline that extracts text from scans and handwritten notes, then structures it into editable spreadsheet rows. Reduces manual data entry for bookkeeping, inventory, and document digitization workflows.',
            'case_study': {
                'problem': 'Receipts, invoices, and handwritten notes pile up in paper form or as phone photos. Someone has to manually type each line into a spreadsheet — tedious, slow, and prone to typos. For small businesses doing weekly bookkeeping, this burns hours.',
                'steps': [
                    {'title': 'Capture or upload', 'desc': 'Take a photo of a receipt, scan an invoice, or paste raw text. The system accepts images and text input.'},
                    {'title': 'Extract & parse', 'desc': 'OCR engine extracts text from images. A parsing layer identifies fields: date, vendor, amount, line items, and totals.'},
                    {'title': 'Review & export', 'desc': 'Results appear as structured spreadsheet rows. Users correct any misreads before exporting to Excel or CSV.'},
                ],
                'decisions': [
                    {'title': 'Human-in-the-loop review', 'desc': 'Full automation is risky for financial data. The system extracts, then a human reviews and confirms before export — catches OCR mistakes without sacrificing speed.'},
                    {'title': 'Rule-based field parsing', 'desc': 'Instead of an LLM for every receipt (slow and expensive), extraction uses layout heuristics and regex patterns tuned for common receipt formats. Fast and deterministic.'},
                ],
                'results': [
                    {'icon': '⏱️', 'text': 'Cuts data entry time from 30 minutes to under 5 per batch of receipts'},
                    {'icon': '✅', 'text': 'Review step catches OCR errors before they hit the books'},
                    {'icon': '📊', 'text': 'Exports directly to Excel — no format conversion needed'},
                ],
                'next': ['Mobile app with real-time camera capture', 'Multi-language OCR for receipts in Spanish and Chinese', 'Table detection for complex invoice layouts'],
            },
        },
        {
            'name': 'KnowledgeAssistant',
            'description': 'Uploads notes/docs, chunks them, searches passages, and answers questions with citations.',
            'tech': ['Python', 'Search', 'Knowledge Base'],
            'url': 'https://github.com/Jdrexx/knowledgeassistant',
            'status': 'active',
            'details': 'RAG-style knowledge base that chunks uploaded documents, indexes passages, and answers queries with source citations. Designed for teams that need to search internal documentation without a commercial vector database.',
            'case_study': {
                'problem': 'Teams sit on mountains of documentation — SOPs, project notes, client records, technical specs. Finding the right information means digging through folders or asking someone who "might know." Slow, frustrating, and scales terribly.',
                'steps': [
                    {'title': 'Upload documents', 'desc': 'Upload plain text files, markdown docs, or paste notes directly. Each document is stored with metadata for tracking.'},
                    {'title': 'Chunk & index', 'desc': 'Documents are split into overlapping passages. Each passage becomes a searchable vector embedding, mapped back to its source document for attribution.'},
                    {'title': 'Ask questions', 'desc': 'Type a question in plain English. The system finds relevant passages via semantic similarity and returns answers with citations back to the original source.'},
                ],
                'decisions': [
                    {'title': 'No commercial vector DB', 'desc': 'Uses in-process similarity search instead of Pinecone or Weaviate. Keeps deployment simple, cost zero, and data fully private — critical for internal business docs.'},
                    {'title': 'Overlapping chunks', 'desc': 'Passages overlap by ~20% to avoid cutting off meaning at chunk boundaries. A sentence spanning two chunks appears in full in at least one passage.'},
                    {'title': 'Citation-first answers', 'desc': 'Every answer includes the source passage and document name. Users verify claims and explore context — no black-box responses.'},
                ],
                'results': [
                    {'icon': '⚡', 'desc': 'New team members query internal docs from day one instead of waiting for walkthroughs'},
                    {'icon': '🔍', 'desc': 'Search time drops from minutes to seconds for specific policies and specs'},
                    {'icon': '📋', 'desc': 'Every answer is auditable — citations prevent hallucinated responses'},
                ],
                'next': ['PDF and Word document uploads with automatic extraction', 'Batch upload entire folders at once', 'Conversation history across multiple questions', 'Admin dashboard for query logs and popular searches'],
            },
        },
        {
            'name': 'JobCRM',
            'description': 'Kanban-style job application tracker with follow-up reminders and match notes.',
            'tech': ['Python', 'CRM', 'Productivity'],
            'url': 'https://github.com/Jdrexx/jobcrm',
            'status': 'active',
            'details': 'A kanban job tracker that organizes applications by stage (saved, applied, interviewing, offer, rejected). Includes follow-up reminders and interview note templates. Built to streamline the job search workflow.',
            'case_study': {
                'problem': 'Job hunting involves dozens of applications across multiple platforms, each at different stages. Spreadsheets get messy, follow-ups get missed, and interview prep notes end up scattered across files. A purpose-built tracker keeps everything in one place.',
                'steps': [
                    {'title': 'Log an application', 'desc': 'Add company, role, link, and notes. The card appears in the "Saved" column automatically.'},
                    {'title': 'Drag through stages', 'desc': 'Move cards across columns as you progress: Saved → Applied → Interviewing → Offer → Rejected. Each move logs the date.'},
                    {'title': 'Follow up on time', 'desc': 'Set reminders for follow-ups after applications or interviews. Never forget to check in after a week of silence.'},
                ],
                'decisions': [
                    {'title': 'Kanban over list view', 'desc': 'Visual columns match how people naturally think about pipeline stages. Familiar from Trello, Linear, and Jira — zero learning curve.'},
                    {'title': 'Lightweight, no auth', 'desc': 'No user accounts or login system. Keeps it simple for a single user running locally — a deliberate tradeoff to avoid overhead for a personal tool.'},
                ],
                'results': [
                    {'icon': '📋', 'text': 'Every application tracked from first save through final outcome'},
                    {'icon': '⏰', 'text': 'Follow-up reminders prevent opportunities from going cold'},
                    {'icon': '📝', 'text': 'Interview notes stored alongside each application — no more lost prep docs'},
                ],
                'next': ['Calendar integration for interview scheduling', 'Stats dashboard with response rates and stage timelines', 'Email integration to auto-detect application confirmations'],
            },
        },
        {
            'name': 'ExpenseTracker',
            'description': 'Imports CSV expenses, auto-categorizes spending, detects anomalies, and exports monthly insights.',
            'tech': ['Python', 'Bookkeeping', 'Data Analysis'],
            'url': 'https://github.com/Jdrexx/ExpenseTracker',
            'status': 'active',
            'details': 'CSV-based expense analyzer that auto-categorizes transactions, flags anomalies, and generates monthly spending summaries. Useful for freelancers and small businesses tracking cash flow.',
            'case_study': {
                'problem': 'Bank and credit card CSV exports are raw transaction dumps — no categories, no summaries, no insights. Freelancers and small business owners spend hours each month manually categorizing and reconciling entries.',
                'steps': [
                    {'title': 'Import a CSV', 'desc': 'Drop in a bank or credit card CSV. The system auto-detects the format — no column mapping needed.'},
                    {'title': 'Auto-categorize', 'desc': 'Each transaction is tagged with a category: groceries, dining, utilities, transportation, entertainment, health, shopping, income, or custom. Rules learn from corrections.'},
                    {'title': 'Review insights', 'desc': 'See monthly spending breakdowns, anomaly flags (unusual amounts, duplicate charges), and category trends. Export the report for tax prep.'},
                ],
                'decisions': [
                    {'title': 'Rule-based categorization', 'desc': 'Uses merchant name patterns and amount ranges instead of an LLM. Deterministic, instant, and predictable — no API costs or variable latency.'},
                    {'title': 'Statistical anomaly detection', 'desc': 'Flags transactions that deviate significantly from a merchant or category baseline. Catches billing errors and fraud without manual review of every line.'},
                ],
                'results': [
                    {'icon': '📉', 'text': 'Monthly categorization drops from hours to under 5 minutes'},
                    {'icon': '🚩', 'text': 'Duplicate and unusual charges flagged automatically'},
                    {'icon': '📊', 'text': 'Clean monthly reports ready for tax preparation and budget reviews'},
                ],
                'next': ['Bank API integration for auto-import', 'Recurring expense detection and subscription tracking', 'Budget targets with spending alerts'],
            },
        },
        {
            'name': 'ServiceAssistant',
            'description': 'Captures service-business leads, summarizes urgency, and manages receptionist intake workflows.',
            'tech': ['Python', 'Automation', 'Lead Intake'],
            'url': 'https://github.com/Jdrexx/serviceassistant',
            'status': 'active',
            'details': 'Lead intake system for service businesses that captures incoming requests, scores urgency, and routes them to the right team member. Designed to replace manual receptionist triage with automated workflows.',
            'case_study': {
                'problem': 'Service businesses (plumbers, electricians, HVAC) get leads through calls, texts, and emails. Someone manually triages urgency, routes to the right tech, and tracks follow-up. High-volume shops drop leads, respond late, or send the wrong person — costing jobs.',
                'steps': [
                    {'title': 'Lead comes in', 'desc': 'A new request arrives via phone, web form, or email. The system captures contact info, service type, and description.'},
                    {'title': 'Urgency scored', 'desc': 'Keywords, time windows, and service type determine urgency. "Water flooding basement" scores higher than "faucet drip."'},
                    {'title': 'Routed & tracked', 'desc': 'The lead is assigned to the right team member with priority level. Status tracks through contact, scheduled, in-progress, completed.'},
                ],
                'decisions': [
                    {'title': 'Urgency scoring over FIFO', 'desc': 'First-in-first-out doesn\'t work for service calls — a burst pipe needs faster response than a slow drain. Keyword-based urgency scoring prioritizes what matters.'},
                    {'title': 'Simple queue, not full CRM', 'desc': 'Focused on intake and routing rather than invoicing, scheduling, or marketing. Integrates with existing tools rather than replacing them.'},
                ],
                'results': [
                    {'icon': '⚡', 'text': 'Emergency calls routed in seconds instead of minutes'},
                    {'icon': '📋', 'text': 'No leads lost — every intake is captured and tracked'},
                    {'icon': '🎯', 'text': 'Right technician dispatched on the first try, every time'},
                ],
                'next': ['SMS integration for text-in leads and auto-replies', 'Automated follow-up scheduling with SLA tracking', 'Customer dashboard for lead status self-service'],
            },
        },
    ],
}
