# Data Protection and Privacy Governance

## Purpose

This document defines privacy-oriented governance considerations for personal data contained within the demonstration energy datasets.

The framework is designed to support GDPR-aligned data governance practices within an Irish and EU organisational context.

## Personal Data in Scope

| Domain | Data Elements | Privacy Consideration |
| --- | --- | --- |
| Customer | `customer_id`, `first_name`, `last_name`, `email`, `phone`, `address`, `customer_type`, `status` | Contains directly identifiable and customer-related information |
| Billing | `customer_id`, `billing_date`, `amount_eur`, `payment_status` | Contains financial and account information linked to a customer |
| Metering | `meters.customer_id`, `meters.meter_id`, `meter_readings.meter_id`, `meter_readings.reading_date`, `meter_readings.consumption_kwh` | Meter and consumption records can be linked to a customer through dataset relationships |
| Tariff | `tariff_id`, `tariff_name`, `energy_type`, `unit_rate` | Contains no direct personal data in the demonstration dataset |

Although `meter_readings` does not contain a direct customer identifier, readings can be associated with customers through the relationship between `meter_readings.meter_id` and `meters.customer_id`.

## Governance Principles

Personal data should be:

- Used only for defined and legitimate business purposes.
- Accessible only to authorised users.
- Limited to the data necessary for the relevant purpose.
- Retained according to approved organisational retention requirements.
- Protected according to its sensitivity.
- Reviewed when data usage or processing purposes change.
- Maintained with appropriate accuracy and quality controls.

## Privacy Considerations

### Data Minimisation

Only data required for the relevant operational, reporting, analytical, or governance purpose should be processed.

Where direct customer identifiers are unnecessary, downstream datasets should minimise or remove identifying attributes where appropriate.

### Purpose Limitation

Customer and customer-linked data should only be used for approved business purposes compatible with the reason for which it was collected.

### Access Control

Access to personal and customer-linked data should follow the role-based access control process defined in the governance framework.

Access requirements may differ between raw and curated data depending on the sensitivity and intended use of each dataset.

### Retention

Retention periods should be defined by the appropriate business, legal, privacy, and regulatory stakeholders.

Raw data, curated data, data quality results, and remediation records may require different retention policies based on their purpose and audit requirements.

### Data Quality and Remediation

Personal data should be sufficiently accurate and up to date for its intended use.

The project's data quality workflow identifies invalid records in the raw data and applies approved remediation actions to the curated data while preserving the original raw state for demonstration and auditability.

In a production environment, corrections to personal data may need to be performed in the authoritative source system and propagated downstream according to established data management procedures.

### Incident Escalation

Suspected inappropriate access, disclosure, loss, or misuse of personal data should be escalated through the organisation's privacy and security incident management process.

## Microsoft Purview Implementation Mapping

In a Microsoft Purview environment, privacy governance could be supported through:

- Automated and custom classifications
- Sensitivity labels
- Data catalogue metadata
- Data ownership and stewardship
- Data access governance
- Data lineage and discovery
- Data quality monitoring

The controls documented in this repository represent governance design for the demonstration environment.