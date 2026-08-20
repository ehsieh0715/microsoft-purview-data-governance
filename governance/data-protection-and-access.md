# Data Protection and Access Framework

## Purpose

This framework defines how governed data should be classified, protected, accessed, and reviewed according to its sensitivity, business purpose, and potential privacy or organisational impact.

It establishes common principles for:

- Data classification and sensitivity
- Data protection
- Access control
- Privacy-aware data use
- Cross-data relationships and aggregation risk
- Review and escalation

Individual data element classifications are maintained as structured governance metadata in [`governed_data_elements.csv`](../config/governed_data_elements.csv).

Domain ownership and stewardship are maintained in [`domain_ownership.csv`](../config/domain_ownership.csv).

Data protection and access decisions operate within the accountability, decision, and escalation model defined in the [Governance Framework](governance-framework.md).


## Classification and Sensitivity

Data should be classified according to the level of protection required based on business sensitivity, privacy implications, regulatory requirements, and potential impact of unauthorised use or disclosure.

| Level | Definition | Handling Expectation |
| --- | --- | --- |
| **Public** | Information approved for public disclosure. | May be shared externally when appropriately approved |
| **Internal** | Business information intended for internal organisational use. | Available to authorised users with a legitimate business need |
| **Confidential** | Sensitive business or personal information where inappropriate access or disclosure could cause material impact. | Restricted to authorised roles and approved business purposes |
| **Restricted** | Highly sensitive information requiring enhanced protection. | Strict need-to-know access with enhanced approval and controls |

Classification should reflect both the nature of the data and the context in which it is used.

Data that has limited sensitivity in isolation may require stronger protection when combined with other information.


## Protection Principles

Governed data should be managed according to the following principles.

| Principle | Expectation |
| --- | --- |
| **Least Privilege** | Access should be limited to the minimum required for an approved role or business purpose. |
| **Purpose Limitation** | Data should be used only for defined and legitimate purposes. |
| **Data Minimisation** | Processing should be limited to data necessary for the intended purpose. |
| **Sensitivity-Based Protection** | Controls should be proportionate to classification, business impact, and privacy risk. |
| **Accountability** | Material access and protection decisions should have clear governance ownership. |
| **Reviewability** | Access and protection requirements should be periodically reviewed as business needs and risks change. |
| **Traceability** | Material access decisions, exceptions, and governance actions should retain appropriate evidence. |


## Access Governance

Access should be granted according to business need, data sensitivity, and governance accountability.

The access lifecycle follows a controlled process.

| Stage | Purpose |
| --- | --- |
| **1. Request** | Document the required access and legitimate business purpose. |
| **2. Review** | Assess the requested data, classification, intended use, and associated risk. |
| **3. Approve** | Obtain approval from the appropriate governance role where required. |
| **4. Provision** | Implement the approved access through the relevant platform or technical control. |
| **5. Record** | Retain appropriate evidence of the access decision. |
| **6. Review** | Periodically confirm that access remains appropriate and necessary. |
| **7. Revoke** | Remove access when the approved business need no longer exists. |

Higher-sensitivity access should require stronger justification, approval, and technical controls.


## Data Relationships and Aggregation Risk

Protection requirements should consider relationships between data in addition to the classification of individual elements.

Information that does not identify an individual or expose sensitive business information in isolation may become sensitive when combined with other identifiers, attributes, or contextual data.

Access and protection decisions should therefore consider:

- Relationships between governed data assets
- Ability to link records across domains or systems
- Combined sensitivity of multiple data elements
- Potential identification or re-identification
- Downstream use and sharing
- Business, privacy, regulatory, and security impact

Where combined access materially increases sensitivity or risk, the stronger applicable protection requirement should be considered.


## Privacy Considerations

Where governed data contains or can be linked to personal data, processing should follow applicable organisational privacy requirements and relevant legal or regulatory obligations.

| Consideration | Expectation |
| --- | --- |
| **Data Minimisation** | Only data necessary for the approved purpose should be processed or exposed. Direct identifiers and other sensitive attributes should be excluded from downstream use where they are unnecessary. |
| **Purpose Limitation** | Personal and customer-linked data should only be processed for defined and legitimate purposes consistent with applicable organisational requirements. |
| **Accuracy** | Personal data should be sufficiently accurate and up to date for its intended use. Identified quality issues should follow the investigation, remediation, and revalidation process defined in [Data Quality Issue Management](issue-management.md). |
| **Retention** | Retention requirements should reflect business, legal, privacy, regulatory, and audit needs. Different categories of data and governance evidence may require different retention periods. |
| **Privacy and Security Incidents** | Suspected inappropriate access, disclosure, loss, or misuse of protected data should be escalated through the appropriate privacy and security incident management process. |


## Classification and Access Review

Classification and access requirements should be reviewed when:

- Business use or processing purpose changes
- Data sensitivity or classification changes
- New relationships increase aggregation or identification risk
- Regulatory, privacy, or security requirements change
- Access is no longer required
- Material governance issues identify weaknesses in existing controls

Data Stewards support metadata and classification review, while material decisions and escalations follow the accountability model defined in the Governance Framework.


## Exceptions and Escalation

Access or protection decisions should be escalated where they:

- Involve highly sensitive or Restricted data
- Create material privacy, security, financial, regulatory, or business risk
- Require access beyond established business need
- Span multiple governance domains with increased combined sensitivity
- Require an exception to established policy or control
- Cannot be resolved within the authority of the responsible governance role

Privacy, security, legal, or regulatory matters should involve the appropriate specialist function.

Exceptions should be documented, appropriately approved, time-bound where practical, and subject to review.


## Production Considerations

This repository demonstrates classification, protection, and access governance using synthetic data and illustrative governance metadata.

In a production environment:

- Classifications and sensitivity requirements should be validated by appropriate business, privacy, security, legal, and regulatory stakeholders.
- Access should be enforced through appropriate identity, platform, and data-access controls.
- Classification may combine automated discovery with business validation and custom domain-specific metadata.
- Access decisions, reviews, exceptions, and material changes should remain traceable.
- Privacy, retention, and protection requirements should be integrated with applicable organisational policies and regulatory obligations.