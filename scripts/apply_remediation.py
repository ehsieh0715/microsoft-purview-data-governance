from pathlib import Path
import shutil

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"
CURATED_DIR = BASE_DIR / "data" / "curated"
REMEDIATION_FILE = BASE_DIR / "remediation" / "remediation_actions.csv"

PRIMARY_KEYS = {
    "customers": "customer_id",
    "billing": "invoice_id",
    "meters": "meter_id",
    "meter_readings": "reading_id",
    "tariffs": "tariff_id",
}


def main():
    # Start curated data as a copy of raw data
    CURATED_DIR.mkdir(parents=True, exist_ok=True)

    for file in RAW_DIR.glob("*.csv"):
        shutil.copy2(file, CURATED_DIR / file.name)

    # Load approved remediation actions
    actions = pd.read_csv(
        REMEDIATION_FILE,
        keep_default_na=False,
    )

    actions = actions[actions["status"] == "Approved"]

    # Apply each approved correction
    for _, action in actions.iterrows():
        dataset = action["dataset"]
        record_id = str(action["record_id"])
        column = action["column"]
        old_value = str(action["old_value"])
        new_value = action["new_value"]

        file_path = CURATED_DIR / f"{dataset}.csv"
        primary_key = PRIMARY_KEYS[dataset]

        df = pd.read_csv(
            file_path,
            keep_default_na=False,
        )

        mask = df[primary_key].astype(str) == record_id

        if mask.sum() != 1:
            raise ValueError(
                f"Expected one record for {dataset}.{record_id}, "
                f"found {mask.sum()}."
            )

        current_value = str(df.loc[mask, column].iloc[0])

        if current_value != old_value:
            raise ValueError(
                f"Unexpected old value for {dataset}.{record_id}.{column}: "
                f"expected '{old_value}', found '{current_value}'."
            )

        column_dtype = df[column].dtype

        if pd.api.types.is_integer_dtype(column_dtype):
            new_value = int(new_value)
        elif pd.api.types.is_float_dtype(column_dtype):
            new_value = float(new_value)
        else:
            new_value = str(new_value)

        df.loc[mask, column] = new_value
        df.to_csv(file_path, index=False)

        print(
            f"Updated {dataset}.{record_id}.{column}: "
            f"{old_value} -> {new_value}"
        )

    print(
        f"\nApplied {len(actions)} approved remediation actions."
    )
    print(f"Curated data written to: {CURATED_DIR}")


if __name__ == "__main__":
    main()