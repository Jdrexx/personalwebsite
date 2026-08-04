"""Search-focused service pages grounded in Jonathan's demonstrated work."""

SERVICES = {
    "ai-workflow-automation": {
        "name": "AI Workflow Automation",
        "short": "Practical AI for the repetitive work: document processing, bookkeeping, lead routing, and knowledge search, with people kept in the loop.",
        "description": "Custom AI workflow automation for small businesses and service teams: document intake, bookkeeping and reconciliation, lead routing and follow-up, and internal knowledge search. Built with OpenAI, Claude, and local models where privacy matters.",
        "seo_description": "AI workflow automation for small businesses: document processing, bookkeeping, lead routing, and knowledge search with human oversight.",
        "problem": "Most teams know which task wastes time but not whether it needs AI, plain automation, or a process fix. I start by mapping your workflow, the decisions inside it, and what a mistake would cost. Then the right tool gets chosen for each step, not the other way around.",
        "outcomes": [
            "A current-state map of your workflow with the automation opportunities marked",
            "A working prototype using rules, APIs, OCR, or AI, whichever fits each step",
            "Human review and approval points for anything consequential",
            "Deployment, plain-English documentation, and a training plan your team will actually use",
        ],
        "process": [
            ("Discover", "Map inputs, owners, exceptions, and the outcome that matters most."),
            ("Design", "Reach for deterministic rules first; use AI where language and ambiguity require it."),
            ("Build", "Ship a narrow working slice with logging, validation, and human checkpoints."),
            ("Operationalize", "Test with real scenarios, document ownership, and measure time or errors saved."),
        ],
        "related": ["KnowledgeAssistant", "ScanExcel", "ServiceAssistant", "ExpenseTracker"],
    },
    "systems-integration": {
        "name": "Website Design & Development",
        "short": "Custom websites and web apps that are fast, secure, and simple to maintain, designed around your customers.",
        "description": "Website design and development for small businesses: marketing sites, ecommerce, client portals, and internal web apps. Responsive, fast, search-friendly, and built so your team can update it.",
        "seo_description": "Custom website design and development: fast, responsive sites, ecommerce, client portals, and web apps your team can maintain.",
        "problem": "A website only earns its keep if it moves your business forward. I start with your customers and what you need them to do, then design and build a site that loads fast, works on every device, and stays easy for your team to update. No page-builder bloat, no locked-in templates.",
        "outcomes": [
            "A clear statement of your site goals, audience, and content before design begins",
            "A responsive, fast site or web app with design and SEO fundamentals built in",
            "Integrations with the tools you already run: payments, forms, booking, CRMs",
            "Training and written instructions so your team can make updates without me",
        ],
        "process": [
            ("Discover", "Talk through goals, audience, and what the site has to do for the business."),
            ("Design", "Structure the content, map the pages, and build a clean interface."),
            ("Build", "Develop a responsive, fast site with SEO, security, and accessibility in place."),
            ("Launch & Support", "Deploy, connect integrations, train your team, and stay available after launch."),
        ],
        "related": ["JobCRM", "ArchPlanReview", "ServiceAssistant"],
    },
    "client-support": {
        "name": "Customer Service & Client Support",
        "short": "Support systems that keep every customer looked after: AI reception and answering, follow-up automation, and onboarding that feels personal.",
        "description": "Customer service and client support systems: AI reception and after-hours answering, lead and follow-up automation, support ticketing, and client onboarding playbooks.",
        "seo_description": "Customer service systems and automation: AI reception and answering, follow-up, support ticketing, and client onboarding that feels personal.",
        "problem": "Small businesses lose work every time a call goes unanswered or a lead goes cold. Twelve years in customer service taught me what good support feels like, and the systems I build make it repeatable. AI handles the routine questions; your people step in where judgment matters.",
        "outcomes": [
            "A reception and follow-up system so no call or lead slips through",
            "Automated replies and triage that route requests to the right person fast",
            "Onboarding and support playbooks your clients will notice and appreciate",
            "A clear boundary between what the automation handles and where a human takes over",
        ],
        "process": [
            ("Listen", "Map the questions, complaints, and requests your customers actually bring."),
            ("Automate", "Handle the routine requests with AI and rules, with answers that sound like you."),
            ("Escalate", "Route anything uncertain to the right person, fast, with context attached."),
            ("Care", "Review what comes through, tune the system, and keep improving response times."),
        ],
        "related": ["ServiceAssistant", "KnowledgeAssistant", "JobCRM"],
    },
    "technical-project-management": {
        "name": "Technical Project Management",
        "short": "Delivery leadership that connects technical decisions, business constraints, stakeholders, and adoption.",
        "description": "Technical project management for software rollouts, automation initiatives, systems implementation, stakeholder coordination, risk management, and adoption.",
        "seo_description": "Technical project management for software rollouts, automation initiatives, and system implementations: scope, risk, and adoption.",
        "problem": "A technically correct system can still fail when ownership, sequencing, change management, or success criteria are unclear. Delivery needs a shared operating picture, not just a task list.",
        "outcomes": [
            "Clear scope, decision rights, milestones, dependencies, and acceptance criteria",
            "A working risk, issue, change, and stakeholder communication cadence",
            "Translation between technical teams and operational users",
            "Rollout, training, adoption, and post-launch measurement plans",
        ],
        "process": [
            ("Frame", "Align the business outcome, constraints, stakeholders, and definition of done."),
            ("Plan", "Sequence dependencies, surface risks, and assign accountable owners."),
            ("Deliver", "Run a concise communication and decision cadence while protecting quality."),
            ("Adopt", "Support rollout, training, feedback, and measurement after launch."),
        ],
        "related": ["JobCRM", "ServiceAssistant", "ArchPlanReview"],
    },
}
