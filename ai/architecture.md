# System Architecture

## Overview

PromocoesCOMAER follows a modular, layered architecture based on Domain Driven Design (DDD) principles and Clean Architecture concepts.

The objective is to isolate business rules from infrastructure concerns, allowing the application to evolve independently from frameworks, databases and user interfaces.

The architecture prioritizes:

- Separation of responsibilities
- Testability
- Maintainability
- Scalability
- Reusability
- Explicit dependencies

---

# High Level Architecture

```
                 Oracle Database
                        │
                        │
                 ETL / Synchronization
                        │
                        ▼
                 PostgreSQL
                        │
                        ▼
                FastAPI Backend
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
   REST API        Simulation      Analytics
                        │
                        ▼
                  React Frontend
                        │
                        ▼
                    End Users
```

---

# Repository Structure

```
PromocoesCOMAER/

backend/
frontend/
database/
docs/
tests/
scripts/
docker/

ai/

.vscode/

README.md

AI_RULES.md
```

---

# Backend Architecture

The backend is implemented using FastAPI.

The application is divided into independent layers.

```
backend/

app/

api/
core/
models/
schemas/
repositories/
services/
etl/
simulation/
analytics/
security/
utils/

main.py
```

---

# Layer Responsibilities

## API

Responsibilities

- HTTP endpoints
- Request validation
- Response generation

Never:

- implement business rules
- execute SQL
- perform calculations

API only orchestrates requests.

---

## Services

This is the heart of the application.

Responsibilities

- promotion rules
- simulations
- validations
- calculations
- orchestration

Every business rule belongs here.

---

## Repositories

Responsibilities

- database access
- persistence
- queries

Repositories never contain business rules.

---

## Models

SQLAlchemy ORM entities.

Represent database tables.

No business logic.

---

## Schemas

Pydantic models.

Responsibilities

- request validation
- response serialization
- API documentation

---

## Core

Shared infrastructure.

Examples

- configuration
- logging
- dependency injection
- security
- startup
- constants

---

## ETL

Responsible for synchronizing Oracle with PostgreSQL.

Responsibilities

- extraction
- transformation
- loading
- validation
- incremental synchronization

Oracle is read-only.

---

## Simulation

Core business engine.

Responsibilities

- promotion simulation
- vacancy simulation
- retirement simulation
- future scenarios

This module contains the Digital Twin.

---

## Analytics

Responsible for analytical calculations.

Examples

- indicators
- statistics
- trends
- projections
- reports

---

# Frontend

React application.

Responsibilities

- dashboards
- reports
- simulation interface
- administration
- authentication

Business rules remain in the backend.

---

# Database Architecture

Two databases exist.

Oracle

Operational database.

Source system.

Read-only.

↓

PostgreSQL

Analytical database.

Stores synchronized information.

Receives simulation results.

Supports dashboards.

---

# Data Flow

```
Oracle
   │
Extract
   │
Transform
   │
Load
   ▼
PostgreSQL
   │
Repositories
   │
Services
   │
REST API
   │
React
```

---

# Dependency Direction

Dependencies always point inward.

```
Frontend
     │
API
     │
Services
     │
Repositories
     │
Database
```

Services never depend on Frontend.

Repositories never depend on API.

---

# Domain Organization

Major domains include

Personnel

Promotion

Simulation

Analytics

Administration

Authentication

Audit

ETL

Each domain should evolve independently.

---

# Business Rules

Business rules are centralized.

Never duplicate calculations.

Never create multiple implementations of promotion logic.

Every rule must exist in one place only.

---

# Configuration

Configuration comes from

.env

Environment Variables

Never hardcode values.

---

# Logging

Use structured logging.

Every important operation should be traceable.

Simulation execution must be logged.

ETL execution must be logged.

Errors must be logged.

---

# Security

Authentication

Authorization

Input validation

Audit trail

Sensitive information must never be exposed.

---

# Testing Strategy

Unit Tests

Service Tests

Repository Tests

Integration Tests

API Tests

Simulation Tests

Regression Tests

---

# Error Handling

Errors should propagate through exceptions.

API converts exceptions into HTTP responses.

Business rules should never return HTTP responses.

---

# Documentation

Every public module should contain documentation.

Complex business rules must explain:

- objective

- inputs

- outputs

- assumptions

---

# Design Principles

Single Responsibility Principle

Open / Closed Principle

Dependency Inversion

Composition over inheritance

Explicit dependencies

Small functions

Pure business rules

Minimal coupling

High cohesion

---

# Evolution Strategy

New modules should integrate without modifying existing domains whenever possible.

Avoid monolithic services.

Favor domain-oriented organization.

---

# AI Assistant Notes

Before modifying any module:

Read:

AI_RULES.md

project.md

Relevant domain documentation.

Respect layer responsibilities.

Do not bypass architecture.

When uncertain,

stop,

explain,

ask.

---

End of document.
