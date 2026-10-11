# Dataset distributions and release verification

**Status:** Version 1.0.0 published October 11, 2026. Repository: https://github.com/brandonmorrow365-netizen/peak-country-northern-colorado-hail-data. No DOI has been assigned.

| Distribution | Canonical file in the public repository root | Format |
|---|---|---|
| Master observations | `data/northern-colorado-hail-history-2016-2025.csv` | CSV |
| Equivalent master | `data/northern-colorado-hail-history-2016-2025.json` | JSON |
| Equivalent master (spatial) | `data/northern-colorado-hail-history-2016-2025.geojson` | GeoJSON |
| Equivalent master (columnar) | `data/northern-colorado-hail-history-2016-2025.parquet` | Parquet |
| Weld and Larimer subsets | `data/subsets/` | CSV |
| Greeley neutral 25-mile subset | `data/subsets/greeley-25-mile-hail-history.csv` | CSV |
| Event memberships, tables and figures | `data/event-group-membership.csv`, `summaries/`, `figures/` | CSV, SVG, PNG |

Four master formats represent the **same** 1,844 observations; never sum across them. All reported values require [methodology](METHODOLOGY.md) and [source-rights](RIGHTS_BY_FILE.md) context.

## Versioned public downloads

The versioned raw downloads listed below use the immutable `v1.0.0` tag. The Schema.org and DCAT descriptors provide explicit links for each of the four equivalent master formats. `SHA256SUMS.txt` and `CHECKSUMS.sha256` verify the released repository files.

- [Master CSV](https://raw.githubusercontent.com/brandonmorrow365-netizen/peak-country-northern-colorado-hail-data/v1.0.0/data/northern-colorado-hail-history-2016-2025.csv)
- [Master JSON](https://raw.githubusercontent.com/brandonmorrow365-netizen/peak-country-northern-colorado-hail-data/v1.0.0/data/northern-colorado-hail-history-2016-2025.json)
- [Master GeoJSON](https://raw.githubusercontent.com/brandonmorrow365-netizen/peak-country-northern-colorado-hail-data/v1.0.0/data/northern-colorado-hail-history-2016-2025.geojson)
- [Master Parquet](https://raw.githubusercontent.com/brandonmorrow365-netizen/peak-country-northern-colorado-hail-data/v1.0.0/data/northern-colorado-hail-history-2016-2025.parquet)
- [Weld County subset](https://raw.githubusercontent.com/brandonmorrow365-netizen/peak-country-northern-colorado-hail-data/v1.0.0/data/subsets/weld-county-hail-history.csv)
- [Larimer County subset](https://raw.githubusercontent.com/brandonmorrow365-netizen/peak-country-northern-colorado-hail-data/v1.0.0/data/subsets/larimer-county-hail-history.csv)
- [Greeley 25-mile subset](https://raw.githubusercontent.com/brandonmorrow365-netizen/peak-country-northern-colorado-hail-data/v1.0.0/data/subsets/greeley-25-mile-hail-history.csv)

The separately governed website route `https://peakcountryhail.com/northern-colorado-hail-history/` is not represented as the canonical dataset landing page in this release. No DOI or archive registration is asserted.

No schema.org `citation` self-citation is used: the dataset's own credit belongs in `name`, `identifier`, `creator` and `publisher`, while the visible formatted citation belongs in `CITE_THIS_DATASET.md`.
