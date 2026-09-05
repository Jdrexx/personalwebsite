"""Editable website content.

Update this file when you want to change copy, resume bullets, services, skills,
or highlighted projects without touching the Django views.

Content synced to Jon Dreksler's latest resume (July 2026).
"""

SITE_CONTENT = {
    "name": "Jonathan Dreksler",
    "location": "Kenmore, WA",
    "email": "Jon@jdreksler.com",
    "phone": "(206) 659-9755",
    "github": "https://github.com/Jdrexx",
    "headline": "Websites and AI automation built around your business",
    "tagline": (
        "I design, build, and support custom websites, web apps, and AI workflow "
        "automation for small businesses and service teams. You get work that "
        "saves your people time, plus a real person who answers when something "
        "comes up."
    ),
    "summary": (
        "Every project starts with listening. We talk through how your team actually "
        "works, where the repetitive tasks eat the most time, and what done looks like "
        "for your business. Then I design and build the website or automation that "
        "fits, test it against real scenarios, and stay on after launch to support it. "
        "Clients mention the follow-through most often. Good software matters, and so "
        "does being easy to work with."
    ),
    "resume_summary": (
        "Project manager and technical consultant with a Computer Science degree and "
        "experience spanning software rollouts, client-facing operations, and workflow "
        "automation. Background in project management, system implementations, and "
        "customer success across multiple industries."
    ),
    "cta": {
        "primary_label": "View Projects",
        "primary_url": "/projects/",
        "secondary_label": "Start a Conversation",
        "secondary_url": "/contact/",
    },
    "status": {
        "emoji": "⚡",
        "text": "Available for AI automation and website projects",
        "link": "/contact/",
        "link_label": "Say hello",
    },
    "metrics": [
        {"value": "20+", "label": "GitHub Projects"},
        {"value": "12+", "label": "Years in Customer Service"},
        {"value": "30+", "label": "Tools & Technologies"},
        {"value": "5", "label": "Industries Served"},
    ],
    "skills": [
        "AI Workflow Automation",
        "Client Onboarding",
        "Customer Success",
        "Website Design & Development",
        "Responsive Web Design",
        "API Integration",
        "Project Management",
        "Process Automation",
        "CRM Platforms",
        "WordPress",
        "Data Analysis",
        "Process Improvement",
        "Cross-Functional Coordination",
        "OpenAI API",
        "Claude",
        "Hermes Agent",
        "Ollama",
        "MCP / Tool-Calling Frameworks",
        "Python",
        "Django",
        "GitHub",
        "Ubuntu",
        "Google Suite",
        "QuickBooks",
        "Microsoft Office",
        "Zendesk",
        "ClickUp",
        "Asana",
        "MailChimp",
        "Procore",
        "Adobe Illustrator",
    ],
    "experience": [
        {
            "company": "Sazzco",
            "location": "Remote / USA",
            "role": "Technical Project Manager",
            "dates": "January 2026 – Present",
            "bullets": [
                "Designed and deployed responsive websites integrated with business systems, managing full lifecycle from requirements gathering through testing and deployment.",
                "Built AI-assisted data workflows for bookkeeping, transaction reconciliation, and financial reporting using OpenAI and Claude APIs, reducing manual processing time and improving accuracy.",
                "Engineered database cleanup and validation pipelines, improving data integrity and system reliability for client records.",
                "Integrated AI tools (OpenAI, Claude, Hermes Agent, local Ollama models) and standardized workflows across platforms, reducing repetitive tasks and administrative overhead through process automation.",
                "Maintained client communication, gathered requirements, and adjusted priorities to keep work aligned with budgets, timelines, and business objectives.",
            ],
        },
        {
            "company": "Vertical Visual Solutions",
            "location": "Mountlake Terrace, WA",
            "role": "Project Manager",
            "dates": "August 2024 – June 2025",
            "bullets": [
                "Coordinated multi-stakeholder installation projects, integrating scheduling systems and vendor coordination workflows to meet build deadlines.",
                "Managed budgets and cost tracking systems, implementing reconciliations for accuracy and compliance across all project phases.",
                "Optimized project workflows through systematic process improvements, helping reduce delays and subcontractor friction.",
                "Led cross-functional communication between clients, trade partners, and internal teams, ensuring alignment on milestones and deliverables.",
                "Conducted quality inspections and addressed issues promptly, helping maintain contractual standards across concurrent projects.",
            ],
        },
        {
            "company": "Commode Cappers",
            "location": "Los Angeles, CA",
            "role": "Project Manager",
            "dates": "March 2021 – August 2024",
            "bullets": [
                "Led company-wide software rollout achieving full team adoption through structured training, change management, and hands-on user support.",
                "Built and maintained eCommerce platform on WordPress, integrating product listings, payment systems, and order fulfillment workflows.",
                "Analyzed production data to identify bottlenecks and implemented process changes that helped compress timelines during peak demand.",
                "Directed vendor coordination, inventory management, and production scheduling that contributed to increased overall output.",
                "Created data-driven stakeholder presentations, analyzing project metrics and visualizing key insights for decision-making.",
            ],
        },
        {
            "company": "Supertutor Media, Inc.",
            "location": "Los Angeles, CA",
            "role": "Project Manager",
            "dates": "April 2019 – February 2021",
            "bullets": [
                "Integrated Excel-based tracking systems with automated email campaigns, enhancing data accuracy and response times across operations.",
                "Self-studied tax code to resolve complex payroll compliance issues, achieving full regulatory compliance and avoiding penalties.",
                "Detected and reported fraudulent transactions through systematic financial monitoring, helping prevent losses.",
                "Maintained website content and coordinated targeted email marketing campaigns, supporting user engagement and retention efforts.",
            ],
        },
        {
            "company": "Various Positions",
            "location": "California",
            "role": "Office Manager / Customer Service Representative",
            "dates": "May 2007 – April 2019",
            "bullets": [
                "Managed customer needs and coordinated staff priorities across retail and service environments, consistently working toward company sales goals.",
                "Trained and onboarded new employees with structured orientation programs, helping accelerate team readiness and productivity.",
            ],
        },
    ],
    "education": "Bachelor of Science in Computer Science | University of Maryland Global Campus | December 2022",
    "projects": [
        {
            "name": "ArchPlanReview",
            "description": "Lets you search architectural plan documents by room, fixture, or spec instead of flipping through PDFs.",
            "tech": ["Python", "Document Search", "Plan Review"],
            "url": "https://github.com/Jdrexx/ArchPlanReview",
            "status": "active",
            "details": "A search engine for architectural plan documents. Upload or reference plan sets and query them by room, fixture, dimension, or specification.",
            "case_study": {
                "problem": "Architectural plans are dense PDFs full of rooms, dimensions, and fixture callouts. Finding one spec means flipping through pages of blueprints — project managers and contractors do this constantly and it's slow.",
                "steps": [
                    {
                        "title": "Upload or reference plans",
                        "desc": "Drop in PDF plan sets. The system parses each document and links it to project metadata so you always know which revision you're searching.",
                    },
                    {
                        "title": "Index rooms, fixtures, and specs",
                        "desc": "Text extraction pulls room names, dimensions, fixture labels, and callouts into searchable passages. Every result links back to its source page.",
                    },
                    {
                        "title": "Search naturally or by spec",
                        "desc": 'Type "conference room dimensions" or "third-floor electrical specs" — both work. Keyword matching handles exact numbers, semantic search covers natural language.',
                    },
                    {
                        "title": "Compare revisions",
                        "desc": "When plans get updated, the old version stays searchable alongside the new. You can see exactly which spec changed between revisions.",
                    },
                ],
                "decisions": [
                    {
                        "title": "Text extraction over CAD parsing",
                        "desc": "Most plan PDFs have readable labels and callouts. Full CAD parsing would be more powerful but way more complex — text got us 90% of the value with 10% of the effort.",
                    },
                    {
                        "title": "Keyword + semantic, not just one",
                        "desc": 'Pure vector search misses exact numbers ("24x36 window"). Pure keyword misses paraphrases. Combining both covers the real ways people query plans.',
                    },
                ],
                "results": [
                    {
                        "icon": "🔍",
                        "text": "Find any room or spec in seconds instead of flipping pages",
                    },
                    {
                        "icon": "📋",
                        "text": "Track which spec applies to which plan revision",
                    },
                ],
                "next": [
                    "CAD file support for .dwg/.dxf",
                    "Auto-dimension extraction from callouts",
                ],
            },
        },
        {
            "name": "ScanExcel",
            "description": "Turns scanned receipts, invoices, and handwritten notes into editable spreadsheet rows.",
            "tech": ["Python", "OCR", "Excel Automation"],
            "url": "https://github.com/Jdrexx/scanexcel",
            "status": "active",
            "details": "OCR pipeline that extracts text from scans and handwritten notes, then structures it into editable spreadsheet rows.",
            "case_study": {
                "problem": "Every week I'd watch small business owners manually type receipt lines into spreadsheets. It's mind-numbing work and mistakes slip in constantly. A photo of a receipt should just become a row in a spreadsheet without someone retyping it.",
                "steps": [
                    {
                        "title": "Snap or paste",
                        "desc": "Take a photo of a receipt, scan an invoice, or paste raw text. The pipeline handles all three input types.",
                    },
                    {
                        "title": "Extract and review",
                        "desc": "OCR pulls the text, then layout heuristics identify date, vendor, line items, and totals. The result appears as structured rows. You correct any misreads before export — because automated bookkeeping mistakes are worse than manual ones.",
                    },
                ],
                "decisions": [
                    {
                        "title": "Human review before export",
                        "desc": "I could have made it fully automatic, but financial data is unforgiving. One OCR mistake in a tax filing is a headache nobody needs. The review step catches errors without making the process slow.",
                    },
                    {
                        "title": "Regex + heuristics over LLM",
                        "desc": "LLMs are slow and unpredictable for receipt parsing. Layout rules and regex patterns handle 95% of receipts in milliseconds. For the weird 5%, the human review step catches them.",
                    },
                ],
                "results": [
                    {
                        "icon": "⏱️",
                        "text": "Data entry drops from 30 minutes to under 5 per receipt batch",
                    },
                    {
                        "icon": "✅",
                        "text": "Review catches OCR errors before they hit the books",
                    },
                ],
                "next": ["Multi-language OCR", "Mobile camera capture"],
            },
        },
        {
            "name": "KnowledgeAssistant",
            "description": "Upload docs, search passages, get answers with source citations — no commercial vector DB required.",
            "tech": ["Python", "Search", "Knowledge Base"],
            "url": "https://github.com/Jdrexx/knowledgeassistant",
            "status": "active",
            "details": "A lightweight RAG-style knowledge base that chunks documents, indexes passages, and answers queries with source citations. Runs entirely in-process — no Pinecone, no Weaviate, no API keys.",
            "case_study": {
                "problem": 'Every team I\'ve worked with has a "docs folder problem." SOPs, project notes, client records — they pile up and nobody can find anything. People end up asking whoever "might know," which is slow and breaks when that person is out.',
                "steps": [
                    {
                        "title": "Upload",
                        "desc": "Text files, markdown, or pasted notes. Each document gets tagged with metadata so you can track provenance.",
                    },
                    {
                        "title": "Chunk and vectorize",
                        "desc": "Documents split into overlapping passages (~20% overlap so nothing gets cut off at boundaries). Each passage becomes a searchable vector embedding.",
                    },
                    {
                        "title": "Ask and verify",
                        "desc": "Type a question in plain English. The system surfaces relevant passages with similarity scoring. Every answer includes a citation back to the source document — no black-box responses.",
                    },
                ],
                "decisions": [
                    {
                        "title": "No cloud vector database",
                        "desc": "In-process similarity search keeps deployment dead simple, cost at zero, and data fully private. For internal business docs, sending everything to Pinecone was a non-starter from day one.",
                    },
                ],
                "results": [
                    {
                        "icon": "⚡",
                        "text": "New team members query internal docs immediately instead of waiting for walkthroughs",
                    },
                    {
                        "icon": "🔍",
                        "text": "Search specific policies in seconds instead of digging through folders",
                    },
                    {
                        "icon": "📋",
                        "text": "Every answer is auditable — citations link back to the original document",
                    },
                ],
                "next": [
                    "PDF/Word uploads with auto-extraction",
                    "Batch upload folders",
                    "Conversation history and query logs",
                ],
            },
        },
        {
            "name": "JobCRM",
            "description": "Kanban-style job application tracker with follow-up reminders and interview notes.",
            "tech": ["Python", "CRM", "Productivity"],
            "url": "https://github.com/Jdrexx/jobcrm",
            "status": "active",
            "details": "A kanban job tracker that organizes applications by stage — saved, applied, interviewing, offer, rejected. Includes follow-up reminders and interview note templates.",
            "case_study": {
                "problem": "Job hunting means juggling applications across LinkedIn, Indeed, company portals, and email. Spreadsheets get messy fast, follow-ups fall through the cracks, and interview notes end up in five different files. I built this because I was living the problem.",
                "steps": [
                    {
                        "title": "Log the application",
                        "desc": 'Add company, role, link, and notes. The card lands in "Saved" automatically.',
                    },
                    {
                        "title": "Drag through stages",
                        "desc": "Move cards forward as you progress. Each stage transition logs the date so you can see how long things take.",
                    },
                    {
                        "title": "Set follow-ups",
                        "desc": "Reminders for checking in after applications or interviews. No more realizing a week later you forgot to follow up.",
                    },
                ],
                "decisions": [
                    {
                        "title": "Kanban not list",
                        "desc": "A linear list doesn't capture pipeline stage at a glance. Kanban columns match how you actually think about your job search pipeline — no learning curve if you've used Trello or Linear.",
                    },
                    {
                        "title": "No auth, single user",
                        "desc": "This is a personal tool. Adding user accounts would triple the complexity for zero benefit. If someone else wants to use it, they can clone the repo.",
                    },
                ],
                "results": [
                    {
                        "icon": "📋",
                        "text": "Every application tracked from first save through final outcome",
                    },
                    {
                        "icon": "⏰",
                        "text": "Follow-up reminders keep opportunities from going cold",
                    },
                ],
            },
        },
        {
            "name": "ExpenseTracker",
            "description": "Imports CSV bank exports, auto-categorizes transactions, flags anomalies, generates monthly reports.",
            "tech": ["Python", "Bookkeeping", "Data Analysis"],
            "url": "https://github.com/Jdrexx/ExpenseTracker",
            "status": "active",
            "details": "CSV-based expense analyzer for freelancers and small businesses. Auto-categorizes transactions, flags duplicates and unusual charges, and exports monthly spending summaries.",
            "case_study": {
                "problem": "Bank CSV exports are raw data dumps — no categories, no summaries, no insights. Freelancers and small business owners spend hours every month manually tagging transactions and reconciling. I watched someone do this in Excel for an entire afternoon and decided that was enough.",
                "steps": [
                    {
                        "title": "Drop in a CSV",
                        "desc": "Bank or credit card export. The system auto-detects the column layout — no mapping step needed.",
                    },
                    {
                        "title": "Auto-categorize",
                        "desc": "Merchant name patterns and amount ranges tag each transaction: groceries, dining, utilities, transportation, and so on. Rules learn from manual corrections over time.",
                    },
                ],
                "decisions": [
                    {
                        "title": "Rule-based, not LLM",
                        "desc": 'Merchant patterns and amount ranges are deterministic, instant, and predictable. No API costs, no variable latency, no "the AI was down" excuses for something as straightforward as categorizing a Starbucks charge.',
                    },
                    {
                        "title": "Statistical anomaly detection",
                        "desc": "Simple deviation-from-baseline catches duplicates and unusual charges. Catches billing errors without making you manually review every entry.",
                    },
                ],
                "results": [
                    {
                        "icon": "📉",
                        "text": "Monthly categorization drops from hours to under 5 minutes",
                    },
                    {
                        "icon": "🚩",
                        "text": "Duplicate and suspicious charges flagged automatically",
                    },
                ],
            },
        },
        {
            "name": "ServiceAssistant",
            "description": "Captures service-business leads, scores urgency, and routes to the right person.",
            "tech": ["Python", "Automation", "Lead Intake"],
            "url": "https://github.com/Jdrexx/serviceassistant",
            "status": "active",
            "details": "Lead intake system for service businesses that captures incoming requests, scores urgency, and routes them to the right team member.",
            "case_study": {
                "problem": "Service businesses get leads through calls, texts, emails, and web forms. Someone has to triage urgency, figure out which tech is available, and track follow-up. High-volume shops drop leads and send the wrong person — every missed call is a lost job.",
                "steps": [
                    {
                        "title": "Lead arrives",
                        "desc": "Phone, web form, or email. The system captures contact info, service type, and description automatically.",
                    },
                    {
                        "title": "Urgency scored",
                        "desc": 'Keyword matching and time windows determine priority. "Water flooding basement" gets a faster response than "faucet drip."',
                    },
                    {
                        "title": "Routed to the right tech",
                        "desc": "Assigns based on availability and service type. Status tracks through contact → scheduled → in-progress → completed.",
                    },
                ],
                "decisions": [
                    {
                        "title": "Urgency scoring over FIFO",
                        "desc": "First-in-first-out doesn't work for service calls. A burst pipe needs a faster response than a slow drain, and keyword-based urgency scoring handles that without needing a dispatcher.",
                    },
                ],
                "results": [
                    {
                        "icon": "⚡",
                        "text": "Emergency calls routed in seconds instead of minutes",
                    },
                    {
                        "icon": "📋",
                        "text": "Every lead captured and tracked — none lost in the shuffle",
                    },
                ],
                "next": [
                    "SMS text-in support and auto-replies",
                    "Follow-up scheduling with SLA tracking",
                ],
            },
        },
    ],
}