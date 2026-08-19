# Data Quality Issue Management

## Purpose

This process defines how data quality issues are identified, assigned, investigated, remediated, validated, and escalated.

It separates automated data quality detection from governance decisions that require Data Steward or business review.

## Issue Lifecycle

1. **Detected** — An automated data quality rule identifies a failed record in the raw data.
2. **Logged** — The failed record is converted into a governance issue with its domain, severity, Data Owner, and Data Steward.
3. **Assigned** — The issue is assigned to the relevant Data Steward for investigation.
4. **Investigated** — The Data Steward determines the root cause, business impact, and appropriate corrective action.
5. **Approved** — The remediation action is reviewed and approved where required.
6. **Remediated** — The approved correction is applied to the curated data while the original raw data remains unchanged.
7. **Validated** — The same data quality rules are rerun against the curated data to verify the remediation.
8. **Closed** — The issue is closed when validation confirms that the required data quality threshold is met.
9. **Escalated** — Critical, cross-domain, or unresolved issues are escalated to the Data Owner or Data Governance Forum.

## Issue Ownership

| Role | Responsibility |
| --- | --- |
| Data Steward | Investigates issues, identifies root causes, and proposes remediation actions |
| Data Owner | Provides accountability and approves significant remediation or escalation decisions |
| Data Governance Forum | Resolves cross-domain, ownership, policy, or unresolved governance issues |

## Escalation Criteria

Issues should be escalated when they:

- Are classified as Critical
- Create material customer, financial, regulatory, or operational risk
- Affect multiple data domains
- Remain unresolved beyond the agreed remediation timeframe
- Require ownership or policy decisions beyond the Data Steward's authority

## Automation Boundary

The pipeline automates data quality validation, failed record identification, governance issue generation, approved remediation execution, and revalidation.

Root cause analysis, business impact assessment, remediation decisions, and approvals require Data Steward or business investigation and are not automatically inferred by the pipeline.

In a production environment, some issues would require correction in the originating source system rather than remediation within a downstream curated data layer.