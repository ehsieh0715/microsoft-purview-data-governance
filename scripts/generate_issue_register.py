from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

FAILED_RECORDS_FILE = (
    BASE_DIR / "data-quality" / "results" / "raw" / "failed-records.csv"
)

RULE_MAPPING_FILE = BASE_DIR / "config" / "rule_governance_mapping.csv"
DOMAIN_OWNERSHIP_FILE = BASE_DIR / "config" / "domain_ownership.csv"
DATA_ELEMENTS_FILE = BASE_DIR / "config" / "governed_data_elements.csv"
BUSINESS_GLOSSARY_FILE = BASE_DIR / "config" / "business_glossary.csv"

OUTPUT_FILE = (
    BASE_DIR / "data-quality" / "results" / "raw" / "data-quality-issues.csv"
)


def build_issue_register(
    failed_records,
    rule_mapping,
    domain_ownership,
    data_elements,
    business_glossary,
):
    issues = (
        failed_records
        .merge(
            rule_mapping,
            on="rule_id",
            how="left",
            validate="many_to_one",
        )
        .merge(
            domain_ownership,
            on="domain",
            how="left",
            validate="many_to_one",
        )
        .merge(
            data_elements,
            on=["dataset", "column"],
            how="left",
            validate="many_to_one",
            suffixes=("", "_element"),
        )
        .merge(
            business_glossary[["term", "definition"]],
            left_on="business_term",
            right_on="term",
            how="left",
            validate="many_to_one",
        )
    )

    domain_mismatch = (
        issues["domain_element"].notna()
        & (issues["domain"] != issues["domain_element"])
    )

    if domain_mismatch.any():
        raise ValueError(
            "Domain mismatch found between rule governance mapping "
            "and governed data elements."
        )

    issues = issues.drop(columns=["domain_element", "term"])
    issues = issues.rename(columns={"definition": "business_definition"})

    issues.insert(
        0,
        "issue_id",
        [f"ISSUE-{i:03d}" for i in range(1, len(issues) + 1)],
    )

    issues["status"] = "Open"

    return issues


def main():
    if not FAILED_RECORDS_FILE.exists():
        raise FileNotFoundError(
            "Raw failed records not found. "
            "Run data_quality_checks.py --stage raw first."
        )

    failed_records = pd.read_csv(FAILED_RECORDS_FILE)
    rule_mapping = pd.read_csv(RULE_MAPPING_FILE)
    domain_ownership = pd.read_csv(DOMAIN_OWNERSHIP_FILE)
    data_elements = pd.read_csv(DATA_ELEMENTS_FILE)
    business_glossary = pd.read_csv(BUSINESS_GLOSSARY_FILE)

    issues = build_issue_register(
        failed_records,
        rule_mapping,
        domain_ownership,
        data_elements,
        business_glossary,
    )

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    issues.to_csv(OUTPUT_FILE, index=False)

    print("\nDATA QUALITY ISSUE REGISTER")
    print(issues.to_string(index=False))
    print(f"\nIssue register written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()