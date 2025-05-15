import argparse
from wage_report.utils.csv_reader import read_csv
from wage_report.reports.payout import payout
from wage_report.reports.avg_rate import avg_rate


def main():
    parser = argparse.ArgumentParser(description="WageRoll - Report generator.")
    parser.add_argument("files", nargs="+", help="Paths to CSV files")
    parser.add_argument("--report", required=True, help="Report type to generate")

    args = parser.parse_args()
    print(
        f"\nFiles to process: {args.files}, report: {args.report}."
        "\nAttempt to generate a report..."
    )

    data_from_all_files = []
    for file_path in args.files:
        data_from_all_files.extend(read_csv(file_path))

    if args.report == "payout":
        report = payout(data_from_all_files)
        for line in report:
            print(line)
        print("Report generated.")

    elif args.report == "avg_rate":
        report = avg_rate(data_from_all_files)
        # for line in report:
        #     print(line)
        print(report)
    else:
        print("Invalid report type.")


if __name__ == "__main__":
    main()
