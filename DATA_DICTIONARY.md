# Data Dictionary: SpaceX Falcon 9 First-Stage Landing Prediction

This document describes the main tracked datasets and feature groups present in the repository. It focuses on fields that can be verified from the repository artifacts and notebook workflow.

## Dataset Inventory

| File | Role | Notes |
|---|---|---|
| `dataset_part_1.csv` | launch-level source snapshot | 94 rows x 17 columns tracked in repo |
| `dataset_part__3.csv` | engineered modeling matrix snapshot | 90 rows x 80 numeric columns tracked in repo |
| `spacex_launch_dash.csv` | dashboard input file | 56 rows x 7 columns tracked in repo |

Several notebooks also load IBM-hosted course CSVs such as `dataset_part_2.csv`, `dataset_part_3.csv`, `Spacex.csv`, and `spacex_launch_geo.csv`. Those external assets are part of the preserved academic workflow but are not all tracked locally in this repository.

## `dataset_part_1.csv` Columns

| Column | Description |
|---|---|
| `FlightNumber` | Sequential Falcon launch number used in the notebook workflow |
| `Date` | Launch date |
| `BoosterVersion` | Booster / vehicle version label |
| `PayloadMass` | Payload mass in kilograms |
| `Orbit` | Target orbit category |
| `LaunchSite` | Launch site name |
| `Outcome` | Original landing-outcome text used to derive the binary target |
| `Flights` | Number of booster flights at the time of launch |
| `GridFins` | Whether grid fins were used |
| `Reused` | Whether the booster had flown previously |
| `Legs` | Whether landing legs were present |
| `LandingPad` | Landing-pad identifier when available |
| `Block` | Falcon block / version generation field |
| `ReusedCount` | Count of prior reuses recorded in the dataset |
| `Serial` | Booster serial identifier |
| `Longitude` | Launch-site longitude |
| `Latitude` | Launch-site latitude |

### Derived target used in notebooks
The wrangling notebook creates a binary `Class` label from `Outcome`:
- `1` = successful landing outcome
- `0` = unsuccessful / non-successful outcome

That `Class` target is the label used later in the EDA and modeling notebooks.

## `dataset_part__3.csv` Feature Groups

`dataset_part__3.csv` is an already engineered numeric feature matrix used for classification. It contains:

### Base numeric features
- `FlightNumber`
- `PayloadMass`
- `Flights`
- `GridFins`
- `Reused`
- `Legs`
- `Block`
- `ReusedCount`

### One-hot encoded orbit features
Examples include:
- `Orbit_GTO`
- `Orbit_ISS`
- `Orbit_LEO`
- `Orbit_SSO`
- `Orbit_VLEO`

### One-hot encoded launch-site features
- `LaunchSite_CCAFS SLC 40`
- `LaunchSite_KSC LC 39A`
- `LaunchSite_VAFB SLC 4E`

### One-hot encoded landing-pad features
Examples include:
- `LandingPad_5e9e3032383ecb267a34e7c7`
- `LandingPad_5e9e3032383ecb554034e7c9`
- `LandingPad_5e9e3033383ecbb9e534e7cc`

### One-hot encoded booster serial features
Examples include:
- `Serial_B0003`
- `Serial_B1008`
- `Serial_B1049`
- `Serial_B1062`

### Boolean hardware indicator features
- `GridFins_False`
- `GridFins_True`
- `Reused_False`
- `Reused_True`
- `Legs_False`
- `Legs_True`

## `spacex_launch_dash.csv` Columns

| Column | Description |
|---|---|
| unnamed index column | Preserved CSV index from the original dashboard data export |
| `Flight Number` | Launch number used by the Dash app |
| `Launch Site` | Launch site label used in the dropdown filter |
| `class` | Binary recovery-outcome label used in plots (`1` = successful landing, `0` = unsuccessful landing or no successful recovery) |
| `Payload Mass (kg)` | Payload mass filter and scatter-plot x-axis |
| `Booster Version` | Raw booster label used in hover data |
| `Booster Version Category` | Grouped booster category used for scatter-plot color |

## Modeling Caveats Tied to the Data

- The tracked modeling matrix is small: 90 rows.
- The saved notebook scales the full feature matrix before splitting, so evaluation is not strictly leakage-free.
- Because launches occur over time, `FlightNumber`, `Flights`, and `ReusedCount` should be interpreted as historically accumulating variables rather than timeless features.
- The presence of many serial and location dummy variables can improve retrospective classification while reducing portability to new data.

## Dashboard Caveats

The dashboard dataset is a compact teaching dataset intended for interactive filtering and visualization, not a full reproduction of every launch record used in the notebooks.
