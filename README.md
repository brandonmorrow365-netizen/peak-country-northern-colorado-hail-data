# Peak Country Northern Colorado Hail History Dataset

**Version:** 1.0.0 — published October 11, 2026

**Publisher:** Peak Country Auto Hail Repair & Paintless Dent Repair. **Study period:** January 2016–December 2025. **Scope:** Weld and Larimer Counties, Colorado, with an additional 25-statute-mile Greeley geographic-reference subset. This dataset combines confirmed ground observations and provenance-linked supporting context under documented source precedence and de-duplication rules.

**Dataset prepared and maintained by:** [Peak Country Auto Hail Repair & Paintless Dent Repair](https://peakcountryhail.com/). Peak Country is the dataset publisher, not the original government or CoCoRaHS reporting source.

## Cite this dataset

> Peak Country Auto Hail Repair & Paintless Dent Repair. (2026). *Peak Country Northern Colorado Hail History Dataset, 2016–2025* (Version 1.0.0) [Data set]. GitHub. https://github.com/brandonmorrow365-netizen/peak-country-northern-colorado-hail-data/releases/tag/v1.0.0

Copyable formats: [plain text](CITATION.txt), [APA-style](CITATION_APA.txt), [BibTeX](CITATION.bib), [RIS](CITATION.ris) and [GitHub citation metadata](CITATION.cff). See [citation guidance and source-rights notes](CITE_THIS_DATASET.md). No DOI has been assigned. The publisher website is not a dataset download link.

## Start with the research guides

- **[Researcher / journalist quickstart](RESEARCHER_START_HERE.md)** — what to download, QGIS/Python examples, safe reporting language.
- **[25-mile research dataset vs 50-mile website history](SCOPE_AND_COUNT_COMPARISON.md)** — these have different periods, geographies, and source methodologies. Do **not** equate or add their counts.
- **[Source-specific reuse rights](RIGHTS_BY_FILE.md)** — NOAA facts, CoCoRaHS CC BY 3.0, applicable Peak Country rights, and reserved trademarks.
- **[Source traceability and reproducibility limits](SOURCE_TRACEABILITY_LIMITS.md)** — official archive-level provenance is available; public per-observation source-event links are **not** currently distributed.
- **[Data downloads and release activation requirements](DISTRIBUTIONS_AND_RELEASE_GATE.md)** — the four equivalent master formats, planned permanent download URLs, and mandatory post-publication checks.

**Attribution:** Dataset compilation and original presentation by [Peak Country Auto Hail Repair & Paintless Dent Repair](https://peakcountryhail.com/). Underlying weather observations retain their original source status and applicable rights. Publishing this data does not assert that any particular vehicle suffered damage.

## What the data contains

The normalized master contains **1,844 active confirmed observations** (773 Weld; 1,071 Larimer). The geographic-reference subset contains **1,064 observations** within 25 statute miles of the fixed reference. The release includes a master exported in CSV, JSON, GeoJSON, and Parquet; three geographic subsets; an event-group membership file; nine summary CSV files; five chart pairs (PNG and SVG) with unobtrusive creator credit and metadata; source and figure manifests; and machine-readable metadata. Figures are descriptive and do not test climate trends.

**Do not treat observations as unique storms.** A ground observation is not equivalent to an event-group membership or a distinct hail day. Reports may be incomplete and vary across place, time and reporting system. This work does not establish property-level hail occurrence, damage, hail risk, or a climate trend.

## Directory guide

- `data/northern-colorado-hail-history-2016-2025.{csv,json,geojson,parquet}`: the same approved observation dataset in four formats; one format does not add extra records.
- `data/subsets/`: Weld, Larimer, and Greeley 25-mile subsets; subsets overlap and should not be summed indiscriminately.
- `data/event-group-membership.csv`: observation-to-event group membership (not an additional observation dataset).
- `summaries/`: annual, monthly, county, geographic distance, hail size, hail day, community, event-group, and corroboration summaries. See `summaries/README.md` for MRMS archive limitations.
- `figures/`: five paired descriptive figures, captions and alt text; see `figures/FIGURE_CAPTIONS.md` and `figures/figure-manifest.json`.
- `metadata/`: documentation of version, subset methods, summary meanings, field notes and public-field mapping.
- `sources/source-manifest.json` and `ATTRIBUTION.md`: original source provenance, license notices and attribution boundaries.
- `LICENSE`, `LICENSE-DATA`, `LICENSE-CONTENT`, `RIGHTS_BY_FILE.md`, `RIGHTS.md`: the mixed-rights framework; no single blanket license covers all underlying data.

## Research documentation and reuse

- [Methodology](METHODOLOGY.md) — source precedence, observation identity, event grouping, Greeley radius and MRMS archive.
- [Public data dictionary](DATA_DICTIONARY.md) — the approved 34 exported fields without internal-only schema elements.
- [Source provenance](SOURCE_PROVENANCE.md) and [verified acquisition appendix](sources/source-retrieval-details.json) — validated historical source URLs, versions, acquisition dates, and checksums.
- [Limitations](LIMITATIONS.md) — reporting incompleteness, interpretation and lack of property-level risk inference.
- [Corrections](CORRECTIONS.md), [contributing](CONTRIBUTING.md), and [changelog](CHANGELOG.md) — maintenance and governance.
- [Rights](RIGHTS.md), [source attribution](ATTRIBUTION.md), and [reserved trademarks](TRADEMARKS.md) — rights are source- and expression-specific.
- [Dataset metadata](metadata.json), [Schema.org Dataset](schemaorg.jsonld), [DCAT JSON-LD](dcat.json), and [Data Package](datapackage.json) — machine-readable release descriptors.
- [Figure reuse](figures/FIGURE_REUSE.md) — publisher credits and underlying observation-source limitations.

**Citing this dataset:** Finalized version 1.0.0 formats are available in `CITATION.cff`, `CITATION.txt`, `CITATION_APA.txt`, `CITATION.bib`, and `CITATION.ris`; review the source-aware instructions in `CITE_THIS_DATASET.md`. The public repository is https://github.com/brandonmorrow365-netizen/peak-country-northern-colorado-hail-data. No DOI has been assigned.

## Geographic method

The Greeley subset is calculated using WGS84 geodesic distance to the **fixed Peak Country-selected methodology reference** at Lincoln Park, Greeley, Colorado: latitude 40.424896787198563, longitude -104.69350052421541. This is **not** a shop/customer address, claim of business presence, City GIS dataset, hail report, or municipal-membership test. The defined 25-mile radius is methodological; no City of Greeley GIS material is used.

## Source roles and radar limitations

**NOAA/NCEI Storm Events** is the authoritative historical backbone. **NWS LSR** is preliminary/reference. **SPC reports** are preliminary derivatives and are not independent corroboration of matching NWS reports. **CoCoRaHS** provides supplemental ground reports under independently applicable **CC BY 3.0** rights, with attribution and changes notices. **NOAA MRMS/MESH** is radar-derived context only, not a ground hail observation. **Census TIGER/Line** supports county and geographic QA. Raw **mPING** is **NOT_USED** and excluded.

**MRMS archive coverage is not uniform over 2016–2025.** The project had no MRMS coverage for 2016–2019; 2020 is partial from **2020-10-14**; 2021–2025 have archived coverage, but this does not establish complete sampling. Precoverage blanks are **unavailable**, not zero. Radar-positive counts are contextual, not ground confirmation; always read `summaries/README.md` alongside radar-positive columns/tables.

## Rights and attribution

**ODC-By 1.0** applies only to protectable Peak Country-owned compilation/database rights, if and where they exist. **CC BY 4.0** applies only to protectable Peak Country-original documentation and figure expression. CoCoRaHS source observations remain independently under **CC BY 3.0**. Underlying public-domain U.S. federal facts are not relicensed; other third-party rights are not conveyed. All Peak Country business names, shields, logos and brand identifiers remain reserved. Factual publisher identification is permitted, not implied endorsement. See `LICENSE`, `RIGHTS.md`, `ATTRIBUTION.md`, and `figures/FIGURE_REUSE.md` before reuse. Publisher credit does not claim ownership of original weather-source observations.

## Publication and citation status

Version 1.0.0 was first published on October 11, 2026 in the public GitHub repository at https://github.com/brandonmorrow365-netizen/peak-country-northern-colorado-hail-data and is identified by the immutable tag `v1.0.0`. Use `CITE_THIS_DATASET.md`. No DOI has been assigned; do not infer one from the GitHub release.
