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
        'I build AI agent tools and automation systems, and I manage the '
        'projects that get them into production. API integrations, workflow '
        'pipelines, Django apps — whatever actually helps a team stop doing '
        'things by hand.'
    ),
    'summary': (
        'Technical Project Manager with a Computer Science degree and 4+ years '
        'of experience bridging technical delivery and business outcomes. I\'ve '
        'led software rollouts, built automation workflows, managed multi-stakeholder '
        'construction projects, and worked across industries from edtech to AV '
        'installation. My background covers project management, customer success, '
        'data systems, and compliance — with a practical focus on security and '
        'governance rather than buzzwords.'
    ),
    'cta': {
        'primary_label': 'View Projects',
        'primary_url': '/projects/',
        'secondary_label': 'Read Resume',
        'secondary_url': '/resume/',
    },
    'status': {
        'emoji': '⚡',
        'text': 'Building AI workflow pipelines and automation systems',
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
            'description': 'Agent frameworks, API integrations, and pipelines that automate the repetitive stuff so teams focus on work that matters.',
        },
        {
            'title': 'Systems Integration & Development',
            'description': 'Full-stack Django sites, MCP tool-calling systems, and data pipelines that connect platforms instead of living in silos.',
        },
        {
            'title': 'Project Management & Operations',
            'description': 'Scheduling, budgets, stakeholder coordination, risk tracking, process redesign — the boring stuff that makes or breaks a project.',
        },
    ],
    'skills': [
        'AI Automation & Workflow Design', 'Agent-Based Solutions', 'API Integration',
        'Process Automation', 'Systems Integration', 'Project Management',
        'Risk Management', 'Change Management', 'Stakeholder Communication', 'Customer Success Management',
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
            'description': 'Lets you search architectural plan documents by room, fixture, or spec instead of flipping through PDFs.',
            'tech': ['Python', 'Document Search', 'Plan Review'],
            'url': 'https://github.com/Jdrexx/ArchPlanReview',
            'status': 'active',
            'details': 'A search engine for architectural plan documents. Upload or reference plan sets and query them by room, fixture, dimension, or specification.',
            'case_study': {
                'problem': 'Architectural plans are dense PDFs full of rooms, dimensions, and fixture callouts. Finding one spec means flipping through pages of blueprints — project managers and contractors do this constantly and it\'s slow.',
                'steps': [
                    {'title': 'Upload or reference plans', 'desc': 'Drop in PDF plan sets. The system parses each document and links it to project metadata so you always know which revision you\'re searching.'},
                    {'title': 'Index rooms, fixtures, and specs', 'desc': 'Text extraction pulls room names, dimensions, fixture labels, and callouts into searchable passages. Every result links back to its source page.'},
                    {'title': 'Search naturally or by spec', 'desc': 'Type "conference room dimensions" or "third-floor electrical specs" — both work. Keyword matching handles exact numbers, semantic search covers natural language.'},
                    {'title': 'Compare revisions', 'desc': 'When plans get updated, the old version stays searchable alongside the new. You can see exactly which spec changed between revisions.'},
                ],
                'decisions': [
                    {'title': 'Text extraction over CAD parsing', 'desc': 'Most plan PDFs have readable labels and callouts. Full CAD parsing would be more powerful but way more complex — text got us 90% of the value with 10% of the effort.'},
                    {'title': 'Keyword + semantic, not just one', 'desc': 'Pure vector search misses exact numbers ("24x36 window"). Pure keyword misses paraphrases. Combining both covers the real ways people query plans.'},
                ],
                'results': [
                    {'icon': '🔍', 'text': 'Find any room or spec in seconds instead of flipping pages'},
                    {'icon': '📋', 'text': 'Track which spec applies to which plan revision'},
                ],
                'next': ['CAD file support for .dwg/.dxf', 'Auto-dimension extraction from callouts'],
            },
        },
        {
            'name': 'ScanExcel',
            'description': 'Turns scanned receipts, invoices, and handwritten notes into editable spreadsheet rows.',
            'tech': ['Python', 'OCR', 'Excel Automation'],
            'url': 'https://github.com/Jdrexx/scanexcel',
            'status': 'active',
            'details': 'OCR pipeline that extracts text from scans and handwritten notes, then structures it into editable spreadsheet rows.',
            'case_study': {
                'problem': 'Every week I\'d watch small business owners manually type receipt lines into spreadsheets. It\'s mind-numbing work and mistakes slip in constantly. A photo of a receipt should just become a row in a spreadsheet without someone retyping it.',
                'steps': [
                    {'title': 'Snap or paste', 'desc': 'Take a photo of a receipt, scan an invoice, or paste raw text. The pipeline handles all three input types.'},
                    {'title': 'Extract and review', 'desc': 'OCR pulls the text, then layout heuristics identify date, vendor, line items, and totals. The result appears as structured rows. You correct any misreads before export — because automated bookkeeping mistakes are worse than manual ones.'},
                ],
                'decisions': [
                    {'title': 'Human review before export', 'desc': 'I could have made it fully automatic, but financial data is unforgiving. One OCR mistake in a tax filing is a headache nobody needs. The review step catches errors without making the process slow.'},
                    {'title': 'Regex + heuristics over LLM', 'desc': 'LLMs are slow and unpredictable for receipt parsing. Layout rules and regex patterns handle 95% of receipts in milliseconds. For the weird 5%, the human review step catches them.'},
                ],
                'results': [
                    {'icon': '⏱️', 'text': 'Data entry drops from 30 minutes to under 5 per receipt batch'},
                    {'icon': '✅', 'text': 'Review catches OCR errors before they hit the books'},
                ],
                'next': ['Multi-language OCR', 'Mobile camera capture'],
            },
        },
        {
            'name': 'KnowledgeAssistant',
            'description': 'Upload docs, search passages, get answers with source citations — no commercial vector DB required.',
            'tech': ['Python', 'Search', 'Knowledge Base'],
            'url': 'https://github.com/Jdrexx/knowledgeassistant',
            'status': 'active',
            'details': 'A lightweight RAG-style knowledge base that chunks documents, indexes passages, and answers queries with source citations. Runs entirely in-process — no Pinecone, no Weaviate, no API keys.',
            'case_study': {
                'problem': 'Every team I\'ve worked with has a "docs folder problem." SOPs, project notes, client records — they pile up and nobody can find anything. People end up asking whoever "might know," which is slow and breaks when that person is out.',
                'steps': [
                    {'title': 'Upload', 'desc': 'Text files, markdown, or pasted notes. Each document gets tagged with metadata so you can track provenance.'},
                    {'title': 'Chunk and vectorize', 'desc': 'Documents split into overlapping passages (~20% overlap so nothing gets cut off at boundaries). Each passage becomes a searchable vector embedding.'},
                    {'title': 'Ask and verify', 'desc': 'Type a question in plain English. The system surfaces relevant passages with similarity scoring. Every answer includes a citation back to the source document — no black-box responses.'},
                ],
                'decisions': [
                    {'title': 'No cloud vector database', 'desc': 'In-process similarity search keeps deployment dead simple, cost at zero, and data fully private. For internal business docs, sending everything to Pinecone was a non-starter from day one.'},
                ],
                'results': [
                    {'icon': '⚡', 'text': 'New team members query internal docs immediately instead of waiting for walkthroughs'},
                    {'icon': '🔍', 'text': 'Search specific policies in seconds instead of digging through folders'},
                    {'icon': '📋', 'text': 'Every answer is auditable — citations link back to the original document'},
                ],
                'next': ['PDF/Word uploads with auto-extraction', 'Batch upload folders', 'Conversation history and query logs'],
            },
        },
        {
            'name': 'JobCRM',
            'description': 'Kanban-style job application tracker with follow-up reminders and interview notes.',
            'tech': ['Python', 'CRM', 'Productivity'],
            'url': 'https://github.com/Jdrexx/jobcrm',
            'status': 'active',
            'details': 'A kanban job tracker that organizes applications by stage — saved, applied, interviewing, offer, rejected. Includes follow-up reminders and interview note templates.',
            'case_study': {
                'problem': 'Job hunting means juggling applications across LinkedIn, Indeed, company portals, and email. Spreadsheets get messy fast, follow-ups fall through the cracks, and interview notes end up in five different files. I built this because I was living the problem.',
                'steps': [
                    {'title': 'Log the application', 'desc': 'Add company, role, link, and notes. The card lands in "Saved" automatically.'},
                    {'title': 'Drag through stages', 'desc': 'Move cards forward as you progress. Each stage transition logs the date so you can see how long things take.'},
                    {'title': 'Set follow-ups', 'desc': 'Reminders for checking in after applications or interviews. No more realizing a week later you forgot to follow up.'},
                ],
                'decisions': [
                    {'title': 'Kanban not list', 'desc': 'A linear list doesn\'t capture pipeline stage at a glance. Kanban columns match how you actually think about your job search pipeline — no learning curve if you\'ve used Trello or Linear.'},
                    {'title': 'No auth, single user', 'desc': 'This is a personal tool. Adding user accounts would triple the complexity for zero benefit. If someone else wants to use it, they can clone the repo.'},
                ],
                'results': [
                    {'icon': '📋', 'text': 'Every application tracked from first save through final outcome'},
                    {'icon': '⏰', 'text': 'Follow-up reminders keep opportunities from going cold'},
                ],
            },
        },
        {
            'name': 'ExpenseTracker',
            'description': 'Imports CSV bank exports, auto-categorizes transactions, flags anomalies, generates monthly reports.',
            'tech': ['Python', 'Bookkeeping', 'Data Analysis'],
            'url': 'https://github.com/Jdrexx/ExpenseTracker',
            'status': 'active',
            'details': 'CSV-based expense analyzer for freelancers and small businesses. Auto-categorizes transactions, flags duplicates and unusual charges, and exports monthly spending summaries.',
            'case_study': {
                'problem': 'Bank CSV exports are raw data dumps — no categories, no summaries, no insights. Freelancers and small business owners spend hours every month manually tagging transactions and reconciling. I watched someone do this in Excel for an entire afternoon and decided that was enough.',
                'steps': [
                    {'title': 'Drop in a CSV', 'desc': 'Bank or credit card export. The system auto-detects the column layout — no mapping step needed.'},
                    {'title': 'Auto-categorize', 'desc': 'Merchant name patterns and amount ranges tag each transaction: groceries, dining, utilities, transportation, and so on. Rules learn from manual corrections over time.'},
                ],
                'decisions': [
                    {'title': 'Rule-based, not LLM', 'desc': 'Merchant patterns and amount ranges are deterministic, instant, and predictable. No API costs, no variable latency, no "the AI was down" excuses for something as straightforward as categorizing a Starbucks charge.'},
                    {'title': 'Statistical anomaly detection', 'desc': 'Simple deviation-from-baseline catches duplicates and unusual charges. Catches billing errors without making you manually review every entry.'},
                ],
                'results': [
                    {'icon': '📉', 'text': 'Monthly categorization drops from hours to under 5 minutes'},
                    {'icon': '🚩', 'text': 'Duplicate and suspicious charges flagged automatically'},
                ],
            },
        },
        {
            'name': 'ServiceAssistant',
            'description': 'Captures service-business leads, scores urgency, and routes to the right person.',
            'tech': ['Python', 'Automation', 'Lead Intake'],
            'url': 'https://github.com/Jdrexx/serviceassistant',
            'status': 'active',
            'details': 'Lead intake system for service businesses that captures incoming requests, scores urgency, and routes them to the right team member.',
            'case_study': {
                'problem': 'Service businesses get leads through calls, texts, emails, and web forms. Someone has to triage urgency, figure out which tech is available, and track follow-up. High-volume shops drop leads and send the wrong person — every missed call is a lost job.',
                'steps': [
                    {'title': 'Lead arrives', 'desc': 'Phone, web form, or email. The system captures contact info, service type, and description automatically.'},
                    {'title': 'Urgency scored', 'desc': 'Keyword matching and time windows determine priority. "Water flooding basement" gets a faster response than "faucet drip."'},
                    {'title': 'Routed to the right tech', 'desc': 'Assigns based on availability and service type. Status tracks through contact → scheduled → in-progress → completed.'},
                ],
                'decisions': [
                    {'title': 'Urgency scoring over FIFO', 'desc': 'First-in-first-out doesn\'t work for service calls. A burst pipe needs a faster response than a slow drain, and keyword-based urgency scoring handles that without needing a dispatcher.'},
                ],
                'results': [
                    {'icon': '⚡', 'text': 'Emergency calls routed in seconds instead of minutes'},
                    {'icon': '📋', 'text': 'Every lead captured and tracked — none lost in the shuffle'},
                ],
                'next': ['SMS text-in support and auto-replies', 'Follow-up scheduling with SLA tracking'],
            },
        },
    ],
}
