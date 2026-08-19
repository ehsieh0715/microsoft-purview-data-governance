# Data Governance Operating Model

## Purpose

This operating model defines how data governance responsibilities, decision-making, data quality management, access control, issue remediation, and escalation work together across the demonstration energy data environment.

The model covers the Customer, Billing, Metering, and Tariff data domains.

## Governance Structure

| Role | Primary Responsibility |
| --- | --- |
| Data Governance Forum | Provides cross-domain governance oversight, resolves escalated issues, and reviews governance performance |
| Data Owner | Accountable for data within a business domain and approves material governance decisions |
| Data Steward | Maintains definitions, monitors data quality, investigates issues, coordinates remediation, and supports governance processes |
| Data & Analytics | Implements data quality monitoring, metadata practices, reporting, and governance enablement |
| IT / Platform Administration | Implements approved technical access and platform controls |
| Data Protection / Legal / Security | Provides specialist oversight for privacy, regulatory, legal, and security matters |

## Domain Accountability

| Domain | Data Owner | Data Steward |
| --- | --- | --- |
| Customer | Head of Customer Operations | Customer Data Steward |
| Billing | Finance Director | Billing Data Steward |
| Metering | Head of Energy Operations | Metering Data Steward |
| Tariff | Commercial Director | Commercial Data Steward |

The Metering domain includes both meter master data and meter reading data.

## Governance Lifecycle

### 1. Define

Business terminology, ownership, data definitions, quality expectations, and classification requirements are established.

Supporting artefacts:

- Business Glossary
- Data Dictionary
- Roles and Responsibilities
- Data Classification Framework

### 2. Govern

Governance policies define how data should be accessed, protected, maintained, and managed.

Supporting artefacts:

- Data Access Control Policy
- Data Protection and Privacy Governance
- Data Quality Framework

### 3. Monitor

Automated data quality checks evaluate raw datasets against configured rules and thresholds.

Outputs include:

- Rule-level data quality results
- Failed record identification
- Domain-level quality metrics
- Governance KPIs

### 4. Manage Issues

Failed data quality records are converted into governance issues and enriched with domain, severity, Data Owner, and Data Steward information.

Issues are assigned to the appropriate governance roles for investigation and prioritised according to severity and business impact.

### 5. Remediate

Data Stewards investigate root causes and determine appropriate corrective actions with relevant business or technical teams.

Approved remediation actions are applied to generate curated datasets while the original raw data is retained unchanged.

In a production environment, some issues may require correction in the authoritative source system rather than downstream remediation.

### 6. Validate

The same data quality rules are rerun against the curated datasets after remediation.

Successful revalidation confirms whether the identified data quality failures have been resolved and the required quality thresholds are met.

### 7. Escalate

Critical, unresolved, cross-domain, regulatory, or ownership-related issues are escalated to the relevant Data Owner or Data Governance Forum.

## Decision and Escalation Model

| Scenario | Primary Responsibility | Escalation |
| --- | --- | --- |
| Business term definition | Data Steward | Data Owner |
| Material definition conflict | Data Owner | Data Governance Forum |
| Routine data quality issue | Data Steward | Data Owner |
| Critical data quality issue | Data Owner | Data Governance Forum |
| Remediation decision | Data Steward | Data Owner where material approval is required |
| Data access request | Data Steward / Data Owner | Data Governance Forum where required |
| Privacy concern | Data Protection / Legal | Appropriate senior governance body |
| Cross-domain ownership conflict | Data Owners | Data Governance Forum |

## Governance Reporting

The Data Governance Forum should periodically review:

- Data quality rule pass rates
- Domain data quality scores
- Open and Critical data quality issues
- Remediation and revalidation outcomes
- Ownership and stewardship coverage
- Metadata and glossary coverage
- Access or policy exceptions
- Material privacy or regulatory concerns

Governance KPIs provide a consistent mechanism for monitoring governance effectiveness and identifying areas requiring intervention.

## Microsoft Purview Implementation Mapping

In a Microsoft Purview environment, elements of this operating model could be supported through capabilities including:

- Data catalogue and metadata discovery
- Business glossary management
- Data classifications
- Sensitivity capabilities
- Data ownership and stewardship metadata
- Data quality monitoring
- Data lineage and discovery

Business accountability, governance decisions, issue remediation, and escalation remain organisational governance responsibilities supported by the platform.

## Demonstration Scope

This repository uses synthetic energy datasets and demonstration governance requirements.

The repository implements the data quality workflow using raw and curated data stages, configuration-driven validation, issue generation, remediation actions, and revalidation.

Roles, thresholds, permitted values, classifications, and governance processes were designed for portfolio purposes and would require review and approval by appropriate business, technical, privacy, and regulatory stakeholders before production use.