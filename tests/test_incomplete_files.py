import nemreader as nr
import pytest


def test_correct_NMIs():
    meter_data = nr.read_nem_file(
        "examples/invalid/Example_NEM12_powercor.csv", ignore_missing_header=True
    )
    assert len(meter_data.readings) == 1
    assert "VABD000163" in meter_data.readings


def test_incomplete_interval_row():
    meter_data = nr.read_nem_file(
        "examples/invalid/Example_NEM12_incomplete_interval.csv"
    )
    assert len(meter_data.readings) == 1
    assert "VABD000163" in meter_data.readings


def test_correct_channels():
    meter_data = nr.read_nem_file(
        "examples/invalid/Example_NEM12_powercor.csv", ignore_missing_header=True
    )
    readings = meter_data.readings["VABD000163"]
    assert len(readings) == 2
    assert "E1" in readings
    assert "Q1" in readings


def test_correct_records():
    meter_data = nr.read_nem_file(
        "examples/invalid/Example_NEM12_powercor.csv", ignore_missing_header=True
    )
    readings = meter_data.readings["VABD000163"]

    assert len(readings["E1"]) == 96
    assert readings["E1"][10].read_value == pytest.approx(1.11, 0.1)
    assert readings["E1"][-1].read_value == pytest.approx(3.33, 0.1)

    assert len(readings["Q1"]) == 96
    assert readings["Q1"][10].read_value == pytest.approx(2.22, 0.1)
    assert readings["Q1"][-1].read_value == pytest.approx(4.44, 0.1)
    assert readings["Q1"][-1].quality_method == "A"


def test_zipped_load():
    nr.read_nem_file(
        "examples/invalid/Example_NEM12_powercor.csv.zip", ignore_missing_header=True
    )


def test_missing_fields():
    nr.read_nem_file(
        "examples/invalid/Example_NEM12_powercor.csv", ignore_missing_header=True
    )
