import argparse
from pathlib import Path

import pandas as pd

from rule_engine import build_failed_mask


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
CONFIG_FILE = BASE_DIR / "config" / "data_quality_rules.csv"
RESULTS_DIR = BASE_DIR / "data-quality" / "results"

DATASETS = [
    "customers",
    "billing",
    "meters",
    "meter_readings",
    "tariffs",
]


def load_datasets(stage):
    input_dir = DATA_DIR / stage

    return {
        name: pd.read_csv(input_dir / f"{name}.csv")
        for name in DATASETS
    }


def evaluate_rule(rule, datasets):
    df = datasets[rule["dataset"]]

    failed_mask, eligible_mask = build_failed_mask(
        rule,
        datasets,
    )

    records_checked = int(eligible_mask.sum())
    failed_count = int(failed_mask.sum())

    pass_rate = (
        100.0
        if records_checked == 0
        else (
            (records_checked - failed_count)
            / records_checked
            * 100
        )
    )

    result = {
        "rule_id": rule["rule_id"],
        "dataset": rule["dataset"],
        "column": rule["column"],
        "dimension": rule["dimension"],
        "records_checked": records_checked,
        "failed_records": failed_count,
        "pass_rate": round(pass_rate, 2),
        "target": float(rule["target"]),
        "status": (
            "PASS"
            if pass_rate >= float(rule["target"])
            else "FAIL"
        ),
        "severity": rule["severity"],
    }

    failures = []

    for _, row in df.loc[failed_mask].iterrows():
        failures.append(
            {
                "rule_id": rule["rule_id"],
                "dataset": rule["dataset"],
                "severity": rule["severity"],
                "affected_record": row[
                    rule["record_id_column"]
                ],
                "column": rule["column"],
                "invalid_value": row[rule["column"]],
            }
        )

    return result, failures


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--stage",
        choices=["raw", "curated"],
        default="raw",
    )
    args = parser.parse_args()

    stage = args.stage
    output_dir = RESULTS_DIR / stage
    output_dir.mkdir(parents=True, exist_ok=True)

    datasets = load_datasets(stage)

    rules = pd.read_csv(
        CONFIG_FILE,
        keep_default_na=False,
    ).to_dict("records")

    results = []
    failed_records = []

    for rule in rules:
        result, failures = evaluate_rule(
            rule,
            datasets,
        )

        results.append(result)
        failed_records.extend(failures)

    results_df = pd.DataFrame(results)

    failed_records_df = pd.DataFrame(
        failed_records,
        columns=[
            "rule_id",
            "dataset",
            "severity",
            "affected_record",
            "column",
            "invalid_value",
        ],
    )

    results_file = output_dir / "data-quality-results.csv"
    failures_file = output_dir / "failed-records.csv"

    results_df.to_csv(results_file, index=False)
    failed_records_df.to_csv(failures_file, index=False)

    passed = int(
        (results_df["status"] == "PASS").sum()
    )
    total = len(results_df)

    print(f"\nDATA QUALITY RESULTS: {stage.upper()}")
    print(results_df.to_string(index=False))

    print("\nFAILED RECORDS")

    if failed_records_df.empty:
        print("No data quality issues detected.")
    else:
        print(failed_records_df.to_string(index=False))

    print(f"\nSUMMARY: {passed}/{total} rules passed")
    print(f"Results written to: {results_file}")
    print(f"Failed records written to: {failures_file}")


if __name__ == "__main__":
    main()