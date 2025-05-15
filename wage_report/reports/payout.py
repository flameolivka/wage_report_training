def payout(data_from_all_files):
    result = []
    for row in data_from_all_files:
        name = row["name"]
        hours_worked = float(row["hours_worked"])
        rate = float(row["rate"])

        salary = hours_worked * rate
        result.append(
            f"[{row['department']}] {name}: ${salary} ({hours_worked}h + {rate}$/h)"
        )

    return result
