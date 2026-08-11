# Data Quality Issue Management

## Purpose

This process defines how data quality issues are identified, assigned, investigated, remediated, validated, and escalated.

## Issue Lifecycle

1. **Detected** — An automated data quality rule fails.
2. **Logged** — The failed record is captured in the issue register.
3. **Assigned** — The issue is assigned to the relevant Data Steward.
4. **Investigated** — The Data Steward determines the root cause and business impact.
5. **Remediated** — Corrective action is applied to the data or upstream process.
6. **Validated** — Data quality rules are rerun to verify the remediation.
7. **Closed** — The issue is closed once the required threshold is met.
8. **Escalated** — Critical or unresolved issues are escalated to the Data Owner or Data Governance Forum.

## Escalation Criteria

Issues should be escalated when they:

- Are classified as Critical
- Create material customer, financial, regulatory, or operational risk
- Affect multiple data domains
- Remain unresolved beyond the agreed remediation timeframe
- Require ownership or policy decisions beyond the Data Steward's authority

## Automation Boundary

Automated checks identify failed rules and affected records.

Root cause analysis and remediation decisions require Data Steward or business investigation and are therefore not automatically inferred by the pipeline.