"""Search-focused service pages grounded in Jonathan's demonstrated work."""

SERVICES = {
    "ai-workflow-automation": {
        "name": "Workflow Automation",
        "short": "Practical workflows that reduce repetitive work, improve consistency, and keep people in control.",
        "description": "Custom workflow automation for document intake, knowledge search, lead routing, API integrations, and reviewable business processes.",
        "problem": "Teams often know which task wastes time but not whether it needs an LLM, deterministic automation, or a process redesign. The work starts by mapping the decision points, data risks, and handoffs before choosing technology.",
        "outcomes": [
            "A documented current-state workflow and automation opportunity map",
            "A right-sized prototype using rules, APIs, OCR, or AI where each fits",
            "Human review and audit points for consequential decisions",
            "Deployment, operating notes, and a measurable adoption plan",
        ],
        "process": [
            ("Discover", "Map inputs, owners, exceptions, failure costs, and the outcome that matters."),
            ("Design", "Choose deterministic rules first and use AI only where ambiguity requires it."),
            ("Build", "Develop a narrow working slice with logging, validation, and human checkpoints."),
            ("Operationalize", "Test with real scenarios, document ownership, and measure time or error reduction."),
        ],
        "related": ["KnowledgeAssistant", "ScanExcel", "ServiceAssistant"],
    },
    "systems-integration": {
        "name": "Custom Web Applications & Integration",
        "short": "Secure websites, web applications, API connections, and data pipelines tailored to how your organization works.",
        "description": "Custom website and web application development, including client portals, internal tools, APIs, operational dashboards, and secure business workflows.",
        "problem": "Operational data tends to become fragmented across spreadsheets, SaaS tools, inboxes, and line-of-business systems. Integration work should reduce duplicate entry without creating a fragile black box.",
        "outcomes": [
            "A source-to-destination data and ownership map",
            "Validated API or file-based integrations with explicit failure handling",
            "A maintainable Django or Python application where an off-the-shelf tool is insufficient",
            "Runbooks, tests, deployment configuration, and handoff documentation",
        ],
        "process": [
            ("Model", "Define systems of record, field mappings, permissions, and data-quality rules."),
            ("Connect", "Build bounded interfaces with retries, validation, observability, and safe failure modes."),
            ("Verify", "Test normal paths, edge cases, permissions, and recovery with representative data."),
            ("Handoff", "Ship repeatable deployment, documentation, and clear operational ownership."),
        ],
        "related": ["ArchPlanReview", "ExpenseTracker", "JobCRM"],
    },
    "technical-project-management": {
        "name": "Technical Project Management",
        "short": "Delivery leadership that connects technical decisions, business constraints, stakeholders, and adoption.",
        "description": "Technical project management for software rollouts, automation initiatives, systems implementation, stakeholder coordination, risk management, and adoption.",
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
