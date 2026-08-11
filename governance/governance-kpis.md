# Data Governance KPIs

## Purpose

This document defines governance KPIs used to monitor data quality, governance coverage, issue management, and remediation performance across the demonstration data domains.

The KPIs are designed to support regular reporting to Data Owners, Data Stewards, and the Data Governance Forum.

## KPI Definitions

| KPI | Definition | Calculation | Target |
|---|---|---|---|
| Data Quality Rule Pass Rate | Percentage of data quality rules meeting their defined target | Passed rules / Total rules | >= 95% |
| Open Data Quality Issues | Number of unresolved data quality issues | Count of issues where status is not Closed | 0 Critical issues |
| Critical Data Quality Issues | Number of unresolved issues classified as Critical | Count of open Critical issues | 0 |
| Domain Data Quality Score | Percentage of rules passing within each data domain | Passed domain rules / Total domain rules | >= 95% |
| Remediation Completion Rate | Percentage of logged issues successfully remediated and closed | Closed issues / Total logged issues | >= 95% |
| Ownership Coverage | Percentage of governed domains with assigned Data Owners | Domains with assigned owners / Total domains | 100% |
| Stewardship Coverage | Percentage of governed domains with assigned Data Stewards | Domains with assigned stewards / Total domains | 100% |
| Glossary Coverage | Percentage of priority business concepts represented in the governed glossary | Governed glossary terms / Identified priority terms | >= 95% |

## Current Baseline

Based on the initial automated data quality run:

| KPI | Current Result | Status |
|---|---:|---|
| Data Quality Rule Pass Rate | 85% | Below Target |
| Open Data Quality Issues | 3 | Action Required |
| Critical Data Quality Issues | 1 | Action Required |
| Ownership Coverage | 100% | Meets Target |
| Stewardship Coverage | 100% | Meets Target |

## Domain Data Quality Scores

| Domain | Passed Rules | Total Rules | Score |
|---|---:|---:|---:|
| Customer | 4 | 5 | 80% |
| Billing | 6 | 6 | 100% |
| Metering | 2 | 4 | 50% |
| Tariff | 5 | 5 | 100% |

## Governance Reporting Process

Governance KPIs should be reviewed on a defined reporting cadence and presented to the Data Governance Forum.

The review should include:

- Overall data quality performance
- Domain-level quality trends
- Open and Critical issues
- Remediation progress
- Ownership or stewardship gaps
- Glossary and metadata coverage
- Policy or compliance exceptions

Material deteriorations or unresolved Critical issues should be escalated to the relevant Data Owner and, where appropriate, senior leadership.