from pathlib import Path

import pandas as pd

from rule_engine import build_failed_mask


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
CONFIG_DIR = BASE_DIR / "config"
RESULTS_DIR = BASE_DIR / "data-quality" / "results"


def load_data():
    return {
        "customers": pd.read_csv(DATA_DIR / "customers.csv"),
        "billing": pd.read_csv(DATA_DIR / "billing.csv"),
        "meter_readings": pd.read_csv(
            DATA_DIR / "meter_readings.csv"
        ),
        "tariffs": pd.read_csv(DATA_DIR / "tariffs.csv"),
    }


def load_rules():
    rules = pd.read_csv(
        CONFIG_DIR / "data_quality_rules.csv",
        keep_default_na=False,
    )

    return rules.to_dict("records")


def evaluate_rule(rule, datasets):
    df = datasets[rule["dataset"]]

    failed_mask, eligible_mask = build_failed_mask(
        rule,
        datasets,
    )

    records_checked = int(eligible_mask.sum())
    failed_records = int(failed_mask.sum())

    pass_rate = (
        100.0
        if records_checked == 0
        else (
            (records_checked - failed_records)
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
        "failed_records": failed_records,
        "pass_rate": round(pass_rate, 2),
        "target": float(rule["target"]),
        "status": (
            "PASS"
            if pass_rate >= float(rule["target"])
            else "FAIL"
        ),
        "severity": rule["severity"],
    }

    failed_rows = []

    for _, row in df.loc[failed_mask].iterrows():
        failed_rows.append(
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

    return result, failed_rows


def run_data_quality_checks():
    datasets = load_data()
    rules = load_rules()

    results = []
    failed_records = []

    for rule in rules:
        result, rule_failures = evaluate_rule(
            rule,
            datasets,
        )

        results.append(result)
        failed_records.extend(rule_failures)

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

    return results_df, failed_records_df


def save_results(results_df, failed_records_df):
    RESULTS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    results_file = (
        RESULTS_DIR / "data-quality-results.csv"
    )

    failed_records_file = (
        RESULTS_DIR / "failed-records.csv"
    )

    results_df.to_csv(
        results_file,
        index=False,
    )

    failed_records_df.to_csv(
        failed_records_file,
        index=False,
    )

    return results_file, failed_records_file


if __name__ == "__main__":
    results_df, failed_records_df = (
        run_data_quality_checks()
    )

    results_file, failed_records_file = (
        save_results(
            results_df,
            failed_records_df,
        )
    )

    print("\nDATA QUALITY RESULTS")
    print(results_df.to_string(index=False))

    print("\nFAILED RECORDS")

    if failed_records_df.empty:
        print("No data quality issues detected.")
    else:
        print(failed_records_df.to_string(index=False))

    print(f"\nResults written to: {results_file}")
    print(
        f"Failed records written to: "
        f"{failed_records_file}"
    )