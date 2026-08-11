# Data Quality Framework

## Purpose

This framework defines the approach used to monitor, assess, and manage data quality across the Customer, Billing, Metering, and Tariff data domains.

The objective is to establish measurable data quality expectations, assign accountability, identify data issues, and support consistent remediation and escalation.

Data quality rules are defined according to business requirements and are designed to be implemented through automated monitoring where appropriate.

## Data Quality Dimensions

| Dimension | Definition | Example |
|---|---|---|
| Completeness | Required data is present and not missing. | Every invoice must contain a customer ID. |
| Uniqueness | Records or identifiers that should be unique contain no duplicates. | Each invoice ID must be unique. |
| Validity | Data conforms to defined formats, domains, or business rules. | Invoice amounts must not be negative. |
| Consistency | Related data follows consistent definitions and values across datasets. | Customer IDs follow the same identifier convention across datasets. |
| Referential Integrity | References to records in another dataset correspond to valid existing records. | Every billing customer ID must exist in the customer dataset. |
| Timeliness | Data is available and recorded within the required business timeframe. | Meter readings should be received within the expected reporting period. |

## Data Quality Rule Severity

| Severity | Definition | Expected Response |
|---|---|---|
| Critical | Issue could materially affect regulatory reporting, customer outcomes, financial reporting, or critical operations. | Immediate investigation and escalation to the relevant Data Owner. |
| High | Significant issue affecting important analytics or operational processes. | Prioritised remediation by the responsible Data Steward. |
| Medium | Issue has limited business impact but should be corrected. | Track and remediate through normal governance processes. |
| Low | Minor issue with minimal immediate business impact. | Monitor and resolve during routine maintenance. |

## Customer Domain Rules

| Rule ID | Data Element | Dimension | Rule | Target | Severity |
|---|---|---|---|---|---|
| DQ-CUS-001 | customer_id | Completeness | Customer ID must not be null. | 100% | Critical |
| DQ-CUS-002 | customer_id | Uniqueness | Customer ID must be unique. | 100% | Critical |
| DQ-CUS-003 | email | Validity | Non-null email addresses must follow a valid email format. | >= 99% | High |
| DQ-CUS-004 | customer_type | Validity | Customer type must be either `Residential` or `Commercial`. | 100% | Medium |
| DQ-CUS-005 | status | Validity | Customer status must be either `Active` or `Inactive`. | 100% | High |

## Billing Domain Rules

| Rule ID | Data Element | Dimension | Rule | Target | Severity |
|---|---|---|---|---|---|
| DQ-BIL-001 | invoice_id | Completeness | Invoice ID must not be null. | 100% | Critical |
| DQ-BIL-002 | invoice_id | Uniqueness | Invoice ID must be unique. | 100% | Critical |
| DQ-BIL-003 | customer_id | Referential Integrity | Every billing customer ID must exist in the customer dataset. | 100% | Critical |
| DQ-BIL-004 | amount_eur | Validity | Invoice amount must be greater than or equal to zero. | 100% | High |
| DQ-BIL-005 | payment_status | Validity | Payment status must be either `Paid` or `Outstanding`. | 100% | High |
| DQ-BIL-006 | billing_date | Completeness | Billing date must not be null. | 100% | High |

## Metering Domain Rules

| Rule ID | Data Element | Dimension | Rule | Target | Severity |
|---|---|---|---|---|---|
| DQ-MET-001 | meter_id | Completeness | Meter ID must not be null. | 100% | Critical |
| DQ-MET-002 | customer_id | Referential Integrity | Every metering customer ID must exist in the customer dataset. | 100% | Critical |
| DQ-MET-003 | reading_date | Completeness | Reading date must not be null. | 100% | High |
| DQ-MET-004 | consumption_kwh | Validity | Energy consumption must be greater than or equal to zero. | 100% | High |

## Tariff Domain Rules

| Rule ID | Data Element | Dimension | Rule | Target | Severity |
|---|---|---|---|---|---|
| DQ-TAR-001 | tariff_id | Completeness | Tariff ID must not be null. | 100% | Critical |
| DQ-TAR-002 | tariff_id | Uniqueness | Tariff ID must be unique. | 100% | Critical |
| DQ-TAR-003 | tariff_name | Completeness | Tariff name must not be null. | 100% | High |
| DQ-TAR-004 | energy_type | Validity | Energy type must be either `Electricity` or `Gas`. | 100% | High |
| DQ-TAR-005 | unit_rate | Validity | Unit rate must be greater than zero. | 100% | High |

## Data Quality Monitoring Process

1. Data quality rules are defined with the relevant business and technical context.
2. Data Stewards review rules, thresholds, and expected values for their domains.
3. Automated checks evaluate datasets against approved data quality rules.
4. Results are recorded and compared against defined quality targets.
5. Failed rules generate data quality issues for investigation.
6. Data Stewards investigate root causes and coordinate remediation.
7. Critical or unresolved issues are escalated to the relevant Data Owner and, where appropriate, the Data Governance Forum.
8. Data quality trends and remediation status are reported through governance KPIs.

## Microsoft Purview Implementation Mapping

In a Microsoft Purview Enterprise environment, applicable data quality rules could be configured and monitored using Purview data quality capabilities.

The rules in this repository represent governance requirements defined for the demonstration environment. Automated execution in this project is implemented separately using Python to demonstrate rule validation, monitoring, and reporting.

## Assumptions

The thresholds and severity levels defined in this project are demonstration governance requirements. In a production environment, these would be reviewed and approved by the relevant Data Owners and Data Stewards based on business, operational, and regulatory requirements.

The approved value sets used in this demonstration are synthetic business rules defined for the portfolio environment. In a production setting, permitted values would be agreed with the relevant Data Owners and Data Stewards and validated against authoritative source systems.