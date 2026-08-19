# Data Classification and Sensitivity Framework

## Purpose

This framework defines how data within the energy data environment is classified based on its sensitivity and potential business or privacy impact.

It establishes consistent classification criteria across the Customer, Billing, Metering, and Tariff domains and provides a framework for implementing classification and sensitivity controls in Microsoft Purview.

## Sensitivity Levels

| Level | Definition | Example | Handling Expectation |
| --- | --- | --- | --- |
| Public | Information approved for public disclosure. | Published tariff information | May be shared externally when approved |
| Internal | Business information intended for internal organisational use. | Operational metadata and reference identifiers | Accessible to authorised employees |
| Confidential | Sensitive business or personal information where unauthorised disclosure could cause privacy, financial, or business impact. | Customer contact details and billing information | Restricted to authorised roles and business purposes |
| Restricted | Highly sensitive information requiring the strongest access controls. | Authentication credentials or highly sensitive regulated data | Strict need-to-know access and enhanced controls |

## Classification Approach

Two related concepts are used in this framework:

- **Data classification** identifies the type or nature of information contained in a data element, such as an email address, telephone number, personal name, or financial information.
- **Sensitivity level** represents the level of protection required based on business, privacy, and regulatory considerations.

Technical classifications may be detected automatically by governance tooling such as Microsoft Purview, while sensitivity requirements are determined according to organisational governance policies and business context.

## Customer Domain

| Data Element | Data Classification | Personal Data | Sensitivity | Rationale |
| --- | --- | ---: | --- | --- |
| `customer_id` | Customer Identifier | Yes | Confidential | Persistent identifier linked to an individual customer record |
| `first_name` | Person Name | Yes | Confidential | Directly identifies or contributes to identifying an individual |
| `last_name` | Person Name | Yes | Confidential | Directly identifies or contributes to identifying an individual |
| `email` | Email Address | Yes | Confidential | Customer contact information and personal data |
| `phone` | Phone Number | Yes | Confidential | Customer contact information and personal data |
| `address` | Postal Address | Yes | Confidential | Customer location and contact information |
| `customer_type` | Customer Attribute | Yes | Internal | Business attribute associated with a customer record |
| `tariff_id` | Tariff Assignment | Yes | Internal | Identifies the tariff assigned to a customer account |
| `status` | Customer Attribute | Yes | Internal | Operational account status associated with a customer |

## Billing Domain

| Data Element | Data Classification | Personal Data | Sensitivity | Rationale |
| --- | --- | ---: | --- | --- |
| `invoice_id` | Invoice Identifier | Potentially | Internal | Operational identifier that can be linked to a customer invoice |
| `customer_id` | Customer Identifier | Yes | Confidential | Links billing information to an identifiable customer |
| `billing_date` | Billing Information | Yes | Confidential | Forms part of an identifiable customer's billing history |
| `amount_eur` | Financial Information | Yes | Confidential | Reveals financial information associated with a customer account |
| `payment_status` | Financial Information | Yes | Confidential | Reveals payment information associated with a customer |

## Metering Domain

### Meter Data

| Data Element | Data Classification | Personal Data | Sensitivity | Rationale |
| --- | --- | ---: | --- | --- |
| `meter_id` | Meter Identifier | Potentially | Internal | Identifies a meter that can be linked to a customer account |
| `customer_id` | Customer Identifier | Yes | Confidential | Directly links the meter to a customer record |
| `meter_type` | Meter Attribute | Potentially | Internal | Operational attribute associated with a customer-linked meter |
| `installation_date` | Meter Metadata | Potentially | Internal | Installation information that can be associated with a customer-linked meter |
| `status` | Meter Attribute | Potentially | Internal | Operational status associated with a customer-linked meter |

### Meter Reading Data

| Data Element | Data Classification | Personal Data | Sensitivity | Rationale |
| --- | --- | ---: | --- | --- |
| `reading_id` | Meter Reading Identifier | Potentially | Internal | Identifies a reading that can be linked to a meter and customer |
| `meter_id` | Meter Identifier | Potentially | Internal | Links the reading to a meter that can be associated with a customer |
| `reading_date` | Consumption Metadata | Potentially | Internal | Becomes customer-related information when linked through a meter |
| `consumption_kwh` | Energy Consumption Data | Potentially | Confidential | Consumption patterns linked to a customer may reveal behavioural information |

A value marked as **Potentially** personal data may not identify an individual in isolation but can become personal data when linked with other identifiers or contextual information.

For example, `meter_readings.csv` does not contain `customer_id`, but its records can be associated with customers through the relationship between `meter_readings.meter_id` and `meters.customer_id`.

## Tariff Domain

| Data Element | Data Classification | Personal Data | Sensitivity | Rationale |
| --- | --- | ---: | --- | --- |
| `tariff_id` | Tariff Identifier | No | Internal | Reference identifier for a tariff |
| `tariff_name` | Tariff Information | No | Internal | Business-facing tariff information |
| `energy_type` | Product Information | No | Internal | Describes the energy product associated with the tariff |
| `unit_rate` | Pricing Information | No | Internal | Commercial pricing information used by the tariff |

Tariff reference data does not directly contain personal data. A customer's tariff assignment becomes customer-related information when `customers.tariff_id` is associated with a customer record.

## Microsoft Purview Implementation Mapping

In a Microsoft Purview environment, this framework could be implemented using data scanning, classifications, catalogue metadata, and applicable sensitivity capabilities.

Examples include:

| Data Element | Expected Purview Classification / Governance Treatment |
| --- | --- |
| `customers.first_name` | Person Name classification |
| `customers.last_name` | Person Name classification |
| `customers.email` | Email Address classification |
| `customers.phone` | Phone Number classification |
| `customers.address` | Address or personal data classification |
| `customers.customer_id` | Custom customer identifier classification |
| `billing.amount_eur` | Financial information classification or custom classification |
| `meters.meter_id` | Custom meter identifier classification |
| `meter_readings.consumption_kwh` | Custom energy consumption classification |

Built-in classifications should be evaluated against organisational requirements, with custom classifications introduced where domain-specific concepts are not adequately represented.

The classifications in this repository represent the intended governance design. Automated classification results were not generated because full Microsoft Purview scanning was unavailable in the project environment.

## Classification Governance Process

1. Data assets are discovered and technical metadata is captured.
2. Automated classifications are reviewed where available.
3. Data Stewards validate classifications against business context.
4. Sensitivity levels are assigned according to organisational policy.
5. Data Owners approve material classification decisions where required.
6. Classification conflicts or high-risk cases are escalated through the governance process.
7. Classifications are periodically reviewed as datasets, regulations, and business uses change.