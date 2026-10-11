# Summaries — interpretation and MRMS coverage

The CSVs in this folder summarize the approved ground-observation dataset, geographic subsets and event memberships. Annual counts, observation counts, event groups and hail days have different denominators; none alone is a frequency trend or property-risk estimate.

## Radar-positive columns: essential adjacent coverage notice

In `annual-summary.csv`, `hail-day-summary.csv`, `county-summary.csv`, `monthly-climatology.csv` and other tables containing `radar_positive`, interpret the value only as **MRMS/MESH contextual association**, **not confirmed hail on the ground**. Project MRMS archive coverage is **unavailable in 2016–2019** (blanks are unavailable, not zero), **partial in 2020 beginning October 14, 2020**, and archive-available in **2021–2025** (availability does not guarantee full observation sampling). Comparisons between earlier and later radar-positive counts across the coverage break are invalid without accounting for coverage.

For scale, the master dataset has **196 radar-positive contextual associations** over its covered observation set; scope values recorded in T11-C2 are Weld **153**, Larimer **43**, and Greeley 25-mile **106**. The Greeley subset overlaps counties, so do not add that figure to the county figures.

Source-specific methodology and availability are recorded in `../metadata/summary-metadata.json` and `../sources/source-manifest.json`. Ground size thresholds are nested: at least 1 inch **588**, at least 1.5 inches **238**, and at least 2 inches **65**; these are not mutually exclusive or radar estimates.
