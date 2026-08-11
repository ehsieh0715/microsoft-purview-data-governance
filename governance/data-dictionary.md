# Enterprise Data Dictionary

## Purpose

This data dictionary documents the technical metadata for the datasets used in the energy data governance project.

It provides consistent definitions for data elements across the Customer, Metering, Billing, and Tariff domains and maps technical fields to relevant business glossary terms.

The dictionary is designed as a Purview-aligned governance artefact demonstrating how technical metadata, business definitions, ownership, and data quality requirements can be connected within an enterprise data catalogue.

## Customer Domain

**Dataset:** `customers.csv`  
**Description:** Customer master data containing identity, contact, customer type, and account status information.

| Column | Data Type | Description | Nullable | Business Term |
|---|---|---|---|---|
| customer_id | String | Unique identifier assigned to a customer. | No | Customer ID |
| first_name | String | Customer's first name. | No | — |
| last_name | String | Customer's last name. | No | — |
| email | String | Email address associated with the customer account. | No | Customer Email |
| phone | String | Telephone number associated with the customer account. | Yes | — |
| address | String | Postal address associated with the customer account. | Yes | — |
| customer_type | String | Category assigned to the customer account. | No | Customer Type |
| status | String | Current operational status of the customer account. | No | Active Customer |

## Metering Domain

**Dataset:** `meter_readings.csv`  
**Description:** Meter-level energy consumption readings associated with customers over time.

| Column | Data Type | Description | Nullable | Business Term |
|---|---|---|---|---|
| meter_id | String | Unique identifier assigned to an energy meter. | No | Meter |
| customer_id | String | Identifier of the customer associated with the meter reading. | No | Customer ID |
| reading_date | Date | Date on which the meter reading was recorded. | No | Meter Reading |
| consumption_kwh | Decimal | Energy consumption recorded in kilowatt-hours (kWh). | No | Energy Consumption |

## Billing Domain

**Dataset:** `billing.csv`  
**Description:** Customer invoice and payment information used for billing operations.

| Column | Data Type | Description | Nullable | Business Term |
|---|---|---|---|---|
| invoice_id | String | Unique identifier assigned to an invoice. | No | Invoice |
| customer_id | String | Identifier of the customer associated with the invoice. | No | Customer ID |
| billing_date | Date | Date associated with the issuance of the invoice. | No | Billing Date |
| amount_eur | Decimal | Invoice amount denominated in euros. | No | Invoice Amount |
| payment_status | String | Current payment state of the invoice. | No | Payment Status |

## Tariff Domain

**Dataset:** `tariffs.csv`  
**Description:** Energy tariff information defining available pricing plans and unit rates.

| Column | Data Type | Description | Nullable | Business Term |
|---|---|---|---|---|
| tariff_id | String | Unique identifier assigned to an energy tariff. | No | Tariff |
| tariff_name | String | Business-facing name of the tariff. | No | Tariff Name |
| energy_type | String | Type of energy product associated with the tariff. | No | Energy Type |
| unit_rate | Decimal | Monetary charge applied per unit of energy consumption. | No | Unit Rate |

## Dataset Relationships

| Parent Dataset | Parent Field | Child Dataset | Child Field | Relationship |
|---|---|---|---|---|
| customers.csv | customer_id | meter_readings.csv | customer_id | One customer may have multiple meter readings |
| customers.csv | customer_id | billing.csv | customer_id | One customer may have multiple invoices |

These relationships are used to support referential integrity checks and cross-domain data quality monitoring.