#!/usr/bin/env python3
"""Read-only, standard-library demonstration of the Peak Country v1 historical hail dataset.

Run from the repository root: python examples/read_hail_data.py
Counts represent confirmed reported observations, not independent storms or property damage.
"""
from collections import Counter
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parent.parent
MASTER = ROOT / "data" / "northern-colorado-hail-history-2016-2025.csv"
GREELEY = ROOT / "data" / "subsets" / "greeley-25-mile-hail-history.csv"

with MASTER.open(newline="", encoding="utf-8-sig") as fh:
    observations = list(csv.DictReader(fh))
assert len(observations) == 1844, "Unexpected v1.0.0 record count"
ids = [r["observation_id"] for r in observations]
assert len(ids) == len(set(ids)), "Repeated observation ID"
assert all(r["dataset_version"] == "1.0.0" for r in observations)

counties = Counter(r["county_name"] for r in observations)
assert counties == {"WELD": 773, "LARIMER": 1071}, counties

with GREELEY.open(newline="", encoding="utf-8-sig") as fh:
    subset = list(csv.DictReader(fh))
assert len(subset) == 1064, "Greeley 25-mile subset mismatch"
master_ids = set(ids)
assert all(r["observation_id"] in master_ids for r in subset)
assert all(r["greeley_25mi_status"] == "in" for r in subset)

per_year = Counter(r["year"] for r in observations)
print("Peak Country Northern Colorado Hail History Dataset v1.0.0 (2016–2025)")
print("Publisher: Peak Country Auto Hail Repair & Paintless Dent Repair")
print("Confirmed reporting lineages:", len(observations))
print("Weld:", counties["WELD"], "Larimer:", counties["LARIMER"])
print("Greeley neutral reference, 25mi overlap:", len(subset))
print("Reports by year (not a storm-frequency trend):")
for year in sorted(per_year):
    print(" ", year, per_year[year])
print("Reminder: observational reports are not independent storms or evidence of vehicle damage.")
