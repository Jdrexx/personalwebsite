(function () {
  "use strict";
  var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var heading = document.querySelector(".typewriter");
  if (heading && !reducedMotion) {
    var text = heading.dataset.text || heading.textContent;
    heading.textContent = "";
    var index = 0;
    function typeNext() {
      if (index < text.length) { heading.textContent += text.charAt(index++); window.setTimeout(typeNext, 45); }
    }
    window.setTimeout(typeNext, 250);
  }
  var input = document.getElementById("terminal-input");
  var output = document.getElementById("terminal-output");
  var commands = {
    help: "Available: about, projects, services, skills, help, clear",
    about: "Technical Project Manager — AI automation, systems integration, and delivery.",
    projects: "ArchPlanReview · ScanExcel · KnowledgeAssistant · JobCRM · ExpenseTracker · ServiceAssistant",
    services: "AI Workflow Automation · Python & Django Integration · Technical Project Management",
    skills: "AI Automation, API Integration, Python, Django, MCP, Project Management"
  };
  if (input && output) input.addEventListener("keydown", function (event) {
    if (event.key !== "Enter" || !input.value.trim()) return;
    var command = input.value.trim().toLowerCase();
    if (command === "clear") { output.textContent = ""; input.value = ""; return; }
    var line = document.createElement("div"); line.className = "terminal-line";
    var prompt = document.createElement("span"); prompt.className = "prompt"; prompt.textContent = "jon@portfolio:~$ ";
    var value = document.createElement("span"); value.className = "cmd"; value.textContent = command;
    line.append(prompt, value);
    var response = document.createElement("div"); response.className = "terminal-line output";
    response.textContent = commands[command] || "Unknown command. Try: help";
    output.append(line, response); output.scrollTop = output.scrollHeight; input.value = "";
  });
})();
