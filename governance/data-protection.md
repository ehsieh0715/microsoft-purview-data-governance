# Data Protection and Privacy Governance

## Purpose

This document defines privacy-oriented governance considerations for personal data contained within the demonstration energy datasets.

The framework is designed to support GDPR-aligned data governance practices within an Irish and EU organisational context.

## Personal Data in Scope

| Domain | Data Elements |
|---|---|
| Customer | customer_id, first_name, last_name, email, phone, address, customer_type, status |
| Billing | customer_id, billing_date, amount_eur, payment_status |
| Metering | customer_id and customer-linked meter and consumption information |
| Tariff | No direct personal data in the demonstration dataset |

## Governance Principles

Personal data should be:

- Used only for defined and legitimate business purposes.
- Accessible only to authorised users.
- Limited to the data necessary for the relevant purpose.
- Retained according to approved organisational retention requirements.
- Protected according to its sensitivity.
- Reviewed when data usage or processing purposes change.

## Privacy Considerations

### Data Minimisation

Only data required for the relevant operational, reporting, or analytical purpose should be processed.

### Purpose Limitation

Customer data should only be used for approved business purposes compatible with the reason for which it was collected.

### Access Control

Access to personal data should follow the access control process defined in the governance framework.

### Retention

Retention periods should be defined by the appropriate business, legal, and regulatory stakeholders.

### Data Quality

Personal data should be kept sufficiently accurate and up to date for its intended use.

### Incident Escalation

Suspected inappropriate access, disclosure, or misuse of personal data should be escalated through the organisation's privacy and security incident management process.

## Microsoft Purview Implementation Mapping

In a Microsoft Purview Enterprise environment, privacy governance could be supported through:

- Automated and custom classifications
- Sensitivity labels
- Data catalogue metadata
- Data ownership and stewardship
- Data access governance
- Data lineage and discovery
- Data quality monitoring

The controls documented in this repository represent governance design for the demonstration environment.