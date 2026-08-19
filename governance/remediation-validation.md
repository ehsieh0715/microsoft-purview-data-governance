# Data Quality Remediation and Validation

## Purpose

This document demonstrates how identified data quality issues are
remediated and revalidated while preserving the original raw data.

Approved remediation actions are applied to create a curated data layer,
and the same data quality rules are then rerun to verify the outcome.

## Raw Data Issues

The initial data quality run against `data/raw/` identified three failed
records:

  ----------------------------------------------------------------------------
  Rule           Dataset          Severity       Affected       Problem
                                                 Record         
  -------------- ---------------- -------------- -------------- --------------
  DQ-CUS-003     customers        High           C002           Invalid
                                                                customer email
                                                                format

  DQ-MTR-003     meters           Critical       M004           Meter
                                                                references an
                                                                unknown
                                                                customer

  DQ-MET-005     meter_readings   High           R002           Negative
                                                                energy
                                                                consumption
                                                                value
  ----------------------------------------------------------------------------

These invalid records remain in the raw datasets to preserve the
original source state.

## Remediation Actions

Approved corrections are defined separately in:

`remediation/remediation_actions.csv`

  -----------------------------------------------------------------------
  Rule              Dataset           Record            Remediation
  ----------------- ----------------- ----------------- -----------------
  DQ-CUS-003        customers         C002              Correct invalid
                                                        email address

  DQ-MTR-003        meters            M004              Reconcile the
                                                        meter with a
                                                        valid customer

  DQ-MET-005        meter_readings    R002              Correct the
                                                        invalid negative
                                                        consumption value
  -----------------------------------------------------------------------

The remediation process creates `data/curated/` from the raw datasets
and applies the approved corrections to the curated copies.

The raw datasets are not modified.

## Validation

The same configured data quality rules are executed against both data
stages:

``` bash
python scripts/data_quality_checks.py --stage raw
python scripts/data_quality_checks.py --stage curated
```

The validation results demonstrate the effect of remediation:

  Metric                         Raw   Curated
  ------------------------ --------- ---------
  Rules Passed               24 / 27   27 / 27
  Overall Rule Pass Rate       88.9%      100%
  Failed Records                   3         0
  Critical Issues                  1         0
  High Issues                      2         0

All 27 configured data quality rules meet their defined thresholds after
the approved remediation actions are applied.

## Demonstrated Workflow

``` text
Raw Data
    ↓
Data Quality Validation
    ↓
Failed Records
    ↓
Governance Issue Generation
    ↓
Approved Remediation Actions
    ↓
Curated Data
    ↓
Data Quality Revalidation
```

This workflow preserves the original raw data while providing a
reproducible record of the corrections applied and their validation
outcome.

In a production environment, remediation may require correction in the
authoritative source system, followed by propagation through downstream
data pipelines.