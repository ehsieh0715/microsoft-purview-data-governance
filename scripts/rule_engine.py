import re

import pandas as pd


def build_failed_mask(rule, datasets):
    dataset = rule["dataset"]
    column = rule["column"]
    check_type = rule["check_type"]
    parameter = rule.get("parameter", "")

    df = datasets[dataset]

    if check_type == "not_null":
        failed_mask = df[column].isna()
        eligible_mask = pd.Series(True, index=df.index)

    elif check_type == "unique":
        failed_mask = df[column].duplicated(keep=False)
        eligible_mask = pd.Series(True, index=df.index)

    elif check_type == "email_format":
        eligible_mask = df[column].notna()

        failed_mask = (
            eligible_mask
            & ~df[column]
            .astype(str)
            .str.match(
                r"^[^@\s]+@[^@\s]+\.[^@\s]+$",
                flags=re.IGNORECASE,
            )
        )

    elif check_type == "allowed_values":
        allowed_values = set(str(parameter).split("|"))

        failed_mask = ~df[column].isin(allowed_values)
        eligible_mask = pd.Series(True, index=df.index)

    elif check_type == "min_value":
        minimum = float(parameter)

        failed_mask = ~df[column].ge(minimum)
        eligible_mask = pd.Series(True, index=df.index)

    elif check_type == "min_exclusive":
        minimum = float(parameter)

        failed_mask = ~df[column].gt(minimum)
        eligible_mask = pd.Series(True, index=df.index)

    elif check_type == "foreign_key":
        reference_dataset, reference_column = str(parameter).split(".")

        valid_values = set(
            datasets[reference_dataset][reference_column].dropna()
        )

        failed_mask = ~df[column].isin(valid_values)
        eligible_mask = pd.Series(True, index=df.index)

    else:
        raise ValueError(
            f"Unsupported check type: {check_type}"
        )

    return failed_mask, eligible_mask