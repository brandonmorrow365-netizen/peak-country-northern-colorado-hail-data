# Methodology — Northern Colorado hail history V1.0.0

**Status:** published version 1.0.0 (2026-10-11). **Period:** 2016–2025. **Scope:** Weld County (GEOID 08123) and Larimer County (GEOID 08069), Colorado. This describes the approved method, not newly calculated results.

## Provenance, precedence and observations
NOAA/NCEI Storm Events is the canonical finalized historical backbone. NWS Local Storm Reports remain preliminary/reference; SPC hail reports may derive from NWS and do not count as independent corroboration for matching reports. CoCoRaHS supplies supplemental ground observations; source redistribution remains subject to independently applicable CC BY 3.0 attribution and change notices. Raw mPING is excluded/not used. A source representation, a stable Peak Country observation ID and a meteorological event-group ID are distinct identities. Same-lineage republications are not double-counted, and conflicting sources are not averaged.

T09 documented 1,844 active confirmed observation lineages (773 Weld, 1,071 Larimer), 29 review-required provisional identities excluded from confirmed counts, one merged alias excluded, and 1,119 conservative event groups. The independently corroborated ground-observation count is 864; conservative association limits should not be interpreted as exhaustive storm tracking. A hail day is a unique local calendar date with a confirmed report in the specified scope; it is not synonymous with an observation or event group.

## Geographic method
Weld/Larimer master membership is county-based, with source classification and independent 2026 U.S. Census TIGER/Line County polygon QA. Source locality labels do not imply municipality membership. The Greeley 25-statute-mile subset uses the WGS84 inverse geodesic from fixed Peak Country-selected neutral Lincoln Park, Greeley reference latitude 40.424896787198563, longitude -104.69350052421541. Include distances ≤ 40,233.6 meters at full precision. This point is neither a business/customer address nor a City GIS dataset. No City of Greeley GIS source material is used. The geographic subset contains 1,064 observations and overlaps the county subsets; do not add it to the county totals.

## Radar and source availability
MRMS `CONUS/MESH_00.50` contributes radar-derived context, not ground hail evidence. T09 matching uses nearest eligible time within five minutes and the nearest regular_ll 0.01-degree grid cell; MESH millimeters are converted to inches using 25.4 mm per inch. The project had no MRMS archive for 2016–2019; 2020 is partial beginning 2020-10-14; archived coverage is available 2021–2025 without guaranteeing complete sampling. Unavailable is not zero, a sampled no-signal does not establish no hail, and MRMS does not change source-reported ground hail magnitude.

## Publication projection and statistics
One T06-approved authoritative model produces one 34-field public projection in CSV, JSON, GeoJSON and Parquet and three geographic subset CSVs. Outputs must not be hand-edited separately. The nine summary tables and five figure pairs present descriptive counts; they do not establish climatic trends, property-specific hail occurrence, or vehicle damage.

For each public field see `DATA_DICTIONARY.md`. Source rights, retrieval evidence, known gaps, and correction policies are in `SOURCE_PROVENANCE.md`, `sources/source-retrieval-details.json`, `LIMITATIONS.md` and `CORRECTIONS.md`. Original implementation logs, staging and restricted archives are not distributed.
