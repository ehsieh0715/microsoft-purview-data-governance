# Governance Framework

## Purpose and Scope

This framework defines the principles, accountability model, decision rights, and operating lifecycle used to govern data across the organisation.

It provides a common structure for:

- Data ownership and stewardship
- Business and technical metadata
- Critical Data Elements (CDEs)
- Data quality management
- Data protection and access
- Issue management and remediation
- Governance monitoring and escalation

The framework is designed to remain independent of individual datasets, data quality rules, and technical implementations. Operational governance metadata and controls are maintained separately as structured configuration.

This repository demonstrates the framework using synthetic data and illustrative governance requirements. Production implementation would require appropriate business, technical, privacy, security, legal, and regulatory review.


## Governance Principles

The governance model is based on five principles.

| Principle | Description |
| --- | --- |
| **Clear Accountability** | Governed data should have defined ownership and stewardship so that responsibility for governance decisions, data quality, and issue resolution is clear. |
| **Business-Aligned Governance** | Governance requirements should reflect the business meaning, use, risk, and impact of data. |
| **Risk-Based Governance** | Governance effort and controls should be proportionate to data criticality, sensitivity, and potential business impact. |
| **Metadata-Driven Governance** | Governance metadata should be maintained in structured and reusable forms wherever practical, reducing duplication and enabling consistent application of governance controls. |
| **Measurable and Traceable Governance** | Governance controls and issues should produce measurable evidence for monitoring data quality, governance coverage, remediation, and control effectiveness. |


## Governance Domains

Data governance is organised into business-aligned domains.

Each domain represents a logical area of data accountability and has defined ownership and stewardship. Domains provide the organisational boundary for governance decisions, issue routing, quality oversight, and escalation.

Where data spans multiple domains, accountability should be determined according to the authoritative source, business responsibility, and downstream impact of the data.

Domain definitions and accountability assignments are maintained as structured governance metadata in [`domain_ownership.csv`](../config/domain_ownership.csv).


## Roles and Accountability

| Role | Accountability | Key Responsibilities |
| --- | --- | --- |
| **Data Owner** | Accountable for governance outcomes within a data domain | Approves material requirements and decisions; reviews significant issues; approves material remediation; resolves or escalates issues |
| **Data Steward** | Responsible for day-to-day governance activities | Maintains definitions and metadata; reviews quality requirements; investigates issues; coordinates remediation and revalidation |
| **Data Governance Forum** | Provides cross-domain governance oversight | Reviews material issues and performance; resolves cross-domain conflicts; provides direction on significant decisions |
| **Technical & Specialist Functions** | Provide implementation and subject-matter support | Implement technical controls and provide data, platform, security, privacy, legal, and regulatory expertise |


## Critical Data Elements

Critical Data Elements are data elements whose quality, availability, protection, or misuse could materially affect business processes, financial accuracy, customer outcomes, regulatory obligations, or downstream data use.

CDE designation enables governance effort to be prioritised according to business impact.

Where appropriate, CDEs should have:

- Defined business meaning
- Clear ownership and stewardship
- Appropriate data classification
- Relevant data quality controls
- Traceability to governance issues and remediation

CDE designation should be reviewed as business processes, data usage, and risk change over time.

Individual governed data elements, including their domain, business term, CDE designation, and classification, are maintained in [`governed_data_elements.csv`](../config/governed_data_elements.csv).

Business terms and their governed definitions are maintained in [`business_glossary.csv`](../config/business_glossary.csv).


## Decision Rights and Escalation

Governance decisions should be made at the lowest appropriate level while maintaining clear accountability and escalation paths.

| Governance Matter | Primary Responsibility | Escalation |
| --- | --- | --- |
| Business definition maintenance | Data Steward | Data Owner |
| Material definition or ownership conflict | Data Owner | Data Governance Forum |
| Routine data quality issue | Data Steward | Data Owner |
| Material or Critical data quality issue | Data Owner | Data Governance Forum |
| Remediation decision | Data Steward | Data Owner where material approval is required |
| Material data access decision | Data Owner | Data Governance Forum where required |
| Privacy, security, legal, or regulatory concern | Relevant specialist function | Appropriate governance authority |
| Cross-domain governance conflict | Relevant Data Owners | Data Governance Forum |

Escalation should consider severity, business impact, duration, regulatory exposure, cross-domain impact, and the ability of the responsible governance role to resolve the issue.


## Governance Lifecycle

The governance framework follows a continuous lifecycle.

| Stage | Purpose |
| --- | --- |
| **1. Define** | Establish domains, accountability, terminology, classifications, CDEs, and governance requirements |
| **2. Control** | Translate requirements into policies, metadata, quality controls, access requirements, and protection measures |
| **3. Monitor** | Evaluate controls and collect evidence of governance and data quality performance |
| **4. Manage Issues** | Identify failures, establish governance context, assign accountability, and prioritise investigation |
| **5. Remediate** | Investigate root causes and coordinate corrective actions |
| **6. Revalidate** | Re-evaluate affected controls to confirm governance requirements have been restored |

Where possible, remediation should address the underlying source of an issue rather than only its downstream symptoms. Governance outcomes should feed back into definitions, controls, metadata, and monitoring requirements to support continuous improvement.

Escalation may occur at any stage where an issue exceeds the authority, risk tolerance, or resolution capability of the responsible governance role.


## Governance Monitoring

Governance monitoring provides evidence that governance responsibilities and controls are operating effectively.

Monitoring should consider both control performance and governance coverage.

| Perspective | Purpose | Example Measures |
| --- | --- | --- |
| **Control Performance** | Measures whether governed data and controls are meeting defined expectations. | Data quality performance; control failures by severity; open governance issues; remediation outcomes; revalidation success |
| **Governance Coverage** | Measures whether appropriate governance structures have been established. | Ownership and stewardship coverage; CDE coverage; classification coverage; data quality control coverage; business metadata coverage |

Additional operational measures may include issue ageing, remediation service levels, policy exceptions, access exceptions, and material privacy or regulatory concerns.

Governance metrics should support decision-making and prioritisation. Targets, thresholds, reporting cadence, and escalation criteria should be defined according to organisational requirements and risk appetite.