# Public data dictionary — V1.0.0

Only the **34 approved PUBLIC observation fields** in the CSV/JSON/GeoJSON/Parquet master and the three CSV subsets appear below. Definitions are taken from the approved T06 data dictionary and checked against the T12 public projection field map. Non-public and metadata-only staging fields are excluded. Null is not zero.

| Column | Definition | Logical type | Nullable | Units |
|---|---|---|---|---|
| `observation_id` | Stable Peak Country identifier for one underlying ground/reporting observation lineage. | string | NO | — |
| `identity_status` | Current lifecycle state of the observation identity. | enum | NO | — |
| `event_date_local` | Local calendar date used for annual/monthly/hail-day reporting. | date | YES | — |
| `observation_time_local` | Canonical source-local observation timestamp without inventing an offset. | datetime_local | YES | — |
| `observation_time_utc` | Canonical observation timestamp normalized to UTC only when source timezone can be resolved deterministically. | datetime | YES | — |
| `time_normalization_status` | Explains whether the canonical local time could be normalized reliably to UTC. | enum | NO | — |
| `year` | Reporting year derived from event_date_local. | integer | YES | year |
| `month` | Reporting month number derived from event_date_local. | integer | YES | month |
| `state_name` | Normalized state name for V1 observation geography. | string | YES | — |
| `state_fips` | Two-character state FIPS preserving leading zeroes. | string | YES | — |
| `county_name` | Approved county name used for V1 observation classification. | string | YES | — |
| `county_fips` | Three-character county FIPS preserving leading zeroes. | string | YES | — |
| `county_geoid` | Five-character state+county GEOID. | string | YES | — |
| `geographic_classification_status` | Agreement/conflict state between source and derived geography. | enum | NO | — |
| `latitude` | Approved usable observation latitude for coordinate-dependent derived outputs. | number | YES | degrees |
| `longitude` | Approved usable observation longitude for coordinate-dependent derived outputs. | number | YES | degrees |
| `coordinate_status` | Usability/availability state for observation coordinates. | enum | NO | — |
| `canonical_reported_location` | Location wording from the canonical source representation, preserved as source-derived display context. | string | YES | — |
| `normalized_display_location` | Optional cleaned display/community label that does not claim city-limit membership. | string | YES | — |
| `hail_magnitude_inches` | Canonical role-specific hail magnitude in inches; never an average of conflicting source values. | decimal | YES | in |
| `measurement_status` | Nature of the canonical measurement/assertion. | enum | NO | — |
| `canonical_source_role` | Role of the canonical source representation for this observation. | enum | NO | — |
| `evidence_class` | Observation-level evidence summary class. | enum | NO | — |
| `independent_supporting_observation_count` | Number of other confirmed independent ground-observation lineages associated with the same event group under T03/T09 rules. | integer | YES | count |
| `independent_corroboration_status` | Whether independent supporting ground observations are established. | enum | NO | — |
| `radar_context_status` | Whether MRMS/MESH context is associated separately from ground observations. | enum | NO | — |
| `conflict_status` | Summary state indicating whether material source conflicts remain for this observation. | enum | NO | — |
| `duplicate_candidate_status` | Summary state for unresolved/resolved duplicate-candidate relationships. | enum | NO | — |
| `distance_from_greeley_miles` | WGS84 ellipsoidal distance from frozen Lincoln Park reference, in statute miles. | decimal | YES | statute_mile |
| `greeley_25mi_status` | Eligibility for the derived Greeley 25-mile subset. | enum | NO | — |
| `distance_bin` | Descriptive distance band under T05 semantics. | enum | NO | — |
| `quality_flags` | Sorted controlled public-safe quality/limitation codes derived from issues. | array[string] | NO | — |
| `dataset_version` | Dataset release version containing this row. | string | NO | — |
| `methodology_version` | Methodology version used to derive this row. | string | NO | — |

Interpretation: observation IDs identify source reporting lineages, not unique storms; event-group memberships and unique hail days are separate concepts. Radar context is not independently confirmed ground hail. Coordinates are WGS84; the 25-mile Greeley subset uses the neutral Lincoln Park methodology reference, not a business address or city boundary. See `METHODOLOGY.md`, `LIMITATIONS.md`, and `summaries/README.md`.
