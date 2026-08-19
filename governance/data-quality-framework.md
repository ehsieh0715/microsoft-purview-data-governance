# Data Quality Framework

## Purpose

This framework defines how data quality is measured, monitored, and governed across the Customer, Billing, Metering, and Tariff data domains.

Data quality rules are maintained as configuration and executed through a reusable Python rule engine. Failed records are converted into governance issues with defined ownership, followed by approved remediation and revalidation.

## Data Quality Dimensions

The framework evaluates data using the following dimensions:

| Dimension | Description | Example |
| --- | --- | --- |
| Completeness | Required data is populated. | Customer ID must not be null. |
| Uniqueness | Identifiers expected to be unique contain no duplicates. | Reading ID must be unique. |
| Validity | Values conform to defined formats, ranges, or permitted values. | Energy consumption must not be negative. |
| Referential Integrity | Relationships between datasets reference valid records. | A meter must reference an existing customer. |

## Rule Configuration

Data quality rules are maintained in:

`config/data_quality_rules.csv`

Each rule defines:

| Field | Purpose |
| --- | --- |
| `rule_id` | Unique identifier for the data quality rule |
| `dataset` | Dataset evaluated by the rule |
| `column` | Column evaluated by the rule |
| `dimension` | Data quality dimension |
| `check_type` | Validation logic executed by the rule engine |
| `target` | Minimum required pass rate |
| `severity` | Governance severity assigned when the rule fails |
| `record_id_column` | Identifier used to trace failed records |
| `parameter` | Optional configuration required by the check |

Separating rule configuration from execution logic allows validation requirements to be maintained without hard coding individual rules into the Python workflow.

## Data Quality Rules

### Customer

| Rule ID | Column | Dimension | Check | Target | Severity |
| --- | --- | --- | --- | ---: | --- |
| DQ-CUS-001 | `customer_id` | Completeness | Not null | 100% | Critical |
| DQ-CUS-002 | `customer_id` | Uniqueness | Unique | 100% | Critical |
| DQ-CUS-003 | `email` | Validity | Email format | 99% | High |
| DQ-CUS-004 | `customer_type` | Validity | Residential or Commercial | 100% | Medium |
| DQ-CUS-005 | `tariff_id` | Referential Integrity | References `tariffs.tariff_id` | 100% | High |
| DQ-CUS-006 | `status` | Validity | Active or Inactive | 100% | High |

### Billing

| Rule ID | Column | Dimension | Check | Target | Severity |
| --- | --- | --- | --- | ---: | --- |
| DQ-BIL-001 | `invoice_id` | Completeness | Not null | 100% | Critical |
| DQ-BIL-002 | `invoice_id` | Uniqueness | Unique | 100% | Critical |
| DQ-BIL-003 | `customer_id` | Referential Integrity | References `customers.customer_id` | 100% | Critical |
| DQ-BIL-004 | `amount_eur` | Validity | Minimum value 0 | 100% | High |
| DQ-BIL-005 | `payment_status` | Validity | Paid or Outstanding | 100% | High |
| DQ-BIL-006 | `billing_date` | Completeness | Not null | 100% | High |

### Meter

| Rule ID | Column | Dimension | Check | Target | Severity |
| --- | --- | --- | --- | ---: | --- |
| DQ-MTR-001 | `meter_id` | Completeness | Not null | 100% | Critical |
| DQ-MTR-002 | `meter_id` | Uniqueness | Unique | 100% | Critical |
| DQ-MTR-003 | `customer_id` | Referential Integrity | References `customers.customer_id` | 100% | Critical |
| DQ-MTR-004 | `meter_type` | Validity | Smart or Traditional | 100% | Medium |
| DQ-MTR-005 | `status` | Validity | Active or Inactive | 100% | High |

### Meter Reading

| Rule ID | Column | Dimension | Check | Target | Severity |
| --- | --- | --- | --- | ---: | --- |
| DQ-MET-001 | `reading_id` | Completeness | Not null | 100% | Critical |
| DQ-MET-002 | `reading_id` | Uniqueness | Unique | 100% | Critical |
| DQ-MET-003 | `meter_id` | Referential Integrity | References `meters.meter_id` | 100% | Critical |
| DQ-MET-004 | `reading_date` | Completeness | Not null | 100% | High |
| DQ-MET-005 | `consumption_kwh` | Validity | Minimum value 0 | 100% | High |

### Tariff

| Rule ID | Column | Dimension | Check | Target | Severity |
| --- | --- | --- | --- | ---: | --- |
| DQ-TAR-001 | `tariff_id` | Completeness | Not null | 100% | Critical |
| DQ-TAR-002 | `tariff_id` | Uniqueness | Unique | 100% | Critical |
| DQ-TAR-003 | `tariff_name` | Completeness | Not null | 100% | High |
| DQ-TAR-004 | `energy_type` | Validity | Electricity or Gas | 100% | High |
| DQ-TAR-005 | `unit_rate` | Validity | Greater than 0 | 100% | High |

The framework currently contains **27 configured data quality rules**.

## Automated Validation Workflow

The validation workflow can be executed against either the raw or curated data stage.

```text
data/raw/
    ↓
Configured Data Quality Rules
    ↓
Python Rule Engine
    ↓
Rule Results + Failed Records
    ↓
Governance Issue Register
    ↓
Approved Remediation Actions
    ↓
data/curated/
    ↓
Data Quality Revalidation
```

Baseline validation is performed against `data/raw/`. Raw datasets are retained unchanged to preserve the original source state.

Approved remediation actions are applied to copies of the raw datasets to generate `data/curated/`. The same rule set is then executed against the curated datasets to verify the remediation outcome.

## Validation Outputs

Each validation run produces:

`data-quality-results.csv`

Contains rule-level results including records checked, failed records, pass rate, target, status, and severity.

`failed-records.csv`

Contains record-level details for individual data quality failures, including the affected record and invalid value.

Outputs are stored separately by data stage:

```text
data-quality/results/
├── raw/
│   ├── data-quality-results.csv
│   ├── failed-records.csv
│   └── data-quality-issues.csv
└── curated/
    ├── data-quality-results.csv
    └── failed-records.csv
```

The governance issue register is generated from raw failures because it represents issues detected in the source state before remediation.

## Baseline and Revalidation Results

The synthetic raw datasets intentionally contain three data quality issues to demonstrate detection, governance ownership, remediation, and revalidation.

| Metric | Raw | Curated |
| --- | ---: | ---: |
| Rules Passed | 24 / 27 | 27 / 27 |
| Rule Pass Rate | 88.9% | 100% |
| Failed Records | 3 | 0 |
| Critical Issues | 1 | 0 |
| High Issues | 2 | 0 |

The raw failures are:

| Rule ID | Dataset | Record | Issue |
| --- | --- | --- | --- |
| DQ-CUS-003 | `customers` | C002 | Invalid customer email format |
| DQ-MTR-003 | `meters` | M004 | Meter references an unknown customer |
| DQ-MET-005 | `meter_readings` | R002 | Negative energy consumption |

These failures are retained in the raw datasets so the baseline condition remains reproducible.

## Severity Model

| Severity | Meaning | Expected Governance Response |
| --- | --- | --- |
| Critical | Issue may compromise key relationships, identifiers, or essential data integrity. | Immediate investigation and escalation to the responsible Data Owner and Data Steward. |
| High | Issue materially affects data reliability or business use. | Prioritised investigation and remediation by the responsible Data Steward. |
| Medium | Issue affects data consistency but has lower immediate business impact. | Review and remediation through the normal governance process. |

Severity indicates the governance priority of a failed rule. Remediation decisions still require investigation and business context.

## Governance Responsibilities

Data Stewards are responsible for reviewing failed records, investigating root causes, proposing remediation actions, and confirming that corrected data meets the relevant quality requirements.

Data Owners are accountable for data quality within their domain and approve significant remediation or escalation decisions where required.

The Data Governance Forum provides escalation and cross-domain decision support for issues that cannot be resolved within a single data domain.

## Production Considerations

The datasets, thresholds, severity levels, and governance roles in this repository are illustrative.

In a production environment, data quality rules and thresholds would be agreed with relevant business and technical stakeholders. Validation would typically run as part of scheduled data pipelines, with monitoring, alerting, issue management, lineage, and remediation integrated with enterprise data governance and operational platforms.
