# Tableau Build Guide (Parts 1-5)

Follow in order. Expected values come from `docs/data_validation_report.txt` (made by `scripts/validate_data.py`).
Decisions used: circuits KPI = 24, Year filter uses `season`, Sainz rows kept, qualifying sheet loaded but unused.

---
## Part 1 - Data Collection & Extraction
1. Open **Tableau Desktop -> Connect -> Microsoft Excel** -> choose `data/F1_Racing_Project_Dataset.xlsx`.
2. Drag `race_results` onto the canvas first, then `circuits`.
3. Relationship: `race_results` -> `circuits` on **circuit_id = circuit_id** (many-to-one). Do NOT drag other sheets into this data source (Tableau forces a relationship on every sheet you add).
3b. **Data -> New Data Source -> Microsoft Excel** (same file), drag only `championship_standings`, set it to **Extract**. This second source is used only for Sheet 6. `lap_intelligence` and `qualifying_results` are not needed for any chart.
4. In the data grid for `race_results`, check all **42 columns** (the brief says 41; the file has 42). Change:
   - `race_date` -> **Date** (it arrives as text)
   - `season`, `round` -> keep as numbers, then right-click `season` -> **Convert to Dimension**
5. Top right choose **Extract** (not Live). Click the sheet tab; Tableau asks where to save the `.hyper` file.

## Part 2 - Data Preparation
Do **not** delete rows. The 396 blank `finish_position` rows are DNFs and are kept.

**Calculated fields** (Analysis -> Create Calculated Field):

| Name | Formula |
|---|---|
| `DNF Count` | `SUM([dnf])` |
| `DNF Reason (Filter)` | `IFNULL([dnf_reason], "Finished")` |
| `Points Cumulative` | `RUNNING_SUM(SUM([points]))` -> set **Compute using: Round** (see Sheet 4b) |
| `Driver Rank` | `RANK_UNIQUE(SUM([points]))` |
| `Podium` | `IF [finish_position] <= 3 THEN 1 ELSE 0 END` |

Why `DNF Reason (Filter)`: finishers have a blank reason; without this the global filter would remove them from every chart.

**Parameter**: right-click in Data pane -> Create Parameter: name `Top N`, Integer, current value **10**, range 1 to 19 (step 1). Right-click -> **Show Parameter**.

**Gap handling**: `gap_to_leader_s` is blank only for DNFs. No chart in this project needs it. If you use it later, Tableau ignores nulls in averages automatically.

**Global filters** (add to each sheet, then right-click -> *Apply to Worksheets -> Selected Worksheets*, tick all sheets):
1. `DNF Reason (Filter)` - all values selected
2. `season` (label the filter "Year of Race") - all 17 seasons
3. `Top N` parameter

## Part 3 - The 9 Visualizations
Name each sheet exactly as shown. All use the `race_results` data source unless stated.

| # | Sheet name | Chart | How to build |
|---|---|---|---|
| 1 | `KPI Cards` | Text | Four text values: `COUNTD(team)` = 10, `COUNTD(season)` = 17, **Number of Records** = 6,464, `COUNTD(circuit_id)` = 24 (label it "Circuits Raced"). Build as one sheet with four measures, or four small sheets. |
| 2 | `Driver Map` | Map | Double-click `country` (it becomes a geographic field; fix unknowns via *Edit Locations*). Size = `COUNTD(driver)` or Number of Records, Color = Number of Records. Title: "Grand Prix Host Nations". |
| 3 | `Reliability` | Stacked bar | Filter `dnf` = 1. Columns = `DNF Count`, Rows = `driver`, Color = `dnf_reason`. Sort descending. |
| 4 | `Leaderboard` | Vertical bar | Columns = `driver`, Rows = `SUM(points)`. Drag `Driver Rank` to Filters -> *Range of values* -> use the parameter: create `Top N Filter` = `[Driver Rank] <= [Top N]`, put it on Filters, select **True**. Sort descending. |
| 4b | `Cumulative Points` | Line (used in Story scene 4) | Columns = `round`, Rows = `Points Cumulative`, Color = `driver`, filter one `season` (single value) and Top N drivers. Compute using **round**. |
| 5 | `Team Ranking` | Horizontal bar | Rows = `team`, Columns = `SUM(points)`, sort descending. |
| 6 | `Team Championship` | Grouped vertical bar | **Data source: `championship_standings`.** Columns = `season`, then `team` (this makes groups); Rows = `SUM(points)`; Color = `team`. To keep it readable filter to Red Bull Racing, Mercedes, Ferrari, McLaren. |
| 7 | `Tyre Pie` | Pie | Marks = Pie, Color = `starting_compound`, Angle = Number of Records, label = % of Total. |
| 8 | `Country Participation` | Treemap | Size and Color = Number of Records, Detail/Label = `country`. |
| 9 | `Podium Bubbles` | Packed bubble | Marks = Circle, Size = `SUM(Podium)`, Color = `team`, Detail/Label = `driver`. |

Tooltips: edit each tooltip to say what the number is (e.g. "<driver>: <SUM(points)> points").

**Sheet 6 and the Year filter.** `championship_standings` is a separate table, so the Year filter does not reach it by default. Fix: *Data -> Edit Blend Relationships* ensure `season = season`, then the filter can apply to it. If it does not work, build Sheet 6 from `race_results` instead (`SUM(points)` by `season` and `team`) - I verified standings points equal results points for every driver-season, so the values are identical.

**Check each sheet against the expected values** in `docs/data_validation_report.txt` (e.g. Verstappen 4,640 points, Red Bull 8,006, DNF Engine 73, podiums 940).

## Part 4 - Dashboard
1. New Dashboard, size **Automatic** (responsive) or Range min 1000 x 700 / max 1600 x 1200.
2. Dashboard -> Format -> Shading: **black (#000000)**. Text white; accent red **#E10600**.
3. Layout (use Horizontal and Vertical containers; set all sheets to **Fit -> Entire View**):

```
Row 0: [ Title banner "F1 RACE INTELLIGENCE 2010-2026" + car image ]
       [ KPI x4 ]            [ Year filter | DNF Reason filter | Top N ]
Row 1: [ Driver Map ]                [ Reliability ]
Row 2: [ Leaderboard ]               [ Team Ranking ]
Row 3: [ Team Championship ] [ Tyre Pie ] [ Country Participation ] [ Podium Bubbles ]
```
4. Add the race car image with the **Image** object (use your own or a free-licence image). Add a text object for the title in white bold.
5. Show filters from any one sheet (right-click filter -> *Apply to worksheets -> All Using This Data Source*), then place them in the top row.
6. Hide sheet titles you do not need; keep chart titles short. Use the same font (e.g. Tableau Bold) everywhere.
7. Dashboard -> Actions: add **Use as Filter** on `Driver Map` and `Team Ranking` if you want click-to-filter (optional).

## Part 5 - Story
Story -> New Story, size same as dashboard. Add **9 scenes** (click "Blank" for each), caption each:

See `docs/STORY_SCENES.md` for the exact titles, sheets and caption text.
