def read_csv(path):
    with open(path) as f:
        lines = f.readlines()

    headers = lines[0].strip().split(",")
    data = []

    for line in lines[1:]:
        values = line.strip().split(",")
        row = dict(zip(headers, values))

        rate_keys = ["hourly_rate", "rate", "salary"]
        for key in rate_keys:
            if key in row:
                row["rate"] = float(row[key])
                break

        if "hours_worked" in row:
            row["hours_worked"] = float(row["hours_worked"])

        if "hourly_rate" in row:
            del row["hourly_rate"]
        data.append(row)
    return data
