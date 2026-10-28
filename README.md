# Formula 1 Race Intelligence Dashboard (2010-2026)

University project: Tableau dashboard + 9-scene story, published to Tableau Public and embedded in a Flask web app.

## Project Links (one each for the whole project)
- **Demo Link:** _to be added_
- **GitHub Link:** _to be added_

## Folder structure
```
data/        F1_Racing_Project_Dataset.xlsx (source data, unchanged)
scripts/     validate_data.py   (checks data + prints expected values)
docs/        TABLEAU_BUILD_GUIDE.md, STORY_SCENES.md, PERFORMANCE_TEST_LOG.md,
             PUBLISH_AND_EMBED.md, data_validation_report.txt
templates/   Flask HTML pages        static/  style.css
app.py       Flask app               requirements.txt
```

## Parts
| Part | Where |
|---|---|
| 1 Data collection | docs/TABLEAU_BUILD_GUIDE.md (Part 1) |
| 2 Data preparation | docs/TABLEAU_BUILD_GUIDE.md (Part 2), docs/data_validation_report.txt |
| 3 Visualizations (9) | docs/TABLEAU_BUILD_GUIDE.md (Part 3) |
| 4 Dashboard | docs/TABLEAU_BUILD_GUIDE.md (Part 4) |
| 5 Story (9 scenes) | docs/STORY_SCENES.md |
| 6 Performance testing | docs/PERFORMANCE_TEST_LOG.md |
| 7 Web integration | docs/PUBLISH_AND_EMBED.md, app.py |
| 8 Demonstration & documentation | Not started (waiting for instructions) |

## Run the web app
```
pip install -r requirements.txt
python app.py
```
Then open http://127.0.0.1:5000. Add your Tableau Public URLs in `app.py` first.

## Data notes
- 5 sheets, 13,748 rows. `race_results` has 6,464 rows and 42 columns.
- KPIs: 10 teams, 17 seasons, 6,464 outcomes, 24 circuits raced (29 listed in the circuits sheet).
- Year filter uses `season`. 2026 is a partial season (12 races). Carlos Sainz has two rows per race in the source and was kept.
- The qualifying sheet has placeholder driver/team names, so it is loaded but not used in charts.
