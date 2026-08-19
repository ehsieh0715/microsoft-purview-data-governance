from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

FAILED_RECORDS_FILE = (
    BASE_DIR
    / "data-quality"
    / "results"
    / "raw"
    / "failed-records.csv"
)

GOVERNANCE_MAPPING_FILE = (
    BASE_DIR
    / "config"
    / "governance_mapping.csv"
)

OUTPUT_FILE = (
    BASE_DIR
    / "data-quality"
    / "results"
    / "raw"
    / "data-quality-issues.csv"
)


def build_issue_register(failed_records, governance_mapping):
    issues = failed_records.merge(
        governance_mapping,
        on="rule_id",
        how="left",
        validate="many_to_one",
    )

    issues.insert(
        0,
        "issue_id",
        [
            f"ISSUE-{i:03d}"
            for i in range(1, len(issues) + 1)
        ],
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

    governance_mapping = pd.read_csv(
        GOVERNANCE_MAPPING_FILE,
        keep_default_na=False,
    )

    issues = build_issue_register(
        failed_records,
        governance_mapping,
    )

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    issues.to_csv(
        OUTPUT_FILE,
        index=False,
    )

    print("\nDATA QUALITY ISSUE REGISTER")
    print(issues.to_string(index=False))
    print(f"\nIssue register written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()