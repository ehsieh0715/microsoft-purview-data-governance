# Data Governance Roles and Responsibilities

## Purpose

This document defines the key governance roles and responsibilities used across the Customer, Billing, Metering, and Tariff data domains.

## Governance Roles

### Data Owner

Accountable for the quality, use, protection, and governance of data within a business domain.

Key responsibilities include:

- Approving material governance decisions
- Providing accountability for domain-level data quality
- Approving significant remediation or access decisions where required
- Resolving or escalating issues beyond the Data Steward's authority

### Data Steward

Responsible for the day-to-day governance of data within a business domain.

Key responsibilities include:

- Maintaining business definitions and metadata
- Defining and reviewing data quality requirements
- Investigating identified data quality issues
- Determining root causes and proposing remediation actions
- Coordinating remediation and revalidation
- Escalating material or unresolved issues to the Data Owner

### Data Custodian

Responsible for the technical management of data platforms and governed data assets.

Key responsibilities include:

- Maintaining technical storage and availability
- Implementing approved access controls
- Supporting data security and platform controls
- Applying technical changes according to approved governance decisions

### Data Governance Analyst

Coordinates governance activities across domains and supports the operation of the governance framework.

Key responsibilities include:

- Maintaining governance standards and documentation
- Supporting Data Owners and Data Stewards
- Monitoring data quality and governance KPIs
- Coordinating issue and remediation reporting
- Supporting cross-domain governance activities

### Data Governance Forum

Provides cross-functional oversight of governance priorities, material data quality issues, policy compliance, and escalations.

The forum is responsible for resolving cross-domain conflicts and governance matters that cannot be resolved within an individual data domain.

## Domain Ownership

| Data Domain | Data Owner | Data Steward |
| --- | --- | --- |
| Customer | Head of Customer Operations | Customer Data Steward |
| Billing | Finance Director | Billing Data Steward |
| Metering | Head of Energy Operations | Metering Data Steward |
| Tariff | Commercial Director | Commercial Data Steward |

The Metering domain covers both meter master data and meter reading data.

## Responsibility Matrix

| Activity | Data Owner | Data Steward | Data Custodian | Data Governance Analyst | Governance Forum |
| --- | --- | --- | --- | --- | --- |
| Business definitions | Approve | Maintain | Support | Coordinate | Resolve conflicts |
| Data quality rules | Approve material requirements | Define and review | Support implementation | Monitor | Review material issues |
| Issue investigation | Escalation point | Lead | Technical support | Coordinate | Review escalations |
| Remediation | Approve where required | Propose and coordinate | Implement technical changes | Track and report | Resolve escalations |
| Data access | Approve where required | Review | Provision | Support governance process | Resolve exceptions |
| Governance KPIs | Review | Provide domain context | Support | Monitor and report | Review |