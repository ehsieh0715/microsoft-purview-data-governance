# Microsoft Purview Data Governance for Energy Data

A data governance portfolio project built around four synthetic energy data domains: Customer, Billing, Metering, and Tariff.

The project includes a business glossary, data dictionary, ownership and stewardship model, data classification, access controls, governance KPIs, and an automated Python data quality framework.

The data quality pipeline evaluates 20 configurable rules, identifies failed records, generates governance issues, and supports remediation and validation.

## Contents

- [Architecture](#architecture)
- [Data Domains](#data-domains)
- [Governance Framework](#governance-framework)
- [Configuration-Driven Data Quality Framework](#configuration-driven-data-quality-framework)
- [Automated Data Quality Monitoring](#automated-data-quality-monitoring)
- [Governance Issue Generation](#governance-issue-generation)
- [Data Quality Results](#data-quality-results)
- [Microsoft Purview Mapping](#microsoft-purview-mapping)
- [Azure and Microsoft Purview Environment](#azure-and-microsoft-purview-environment)
- [Repository Structure](#repository-structure)
- [Technologies](#technologies)
- [Running the Project](#running-the-project)
- [Project Scope](#project-scope)

## Architecture

``` text
Synthetic Energy Data
        │
        ▼
Data Quality Rules + Governance Configuration
        │
        ▼
Python Rule Engine
        │
        ├── Rule Results
        │
        └── Failed Records
                │
                ▼
          Issue Register
                │
                ▼
      Steward Investigation
                │
                ▼
           Remediation
                │
                ▼
             Recheck
```

## Data Domains

| Domain | Description |
| --- | --- |
| Customer | Customer identity, status, and contact information |
| Billing | Customer invoices, charges, and payment information |
| Metering | Meter readings and energy consumption |
| Tariff | Energy products, pricing plans, and unit rates |

## Governance Framework

| Area | Implementation |
| --- | --- |
| Metadata | Business glossary and data dictionary |
| Accountability | Data Owner and Data Steward model |
| Classification | Data classification and sensitivity framework |
| Data Quality | Configurable rules, automated checks, and issue detection |
| Issue Management | Ownership, severity, escalation, and remediation workflow |
| Access & Privacy | Access control and GDPR-aligned governance |
| Monitoring | Governance KPIs and domain-level DQ scores |
| Operating Model | Governance Forum, decision rights, and escalation model |

Detailed governance documentation is available in the [governance](governance/) directory.


## Configuration-Driven Data Quality Framework

Data quality rules are maintained separately from execution logic in:

`config/data_quality_rules.csv`

The rule engine currently supports:

-   Completeness checks
-   Uniqueness checks
-   Allowed-value validation
-   Email format validation
-   Minimum-value validation
-   Referential integrity checks

Rules, thresholds, severity levels, and permitted values are maintained in configuration rather than hard-coded into the execution logic.

## Automated Data Quality Monitoring

Run:

``` bash
python scripts/data_quality_checks.py
```

The pipeline loads the datasets and configured rules, executes each check through the rule engine, calculates pass rates, and records failed rows.

Outputs are written to `data-quality/results/`:

- `data-quality-results.csv`
- `failed-records.csv`

For this case study, outputs from the initial and post-remediation runs were archived under `baseline/` and `remediated/` to preserve the before-and-after results.


## Governance Issue Generation

Run:

``` bash
python scripts/generate_issue_register.py
```

Failed records are combined with `config/governance_mapping.csv` to generate a Data Quality Issue Register with domain, severity, Data Owner, Data Steward, and issue context.

Root cause and remediation fields remain manual because they require Data Steward investigation.

The generated issue register is also archived with the corresponding run results.

## Data Quality Results
The baseline dataset intentionally contained three quality issues to demonstrate detection and remediation.

Snapshots from both runs are retained in `data-quality/results/baseline/` and `data-quality/results/remediated/`.

| Metric | Baseline | After Remediation |
| --- | ---: | ---: |
| Rules Passed | 17 / 20 | 20 / 20 |
| Rule Pass Rate | 85% | 100% |
| Failed Records | 3 | 0 |
| Critical Issues | 1 | 0 |
| High Issues | 2 | 0 |

### Detected Issues

| Rule | Domain | Severity | Issue |
| --- | --- | --- | --- |
| DQ-CUS-003 | Customer | High | Invalid customer email format |
| DQ-MET-002 | Metering | Critical | Unknown customer referenced by meter reading |
| DQ-MET-004 | Metering | High | Negative energy consumption |

The affected records were corrected and the checks rerun, bringing all 20 rules within their defined thresholds.


## Microsoft Purview Mapping

The governance framework maps to the following Microsoft Purview capabilities:

| Governance Requirement | Purview Capability |
| --- | --- |
| Metadata discovery | Data Catalog |
| Business terminology | Business Glossary |
| Sensitive data identification | Classifications |
| Data protection | Sensitivity labels |
| Ownership and stewardship | Governance metadata |
| Data quality monitoring | Data Quality |
| Data discovery | Unified Catalog |
| Technical relationships | Data lineage |

## Azure and Microsoft Purview Environment

Azure Storage was provisioned and the four synthetic datasets were uploaded to Azure Blob Storage.

Microsoft Purview Enterprise provisioning was attempted, but the regions permitted by the Azure subscription did not support successful deployment of the required Purview resource. This prevented data source registration, scanning, catalogue ingestion, and automated classification from being completed.

The platform-independent governance components were therefore implemented directly in this repository, with Python used for automated data quality monitoring and issue generation. The documentation maps these components to their intended Microsoft Purview implementation.

The Purview components in this repository represent implementation design and platform mapping rather than production Microsoft Purview administration.

## Repository Structure

``` text
.
├── config/
│   ├── data_quality_rules.csv
│   └── governance_mapping.csv
├── data/
├── data-quality/
│   └── results/
│       ├── baseline/
│       └── remediated/
├── governance/
├── screenshots/
├── scripts/
│   ├── data_quality_checks.py
│   ├── generate_issue_register.py
│   └── rule_engine.py
├── README.md
└── requirements.txt
```

## Technologies

- Microsoft Azure / Azure Blob Storage
- Microsoft Purview governance concepts
- Python / pandas
- Git / GitHub

## Running the Project

Create and activate a virtual environment:

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

Run data quality monitoring:

``` bash
python scripts/data_quality_checks.py
```

Generate the issue register:

``` bash
python scripts/generate_issue_register.py
```

## Project Scope

All datasets are synthetic and created for portfolio use. Governance roles, thresholds, classifications, and policies are illustrative and would require review and approval by the relevant business, data, technical, privacy, and regulatory stakeholders before production use.