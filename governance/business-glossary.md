# Enterprise Business Glossary

## Purpose

This glossary defines consistent business terminology across the energy data domains used in this project.

The objective is to establish shared business definitions that support consistent reporting, analytics, data quality, and governance.

The glossary demonstrates how business terms can be governed through defined Data Owner and Data Steward responsibilities and mapped to corresponding data elements in a Microsoft Purview environment.

## Data Domains

| Domain | Description |
| --- | --- |
| Customer | Customer identity, account status, type, contact information, and tariff assignment |
| Billing | Customer invoices, charges, and payment status |
| Metering | Meter information, meter readings, and energy consumption |
| Tariff | Energy pricing plans, energy types, and unit rates |

## Business Terms

| Term | Definition | Domain | Data Owner | Data Steward | Related Data Element | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Customer | An individual or organisation receiving energy services from the company. | Customer | Head of Customer Operations | Customer Data Steward | `customers.customer_id` | Proposed |
| Customer ID | A unique identifier assigned to each customer. | Customer | Head of Customer Operations | Customer Data Steward | `customers.customer_id` | Proposed |
| Customer Type | The category assigned to a customer based on the type of customer account. | Customer | Head of Customer Operations | Customer Data Steward | `customers.customer_type` | Proposed |
| Customer Status | The current operational status of a customer account. | Customer | Head of Customer Operations | Customer Data Steward | `customers.status` | Proposed |
| Customer Email | The email address associated with a customer account and used for customer communication. | Customer | Head of Customer Operations | Customer Data Steward | `customers.email` | Proposed |
| Invoice | A billing record representing charges issued to a customer for energy services. | Billing | Finance Director | Billing Data Steward | `billing.invoice_id` | Proposed |
| Invoice Amount | The monetary amount in euros charged to a customer on an invoice. | Billing | Finance Director | Billing Data Steward | `billing.amount_eur` | Proposed |
| Billing Date | The date associated with the issuance of a customer invoice. | Billing | Finance Director | Billing Data Steward | `billing.billing_date` | Proposed |
| Payment Status | The current payment state associated with an invoice. | Billing | Finance Director | Billing Data Steward | `billing.payment_status` | Proposed |
| Meter | A device associated with a customer account and used to measure energy consumption. | Metering | Head of Energy Operations | Metering Data Steward | `meters.meter_id` | Proposed |
| Meter Type | The category of meter installed for a customer. | Metering | Head of Energy Operations | Metering Data Steward | `meters.meter_type` | Proposed |
| Meter Status | The current operational status of an energy meter. | Metering | Head of Energy Operations | Metering Data Steward | `meters.status` | Proposed |
| Meter Reading | A recorded energy consumption observation associated with a meter on a specific date. | Metering | Head of Energy Operations | Metering Data Steward | `meter_readings.reading_id` | Proposed |
| Energy Consumption | The quantity of energy consumed and recorded in kilowatt-hours (kWh). | Metering | Head of Energy Operations | Metering Data Steward | `meter_readings.consumption_kwh` | Proposed |
| Tariff | An energy pricing plan defining how energy consumption is charged. | Tariff | Commercial Director | Commercial Data Steward | `tariffs.tariff_id`, `customers.tariff_id` | Proposed |
| Tariff Name | The business-facing name assigned to an energy tariff. | Tariff | Commercial Director | Commercial Data Steward | `tariffs.tariff_name` | Proposed |
| Energy Type | The type of energy product to which a tariff applies. | Tariff | Commercial Director | Commercial Data Steward | `tariffs.energy_type` | Proposed |
| Unit Rate | The monetary charge applied per unit of energy consumption under a tariff. | Tariff | Commercial Director | Commercial Data Steward | `tariffs.unit_rate` | Proposed |

## Glossary Governance Process

Business terms follow the governance lifecycle below:

1. **Propose** — A new term or definition change is proposed by a Data Steward or business stakeholder.
2. **Review** — The relevant Data Steward reviews the definition, related data elements, and potential overlaps with existing terms.
3. **Approve** — The accountable Data Owner approves the business definition.
4. **Publish** — The approved term is added to the enterprise glossary and made available to data consumers.
5. **Maintain** — Data Stewards periodically review terms and update definitions when business processes or data structures change.
6. **Escalate** — Conflicting definitions or unresolved ownership issues are escalated to the Data Governance Forum.

## Term Status

Terms in this demonstration project are marked as **Proposed** because they have not been reviewed and formally approved by real organisational Data Owners.

In a production governance environment, terms would progress through the governance lifecycle from Proposed to Approved and Published.