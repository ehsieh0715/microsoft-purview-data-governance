from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = BASE_DIR / "data-quality" / "results"
CONFIG_DIR = BASE_DIR / "config"


def generate_issue_register():
    failed_records = pd.read_csv(
        RESULTS_DIR / "failed-records.csv"
    )

    governance_mapping = pd.read_csv(
        CONFIG_DIR / "governance_mapping.csv"
    )

    issues = failed_records.merge(
        governance_mapping,
        on="rule_id",
        how="left",
    )

    issues.insert(
        0,
        "issue_id",
        [f"DQI-{i:03d}" for i in range(1, len(issues) + 1)],
    )

    issues["status"] = "Open"
    issues["root_cause"] = ""
    issues["remediation_action"] = ""

    return issues


if __name__ == "__main__":
    issue_register = generate_issue_register()

    output_file = RESULTS_DIR / "data-quality-issues.csv"

    issue_register.to_csv(
        output_file,
        index=False,
    )

    print(issue_register.to_string(index=False))