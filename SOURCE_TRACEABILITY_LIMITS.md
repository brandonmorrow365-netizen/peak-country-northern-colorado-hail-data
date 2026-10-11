# Source traceability and reproducibility — scope and known gap

Peak Country's scientific standard is transparent about **what can and cannot currently be reconstructed by an independent reader**.

## What can be verified from the current public release

1. Version 1.0.0 contains **1,844 confirmed ground-observation lineages**, each with a stable publisher `observation_id`, date, county, reported magnitude, coordinates, method/quality flags and source *role*.
2. The conservative `data/event-group-membership.csv` connects observation IDs with **1,119** event groups. A group is not a unique storm.
3. `sources/source-manifest.json` and `sources/source-retrieval-details.json` list verified official source families, acquisition URLs and archive metadata (including dated 2016–2025 NCEI sources, verified CoCoRaHS pages, SPC candidates and Census QA).
4. `SHA256SUMS.txt` verifies distributed bytes; `DATA_DICTIONARY.md` defines the 34 public fields. The canonical `METHODOLOGY.md` documents time, spatial and lineage decisions.

## What is not yet present

The 34-field public master **does not expose a direct official-source event ID, link or per-observation source-record crosswalk**. A source-role category is not a row-level original citation. Consequently, a person cannot trace *every* individual observation to its precise original official record using only this public package. Do **not** label this package “fully record-level reproducible.”

Private staging maintains source lineage records (including upstream record keys), but the frozen public projection explicitly marks direct source-key fields as excluded from the public export. They must not be copied into a public crosswalk without a separate visibility, privacy and source-rights approval under project governance.

## Recommended separate approval and quality gates

A follow-up source-reference sidecar could, **if approved**, publish `observation_id`, source role, eligible official archive reference, original public source ID where permitted and change notice. Before release: (a) rights review per source family, (b) privacy check, (c) null/ambiguous/provisional source status review, (d) automated 1:many lineage reconciliation and 1,844-ID cardinality tests, (e) reviewer sign-off, and (f) versioned publication. Do not infer missing links from coordinates, date or matching hail sizes.

Researchers may already reproduce the **included published values** and aggregation logic using the [research quickstart](RESEARCHER_START_HERE.md) and [methodology](METHODOLOGY.md), but that is different from verifying original source lineage record-by-record.
