import sys
import pytest
from wage_report.main import main


@pytest.fixture
def sample_csv_files(tmp_path):
    file1 = tmp_path / "data1.csv"
    file1.write_text(
        "id,email,name,department,hours_worked,hourly_rate\n"
        "1,alice@example.com,Alice Johnson,Marketing,160,50\n"
    )

    file2 = tmp_path / "data2.csv"
    file2.write_text(
        "id,email,name,department,hours_worked,rate\n"
        "2,bob@example.com,Bob Smith,Design,150,40\n"
    )

    return [file1, file2]


def test_payout_report(sample_csv_files, capsys, monkeypatch):
    test_args = ["main.py", *map(str, sample_csv_files), "--report", "payout"]
    monkeypatch.setattr(sys, "argv", test_args)

    main()

    captured = capsys.readouterr()
    assert "Alice Johnson" in captured.out
    assert "Bob Smith" in captured.out
    assert "Report generated." in captured.out


def test_avg_rate_report(sample_csv_files, capsys, monkeypatch):
    test_args = ["main.py", *map(str, sample_csv_files), "--report", "avg_rate"]
    monkeypatch.setattr(sys, "argv", test_args)

    main()

    captured = capsys.readouterr()
    assert "Coming soon" in captured.out


def test_invalid_report_type(sample_csv_files, capsys, monkeypatch):
    test_args = ["main.py", *map(str, sample_csv_files), "--report", "something"]
    monkeypatch.setattr(sys, "argv", test_args)

    main()

    captured = capsys.readouterr()
    assert "Invalid report type." in captured.out
