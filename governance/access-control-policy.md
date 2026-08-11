# Data Access Control Policy

## Purpose

This policy defines how access to governed data is requested, approved, reviewed, and revoked across the Customer, Billing, Metering, and Tariff domains.

The objective is to ensure that access is granted according to business need, data sensitivity, and organisational responsibilities.

## Access Principles

- Access should follow the principle of least privilege.
- Users should only receive access required for their role and approved business purpose.
- Confidential data should be restricted to authorised users.
- Access to personal data should be limited to legitimate business purposes.
- Access permissions should be periodically reviewed.
- Access should be removed when no longer required.

## Access Levels

| Sensitivity | Example | Access Expectation |
|---|---|---|
| Public | Approved public tariff information | May be shared externally when approved |
| Internal | Operational identifiers and internal metadata | Available to authorised employees |
| Confidential | Customer contact, billing, and linked consumption data | Restricted to approved roles with a valid business purpose |
| Restricted | Highly sensitive regulated or security-related data | Strict need-to-know access with enhanced approval |

## Domain Access Model

| Domain | Example Data | Primary Access Roles |
|---|---|---|
| Customer | Customer identity and contact data | Customer Operations, authorised Analytics users |
| Billing | Invoice and payment information | Finance, authorised Analytics users |
| Metering | Meter readings and consumption data | Energy Operations, authorised Analytics users |
| Tariff | Pricing and tariff information | Commercial, authorised Analytics users |

## Access Request Process

1. User submits an access request with a documented business purpose.
2. The Data Steward validates the requested dataset and sensitivity level.
3. The Data Owner approves or rejects access where required.
4. IT or the relevant platform administrator implements the approved access.
5. Access is recorded for audit and governance purposes.
6. Access is reviewed periodically and revoked when no longer required.

## Escalation

Access requests should be escalated when:

- The request involves Restricted data.
- The business purpose is unclear or disputed.
- The request requires cross-domain access to multiple Confidential datasets.
- The request raises privacy, regulatory, or security concerns.
- Data Owner approval cannot be obtained.

Privacy or regulatory concerns should be referred to the appropriate Data Protection, Legal, or Security function.