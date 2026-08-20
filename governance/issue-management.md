# Data Quality Issue Management

## Purpose

This framework defines how data quality issues are identified, assessed, investigated, remediated, revalidated, and closed.

Data quality issue management connects automated control failures with governance accountability and corrective action. Automated detection and evidence generation support the process, while decisions requiring business context, root cause analysis, or approval remain subject to appropriate governance oversight.

Issue management operates within the accountability, decision, and escalation model defined in the [Governance Framework](governance-framework.md).


## Issue Lifecycle

Data quality issues follow a controlled lifecycle from detection through resolution.

| Stage | Purpose |
| --- | --- |
| **1. Detect** | Identify a data quality control failure and capture supporting evidence. |
| **2. Register** | Create a traceable governance issue with the relevant control, affected data, severity, and governance context. |
| **3. Assess** | Evaluate business impact, priority, ownership, and the need for escalation. |
| **4. Investigate** | Determine the root cause and identify an appropriate corrective action. |
| **5. Approve** | Obtain approval where remediation involves material business, data, or control changes. |
| **6. Remediate** | Apply or coordinate the approved corrective action. |
| **7. Revalidate** | Re-execute the relevant data quality controls to determine whether the required quality threshold has been restored. |
| **8. Close** | Close the issue when remediation and revalidation provide sufficient evidence of resolution. |

Issues may be escalated at any stage according to severity, business impact, ownership, risk, or the ability of the responsible governance role to resolve the issue.


## Issue Assessment and Prioritisation

Issues should be assessed using available governance and data quality context.

Relevant factors may include:

- Control severity
- Critical Data Element status
- Business impact
- Number or significance of affected records
- Data classification
- Downstream impact
- Cross-domain dependencies
- Regulatory, privacy, security, or financial implications
- Recurrence or previous remediation history

Severity provides an initial indication of priority but should not replace investigation and business judgement.

Rule-level governance context used for issue generation is maintained in [`rule_governance_mapping.csv`](../config/rule_governance_mapping.csv). Domain accountability is maintained in [`domain_ownership.csv`](../config/domain_ownership.csv), while CDE and classification metadata are maintained in [`governed_data_elements.csv`](../config/governed_data_elements.csv).


## Root Cause and Remediation

Root cause analysis should determine why the quality requirement failed and identify corrective action appropriate to the source and impact of the issue.

Remediation may involve:

- Correcting inaccurate or incomplete data
- Resolving reference or relationship failures
- Correcting upstream processes or source systems
- Updating transformation or pipeline logic
- Clarifying business definitions or permitted values
- Revising a control where the existing requirement no longer reflects an approved business rule

Where feasible, remediation should address the underlying source of the issue to reduce recurrence.

Corrections applied downstream should preserve traceability to the original data and the approved remediation decision.

Approved remediation actions demonstrated in this repository are maintained in [`remediation_actions.csv`](../remediation/remediation_actions.csv).


## Revalidation and Closure

The relevant data quality controls should be re-executed following remediation to provide evidence that the required quality threshold has been restored.

An issue may be closed when:

- The approved remediation has been completed
- Revalidation meets the required quality threshold
- Relevant evidence has been retained
- No further governance action is required

Where revalidation continues to fail, the issue should remain open for further investigation, remediation, or escalation.


## Escalation

Data quality issues should be escalated where they:

- Have material business, customer, financial, regulatory, privacy, security, or operational impact
- Affect Critical Data Elements with significant downstream consequences
- Span multiple governance domains
- Remain unresolved beyond an appropriate remediation timeframe
- Require decisions beyond the authority of the responsible governance role
- Indicate recurring or systemic control failures

Escalation routes and decision rights are defined in the [Governance Framework](governance-framework.md).


## Automation and Human Decision Boundary

Automation should support repeatable detection, evidence collection, issue creation, routing, remediation execution where appropriate, and revalidation.

| Activity | Typical Approach |
| --- | --- |
| Data quality validation | Automated |
| Failure evidence generation | Automated |
| Governance context enrichment | Automated where metadata is available |
| Issue registration and routing | Automated or workflow-driven |
| Business impact assessment | Human judgement |
| Root cause analysis | Human investigation supported by technical evidence |
| Remediation decision | Human decision or approved workflow |
| Remediation execution | Automated or manual depending on the corrective action |
| Revalidation | Automated |
| Issue closure | Governance decision supported by validation evidence |

Automation should support governance accountability without inferring business decisions that require organisational context or approval.


## Issue Monitoring

Issue monitoring should provide visibility into the effectiveness of investigation and remediation processes.

Relevant measures may include:

- Open issues by severity
- Issue ageing
- Time to remediation
- Recurring issues
- Issues affecting Critical Data Elements
- Revalidation success
- Escalated issues
- Issues by governance domain

Monitoring should support prioritisation, escalation, root cause analysis, and continuous improvement.


## Production Considerations

This repository demonstrates issue management using synthetic data and a controlled remediation and revalidation workflow.

In a production environment:

- Issues should integrate with appropriate operational workflow and case-management processes.
- Remediation should normally occur in the authoritative source system where feasible.
- Material remediation should follow appropriate approval and change-control processes.
- Issue history, decisions, evidence, and validation outcomes should remain traceable.
- Recurring issues should be analysed for systemic causes and opportunities for preventative controls.