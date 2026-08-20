# Data Access Control Policy

## Purpose

This policy defines how access to governed data is requested, approved, reviewed, and revoked across the Customer, Billing, Metering, and Tariff domains.

The objective is to ensure that access is granted according to business need, data sensitivity, and organisational responsibilities.

## Access Principles

- Access should follow the principle of least privilege.
- Users should only receive access required for their role and approved business purpose.
- Confidential data should be restricted to authorised users.
- Access to personal and customer-linked data should be limited to legitimate business purposes.
- Access decisions should consider the sensitivity created by combining data across domains.
- Access permissions should be periodically reviewed.
- Access should be removed when no longer required.

## Access Levels

| Sensitivity | Example | Access Expectation |
| --- | --- | --- |
| Public | Approved public tariff information | May be shared externally when approved |
| Internal | Operational identifiers and internal metadata | Available to authorised employees with a business need |
| Confidential | Customer contact, billing, and customer-linked consumption data | Restricted to approved roles with a valid business purpose |
| Restricted | Highly sensitive regulated or security-related data | Strict need-to-know access with enhanced approval |

## Domain Access Model

| Domain | Example Data | Primary Access Roles |
| --- | --- | --- |
| Customer | Customer identity, contact information, account attributes, and tariff assignment | Customer Operations, authorised Analytics users |
| Billing | Customer invoices, amounts, and payment information | Finance, authorised Analytics users |
| Metering | Customer-linked meter information, meter readings, and energy consumption | Energy Operations, authorised Analytics users |
| Tariff | Energy products, pricing plans, and unit rates | Commercial, authorised Analytics users |

## Cross-Domain Access

Access decisions should consider relationships between datasets in addition to the sensitivity of individual fields.

Meter readings do not directly contain customer identity information, but they can be linked to customer records through the meter dataset:

```text
customers.customer_id
        │
        │ customer_id
        ▼
meters.customer_id
meters.meter_id
        │
        │ meter_id
        ▼
meter_readings.meter_id
```

This relationship means that access to meter_readings alone provides limited customer context, while combined access to customers, meters, and meter_readings can associate energy consumption with an identifiable customer.

Cross-domain access involving Confidential data should therefore be reviewed based on the combined business purpose, dataset relationships, and privacy impact.

## Raw and Curated Data

The project maintains both raw and curated datasets to demonstrate the data quality remediation workflow.

Access controls should apply according to the sensitivity and business purpose of the data regardless of processing stage. Moving a record from the raw layer to the curated layer does not reduce its sensitivity.

Raw data may require additional operational restrictions because it can contain known data quality issues and represents the retained source state used for validation and audit purposes.

## Access Request Process

1. **Request** — The user submits an access request with a documented business purpose and required datasets.
2. **Review** — The Data Steward validates the requested data, sensitivity, and intended use.
3. **Approve** — The Data Owner approves or rejects access where required.
4. **Provision** — IT or the relevant platform administrator implements the approved access.
5. **Record** — The access decision is recorded for audit and governance purposes.
6. **Review** — Access is periodically reviewed to confirm that the business need remains valid.
7. **Revoke** — Access is removed when the user no longer requires it.

## Escalation

Access requests should be escalated when:

- The request involves Restricted data.
- The business purpose is unclear or disputed.
- The request requires cross-domain access to multiple Confidential datasets.
- Combining datasets materially increases privacy or business sensitivity.
- The request raises privacy, regulatory, or security concerns.
- Data Owner approval cannot be obtained.

Privacy or regulatory concerns should be referred to the appropriate Data Protection, Legal, or Security function.

## Microsoft Purview Implementation Mapping

In a Microsoft Purview environment, this policy could be supported through catalogue metadata, classifications, sensitivity information, ownership metadata, and data access governance capabilities.

The access model documented in this repository represents governance design. Access provisioning and enforcement are not implemented in the demonstration environment.
