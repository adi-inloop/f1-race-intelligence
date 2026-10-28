"""Part 1-2: validate the dataset and print expected values to compare with Tableau.
Run from the project folder:  python scripts/validate_data.py
Writes docs/data_validation_report.txt"""
import io
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
XLSX = ROOT / "data" / "F1_Racing_Project_Dataset.xlsx"
OUT = ROOT / "docs" / "data_validation_report.txt"
buf = io.StringIO()
def p(*a): print(*a, file=buf)

sheets = pd.read_excel(XLSX, sheet_name=None)
r = sheets["race_results"]

p("=== 1. SHEETS AND SIZES ===")
total = 0
for n, d in sheets.items():
    p(f"{n:25s} rows={len(d):5d} cols={d.shape[1]}"); total += len(d)
p("Total rows:", total)

p("\n=== 2. race_results COLUMN TYPES (what Tableau should show) ===")
for c, t in r.dtypes.items():
    if c == "race_date": tab = "Text in Excel -> change to Date in Tableau"
    elif str(t).startswith("float"): tab = "Number (decimal)"
    elif str(t).startswith("int"): tab = "Number (whole)"
    else: tab = "String"
    p(f"{c:22s} {str(t):8s} -> {tab}")
p("Column count:", r.shape[1])

p("\n=== 3. NULL CHECK (race_results) ===")
p(r.isna().sum()[r.isna().sum() > 0].to_string())
p("DNF rows:", int(r.dnf.sum()),
  "| DNF rows with finish_position null:", int(((r.dnf == 1) & r.finish_position.isna()).sum()),
  "| DNF rows missing reason:", int(((r.dnf == 1) & r.dnf_reason.isna()).sum()))
p("Duplicate rows:", int(r.duplicated().sum()))

p("\n=== 4. KPI VALUES ===")
p("Competing Teams     :", r.team.nunique())
p("Seasons in Play     :", r.season.nunique())
p("Race Outcomes Logged:", len(r))
p("Circuits Raced      :", r.circuit_id.nunique(), "(circuits sheet lists", len(sheets["circuits"]), ")")

p("\n=== 5. KNOWN DATA NOTES ===")
d = pd.to_datetime(r.race_date)
p("Rows where race_date year != season:", int((d.dt.year != r.season).sum()), "-> use season for the Year filter")
p("Carlos Sainz rows per race:", int(r[r.driver == "Carlos Sainz"].groupby("race_id").size().max()), "(kept as-is)")
p("Races in 2026:", r[r.season == 2026].race_id.nunique(), "(partial season)")

p("\n=== 6. EXPECTED VALUES FOR TABLEAU CHECKS (no filters applied) ===")
p("\nTop 10 drivers by total points:")
p(r.groupby("driver").points.sum().sort_values(ascending=False).head(10).to_string())
p("\nTotal points by team:")
p(r.groupby("team").points.sum().sort_values(ascending=False).to_string())
p("\nDNFs by reason:")
p(r[r.dnf == 1].dnf_reason.value_counts().to_string())
p("\nDNFs by driver (top 5):")
p(r.groupby("driver").dnf.sum().sort_values(ascending=False).head(5).to_string())
p("\nStarting compound share (%):")
p((r.starting_compound.value_counts(normalize=True) * 100).round(1).to_string())
p("\nRace rows by country (top 6):")
p(r.country.value_counts().head(6).to_string())
pod = r[r.finish_position <= 3]
p("\nTotal podium finishes:", len(pod))
p("Podiums by team:"); p(pod.team.value_counts().to_string())
p("Podiums by driver (top 5):"); p(pod.driver.value_counts().head(5).to_string())
p("\nRed Bull vs Mercedes points (every 4th season):")
t = r[r.team.isin(["Red Bull Racing", "Mercedes"])].groupby(["season", "team"]).points.sum().unstack()
p(t.iloc[::4].to_string())

OUT.write_text(buf.getvalue(), encoding="utf-8")
print(buf.getvalue())
