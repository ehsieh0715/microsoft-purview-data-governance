# Enterprise Data Dictionary

## Purpose

This data dictionary documents the technical metadata for the synthetic datasets used in the energy data governance project.

It provides consistent definitions for data elements across the Customer, Metering, Billing, and Tariff domains and connects technical fields to relevant business glossary terms.

The dictionary is designed as a Purview-aligned governance artefact demonstrating how technical metadata, business definitions, ownership, relationships, and data quality requirements can be connected within an enterprise data catalogue.

## Customer Domain

Dataset: `customers.csv`

Grain: One row per customer.

Description: Customer master data containing identity, contact, customer type, tariff assignment, and account status information.

| Column          | Data Type | Description                                            | Nullable | Key / Relationship                | Business Term   |
| --------------- | --------- | ------------------------------------------------------ | -------- | --------------------------------- | --------------- |
| `customer_id`   | String    | Unique identifier assigned to a customer.              | No       | Primary Key                       | Customer ID     |
| `first_name`    | String    | Customer's first name.                                 | No       |                                   |                 |
| `last_name`     | String    | Customer's last name.                                  | No       |                                   |                 |
| `email`         | String    | Email address associated with the customer account.    | No       |                                   | Customer Email  |
| `phone`         | String    | Telephone number associated with the customer account. | Yes      |                                   |                 |
| `address`       | String    | Postal address associated with the customer account.   | Yes      |                                   |                 |
| `customer_type` | String    | Category assigned to the customer account.             | No       |                                   | Customer Type   |
| `tariff_id`     | String    | Identifier of the tariff assigned to the customer.     | No       | Foreign Key → `tariffs.tariff_id` | Tariff          |
| `status`        | String    | Current operational status of the customer account.    | No       |                                   | Active Customer |

## Metering Domain

### Meter Dataset

Dataset: `meters.csv`

Grain: One row per meter.

Description: Meter master data describing meter ownership, type, installation date, and operational status.

| Column              | Data Type | Description                                           | Nullable | Key / Relationship                    | Business Term           |
| ------------------- | --------- | ----------------------------------------------------- | -------- | ------------------------------------- | ----------------------- |
| `meter_id`          | String    | Unique identifier assigned to an energy meter.        | No       | Primary Key                           | Meter                   |
| `customer_id`       | String    | Identifier of the customer associated with the meter. | No       | Foreign Key → `customers.customer_id` | Customer ID             |
| `meter_type`        | String    | Type of meter installed for the customer.             | No       |                                       | Meter Type              |
| `installation_date` | Date      | Date on which the meter was installed.                | No       |                                       | Meter Installation Date |
| `status`            | String    | Current operational status of the meter.              | No       |                                       | Meter Status            |

### Meter Reading Dataset

Dataset: `meter_readings.csv`

Grain: One row per meter reading.

Description: Daily energy consumption readings recorded for individual meters.

| Column            | Data Type | Description                                          | Nullable | Key / Relationship              | Business Term      |
| ----------------- | --------- | ---------------------------------------------------- | -------- | ------------------------------- | ------------------ |
| `reading_id`      | String    | Unique identifier assigned to a meter reading.       | No       | Primary Key                     | Meter Reading      |
| `meter_id`        | String    | Identifier of the meter associated with the reading. | No       | Foreign Key → `meters.meter_id` | Meter              |
| `reading_date`    | Date      | Date on which the meter reading was recorded.        | No       |                                 | Meter Reading Date |
| `consumption_kwh` | Decimal   | Energy consumption recorded in kilowatt-hours.       | No       |                                 | Energy Consumption |

## Billing Domain

Dataset: `billing.csv`

Grain: One row per customer invoice.

Description: Customer invoice and payment information used for billing operations.

| Column           | Data Type | Description                                             | Nullable | Key / Relationship                    | Business Term  |
| ---------------- | --------- | ------------------------------------------------------- | -------- | ------------------------------------- | -------------- |
| `invoice_id`     | String    | Unique identifier assigned to an invoice.               | No       | Primary Key                           | Invoice        |
| `customer_id`    | String    | Identifier of the customer associated with the invoice. | No       | Foreign Key → `customers.customer_id` | Customer ID    |
| `billing_date`   | Date      | Date associated with the issuance of the invoice.       | No       |                                       | Billing Date   |
| `amount_eur`     | Decimal   | Invoice amount denominated in euros.                    | No       |                                       | Invoice Amount |
| `payment_status` | String    | Current payment state of the invoice.                   | No       |                                       | Payment Status |

Billing amounts are synthetic and are not calculated directly from the sample meter readings and tariff rates. The billing dataset is included to demonstrate cross-domain governance relationships rather than a complete utility billing calculation process.

## Tariff Domain

Dataset: `tariffs.csv`

Grain: One row per tariff.

Description: Energy tariff reference data defining available pricing plans and unit rates.

| Column        | Data Type | Description                                             | Nullable | Key / Relationship | Business Term |
| ------------- | --------- | ------------------------------------------------------- | -------- | ------------------ | ------------- |
| `tariff_id`   | String    | Unique identifier assigned to an energy tariff.         | No       | Primary Key        | Tariff        |
| `tariff_name` | String    | Business-facing name of the tariff.                     | No       |                    | Tariff Name   |
| `energy_type` | String    | Type of energy product associated with the tariff.      | No       |                    | Energy Type   |
| `unit_rate`   | Decimal   | Monetary charge applied per unit of energy consumption. | No       |                    | Unit Rate     |

## Dataset Relationships

| Parent Dataset  | Parent Field  | Child Dataset        | Child Field   | Relationship                                           |
| --------------- | ------------- | -------------------- | ------------- | ------------------------------------------------------ |
| `tariffs.csv`   | `tariff_id`   | `customers.csv`      | `tariff_id`   | One tariff may be assigned to multiple customers       |
| `customers.csv` | `customer_id` | `meters.csv`         | `customer_id` | One customer may be associated with one or more meters |
| `meters.csv`    | `meter_id`    | `meter_readings.csv` | `meter_id`    | One meter may have multiple meter readings             |
| `customers.csv` | `customer_id` | `billing.csv`        | `customer_id` | One customer may have multiple invoices                |

These relationships support cross-domain referential integrity checks and make dependencies between governed datasets explicit.

## Data Lifecycle

The project separates source-like data from remediated data:

```text
data/raw/
    ↓
Data Quality Validation
    ↓
Failed Records
    ↓
Governance Issue Register
    ↓
Approved Remediation Actions
    ↓
data/curated/
    ↓
Data Quality Revalidation
```

Files under `data/raw/` represent the immutable synthetic source state used for baseline validation.

Files under `data/curated/` are generated from the raw datasets after approved remediation actions are applied. Raw datasets are retained unchanged so that data quality issues and remediation outcomes remain reproducible and auditable.
