# Researcher and journalist start here — Northern Colorado hail history

**Dataset:** *Peak Country Northern Colorado Hail History Dataset, 2016–2025*, version 1.0.0 — published October 11, 2026. **Publisher:** [Peak Country Auto Hail Repair & Paintless Dent Repair](https://peakcountryhail.com/).

## Best entry point for each use case

| Goal | Start with | Critical caution |
|---|---|---|
| Describe annual or monthly reported observations | `summaries/annual-summary.csv`, `summaries/monthly-climatology.csv` | Descriptive reports are not an area-normalized risk estimate or climate trend |
| Count historical reports in Weld or Larimer | `data/subsets/` and `summaries/county-summary.csv` | Observer coverage and reporting sources differ; don't interpret a county count difference as normalized risk |
| Map verified reporting locations | `data/northern-colorado-hail-history-2016-2025.geojson` in QGIS | Points represent reports, not property-level claims; municipal names need not match boundaries |
| Analyze large data efficiently | Parquet master file | Equivalent to the CSV/JSON/GeoJSON master, **not additional** observations |
| Explore Greeley area | `data/subsets/greeley-25-mile-hail-history.csv` | Fixed **25-mile Lincoln Park geodesic**, not the website's 50-mile historical view |
| Understand events or independent evidence | `data/event-group-membership.csv`, `METHODOLOGY.md` | Groups are conservative; radar is context only |
| Verify original acquisition and reuse | `SOURCE_PROVENANCE.md`, `sources/source-retrieval-details.json`, `RIGHTS_BY_FILE.md` | Original-source row-level reference links are **not yet distributed** |

## No-install Python example

From the repository's public-root directory after download:

```bash
python examples/read_hail_data.py
```

The script uses only Python's standard library, reads the published CSV without modifying it, prints vetted descriptive counts and performs integrity assertions. See [examples/README.md](examples/README.md).

## QGIS in under five minutes

Open QGIS → **Layer → Add Layer → Add Vector Layer**, select `data/northern-colorado-hail-history-2016-2025.geojson` and verify CRS **EPSG:4326**. Filter attributes by `county_name` or `event_date_local`; use point symbols, not inferred storm polygons. For context, use `data/subsets/greeley-25-mile-hail-history.csv` only if an explicit 25-mile subset is intended. Do not turn point locations into a vehicle-damage prediction.

## Approved reporting language

A defensible statement is: “The version 1.0.0 compilation contains **1,844 confirmed reported hail-observation lineages** in Weld and Larimer Counties during 2016–2025, with 1,064 in its specifically defined 25-mile Greeley subset.” Follow that immediately with reporting-coverage caveats. Do not say “1,844 separate storms” or “1,844 damaged properties.”

For copyable citations see [CITE_THIS_DATASET.md](CITE_THIS_DATASET.md). For rights see [RIGHTS_BY_FILE.md](RIGHTS_BY_FILE.md). For the distinction from Peak Country's existing 50-mile hail history, see [SCOPE_AND_COUNT_COMPARISON.md](SCOPE_AND_COUNT_COMPARISON.md).

Original data is educational. Peak Country's automotive damage inspections are a **separate service**; historical reports do not establish damage, coverage or the need for repair at an individual location.
