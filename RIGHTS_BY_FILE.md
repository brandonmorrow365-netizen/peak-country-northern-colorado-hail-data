# Source-specific rights and reuse matrix — v1.0.0

**Published rights guide for version 1.0.0. Not legal advice and not a blanket sublicense of original weather reports.** Publisher: [Peak Country Auto Hail Repair & Paintless Dent Repair](https://peakcountryhail.com/).

| Content or files | Original source / creator | Applicable rights notice | What a reuser must do |
|---|---|---|---|
| `data/` master formats and county/25-mile CSV subsets | Compilation by Peak Country from NOAA/NCEI and separately credited supplemental sources | **Source-specific rights survive normalization**. NOAA U.S. federal public-domain facts are not owned or relicensed. CoCoRaHS observation contributions remain under **CC BY 3.0**. Only protectable Peak Country compilation rights, if any, are made available under ODC-By 1.0 | Cite Peak Country for assembly/method; preserve source network credit and its applicable CC BY 3.0 license/change notice. Do not present one license as covering every underlying row |
| `data/event-group-membership.csv` | Peak Country conservative grouping, based on source observations | Any protectable original compilation/arrangement rights under **ODC-By 1.0**; source facts retain independent status | Credit grouping methodology; do not call groups unique storms |
| `summaries/*.csv` | Peak Country aggregation of the dataset | Underlying counted facts not exclusively owned; protectable original database arrangement rights, if any, follow **ODC-By 1.0** | Cite data source and methodology; preserve original-source notices |
| `figures/*.png`, `figures/*.svg`, chart captioning and original illustration expression | Peak Country-created figures from the compiled observations | Protectable original expression under **CC BY 4.0** where applicable; weather facts not relicensed; Peak Country trademarks/shield **reserved** | Credit chart publisher, distinguish source observations, honor source-layer rights; no brand endorsement implied |
| `README.md`, methodology, guides, definitions, citations and authored explanations | Peak Country-authored prose/selection | **CC BY 4.0 only for protectable Peak Country-original expression** | Give appropriate authorship credit and link to license; cite third-party quotes or source data separately |
| `sources/source-manifest.json`, `sources/source-retrieval-details.json` and equivalents | Public-source identifiers/URLs, retrieval metadata and Peak Country organization | Source facts/metadata are not automatically owned; any separately protectable organization remains scoped as above | Keep provenance intact. Archive response checksums are NOT a redistribution grant |
| `metadata/*.json`, Schema.org, DCAT, Data Package and checksum files | Publication and integrity metadata | Metadata describes files and rights; it does **not** grant ownership of original third-party content | Use the declared provenance and rights matrix |
| Peak Country company name, shield, logos, branding and identifiers | Peak Country | **Trademark and related rights reserved**, outside both content and compilation licenses | Factual publisher identification is acceptable; don't imply endorsement, co-brand, or claim ownership of trademarks |

## Original sources and the CoCoRaHS boundary

- **NOAA/NCEI Storm Events** — finalized federal reporting backbone; underlying weather facts are public-domain U.S. federal information. Report limitations still apply.
- **NWS/NOAA/SPC** — preliminary or derivative weather reports; treat repeated republishing of the same observation as one lineage, not independent confirmation.
- **CoCoRaHS** — supplemental ground hail observations remain independently under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) with appropriate source attribution, a license link and an explanation that Peak Country normalized/harmonized source data. Do not extend CC BY 4.0 to source records or assume supplied images are included.
- **MRMS/MESH** — radar context, not a confirmed ground report.
- **Census TIGER/Line** — county-boundary QA, not weather data.
- **mPING** — raw source excluded (NOT_USED).

Read `LICENSE`, `LICENSE-DATA`, `LICENSE-CONTENT`, `RIGHTS.md`, `ATTRIBUTION.md`, `SOURCE_PROVENANCE.md` and `TRADEMARKS.md`. Official terms: [ODC-By 1.0](https://opendatacommons.org/licenses/by/1-0/), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), [CoCoRaHS CC BY 3.0](https://creativecommons.org/licenses/by/3.0/). The source-specific original license and third-party rights take precedence over any generalized top-level metadata label.

**Release gate:** The exact copyright/license field selected by an archive service such as Zenodo must be checked for multi-source accuracy at T18; do not choose one license and imply it covers all original source rows. An independent legal review is recommended if broad downstream redistribution will be encouraged.
