# Practical research examples (read-only)

From the **prospective public dataset repository root**, execute:

```bash
python examples/read_hail_data.py
```

Requires Python 3.9+; standard library only, no credentials, network calls, scraping, writes or external dependencies. It validates 1,844 unique observation IDs and the published Weld/Larimer/25-mile subset counts, then prints descriptive observations by year.

**QGIS:** Load `data/northern-colorado-hail-history-2016-2025.geojson` as a vector layer. The geometry uses WGS84 lon/lat. Avoid creating implied continuous storm footprints from reported points without an independent, validated meteorological model.

These examples are educational and not an insurer-level hail-loss estimate. See `RESEARCHER_START_HERE.md`, `LIMITATIONS.md`, and `RIGHTS_BY_FILE.md`.
