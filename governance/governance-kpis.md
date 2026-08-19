# Data Governance KPIs

## Purpose

This document defines governance KPIs used to monitor data quality, governance coverage, issue management, and remediation performance across the demonstration data domains.

The KPIs are designed to support regular reporting to Data Owners, Data Stewards, and the Data Governance Forum.

## KPI Definitions

| KPI | Definition | Calculation | Target |
| --- | --- | --- | --- |
| Data Quality Rule Pass Rate | Percentage of data quality rules meeting their defined target | Passed rules / Total rules | >= 95% |
| Open Data Quality Issues | Number of identified data quality issues requiring investigation or remediation | Count of open issues | 0 Critical issues |
| Critical Data Quality Issues | Number of identified issues classified as Critical | Count of Critical issues | 0 |
| Domain Data Quality Score | Percentage of rules passing within each data domain | Passed domain rules / Total domain rules | >= 95% |
| Remediation Validation Rate | Percentage of identified issues that pass revalidation after approved remediation | Successfully revalidated issues / Remediated issues | 100% |
| Ownership Coverage | Percentage of governed domains with assigned Data Owners | Domains with assigned owners / Total domains | 100% |
| Stewardship Coverage | Percentage of governed domains with assigned Data Stewards | Domains with assigned stewards / Total domains | 100% |
| Glossary Coverage | Percentage of identified priority business concepts represented in the governed glossary | Governed glossary terms / Identified priority terms | >= 95% |

## Current Raw Data Results

Based on validation of the raw datasets:

| KPI | Current Result | Status |
| --- | ---: | --- |
| Data Quality Rule Pass Rate | 88.9% | Below Target |
| Open Data Quality Issues | 3 | Action Required |
| Critical Data Quality Issues | 1 | Action Required |
| Ownership Coverage | 100% | Meets Target |
| Stewardship Coverage | 100% | Meets Target |

## Domain Data Quality Scores

| Domain | Passed Rules | Total Rules | Score |
| --- | ---: | ---: | ---: |
| Customer | 5 | 6 | 83.3% |
| Billing | 6 | 6 | 100% |
| Metering | 8 | 10 | 80% |
| Tariff | 5 | 5 | 100% |

Metering combines the rules applied to the `meters` and `meter_readings` datasets because both datasets belong to the Metering governance domain.

## Remediation Results

Approved remediation actions are applied to the curated data layer and the same data quality rules are rerun to validate the outcome.

| KPI | Raw | Curated |
| --- | ---: | ---: |
| Rules Passed | 24 / 27 | 27 / 27 |
| Data Quality Rule Pass Rate | 88.9% | 100% |
| Failed Records | 3 | 0 |
| Critical Data Quality Issues | 1 | 0 |

All three identified data quality failures pass revalidation after the approved remediation actions are applied to the curated datasets.

The resulting Remediation Validation Rate for the demonstration workflow is therefore **100%**.

## Governance Reporting Process

Governance KPIs should be reviewed on a defined reporting cadence and presented to the Data Governance Forum.

The review should include:

- Overall data quality performance
- Domain-level quality trends
- Open and Critical issues
- Remediation and revalidation outcomes
- Ownership or stewardship gaps
- Glossary and metadata coverage
- Policy or compliance exceptions

Material deterioration or unresolved Critical issues should be escalated to the relevant Data Owner and, where appropriate, senior leadership.

## Production Considerations

The KPI targets and current results in this repository are illustrative and based on synthetic demonstration data.

In a production environment, KPI targets, reporting cadence, escalation thresholds, and remediation service levels would be agreed with relevant business, governance, technical, and regulatory stakeholders.