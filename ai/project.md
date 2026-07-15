# PromocoesCOMAER

## Project Overview

PromocoesCOMAER is a Decision Support System (DSS) developed for the Brazilian Air Force (COMAER) to analyze, simulate and forecast military promotions.

The application creates a **Digital Twin** of the promotion process, allowing analysts to explore hypothetical scenarios based on historical data, current personnel information and configurable business rules.

The system does **not** replace the official promotion process.

Instead, it provides analytical information that supports decision making by producing reliable simulations and statistical projections.

---

# Vision

Create the most complete analytical platform for military promotion simulation within COMAER.

The platform should allow analysts to understand not only the current promotion scenario, but also the future impact of changes in personnel, vacancies, legislation and promotion criteria.

---

# Mission

Provide a modern, reliable and maintainable platform capable of generating promotion simulations with high accuracy, helping decision makers understand future promotion scenarios before official decisions are taken.

---

# Objectives

The project has five primary objectives.

## 1. Digital Twin

Create a digital representation of the promotion system.

The Digital Twin must reproduce the behavior of the real promotion process using historical and current personnel data.

---

## 2. Simulation Engine

Allow analysts to simulate future promotion scenarios.

Examples:

- retirement projections
- vacancy creation
- promotion chains
- changes in promotion limits
- changes in legislation
- different promotion policies

---

## 3. Decision Support

Generate information that assists human decision makers.

Examples:

- promotion probability
- promotion forecasts
- future vacancies
- promotion timelines
- statistical indicators

---

## 4. Data Integration

Maintain an analytical PostgreSQL database synchronized with Oracle.

Oracle remains the operational system.

PostgreSQL becomes the analytical platform.

---

## 5. Maintainability

Create software that can evolve for many years.

The codebase must prioritize:

- readability
- modularity
- documentation
- automated testing

---

# Scope

The project includes:

- Oracle data synchronization
- ETL processes
- PostgreSQL analytical database
- FastAPI backend
- React frontend
- REST API
- Promotion simulation engine
- Statistical analysis
- Dashboards
- Reports
- Audit information
- Historical analysis

---

# Out of Scope

The project does NOT:

- approve promotions
- replace official COMAER systems
- modify Oracle operational data
- change official legislation
- execute administrative procedures

PromocoesCOMAER is an analytical platform.

---

# Target Users

Primary users:

- Promotion analysts
- COMAER personnel managers
- Decision makers
- Strategic planning teams

Secondary users:

- System administrators
- Developers
- Database administrators

---

# Functional Domains

The application is divided into multiple domains.

## Personnel

Military personnel information.

Examples:

- personal data
- rank
- specialty
- career
- status

---

## Promotion

Promotion rules.

Examples:

- seniority
- merit
- eligibility
- vacancies
- promotion limits

---

## Simulation

Simulation engine.

Examples:

- future scenarios
- promotion forecasts
- retirement impact
- organizational changes

---

## Analytics

Business Intelligence.

Examples:

- indicators
- statistics
- dashboards
- reports

---

## Administration

System configuration.

Examples:

- synchronization
- ETL execution
- parameters
- audit
- monitoring

---

# Data Sources

Primary source:

Oracle Database

Analytical database:

PostgreSQL

External data sources may be incorporated in future versions.

---

# Non-Functional Requirements

The system must be:

- reliable
- secure
- maintainable
- modular
- scalable
- documented
- testable

---

# Quality Goals

The project prioritizes:

Correctness over speed.

Maintainability over complexity.

Explicit code over implicit behavior.

Documentation over assumptions.

Automation over manual processes.

---

# Development Principles

Every feature should:

- solve one problem
- be documented
- include automated tests
- follow project architecture
- preserve backward compatibility whenever possible

---

# AI Assistant Instructions

Before implementing any feature, understand:

- the project objective
- the affected business domain
- existing architecture
- related business rules

Never implement functionality based solely on assumptions.

If requirements are ambiguous, ask for clarification.

---

# Long-Term Vision

The project is expected to become a strategic analytical platform for promotion planning.

Future versions may include:

- Machine Learning
- Predictive Analytics
- Optimization algorithms
- Scenario comparison
- Executive dashboards
- Explainable AI
- Advanced reporting
- Integration with additional COMAER systems

---

End of document.
