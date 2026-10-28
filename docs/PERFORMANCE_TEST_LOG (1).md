# Part 6 - Performance Testing Log

Rows marked "seen in screenshot" were checked against screenshots of the Tableau workbook during the build.
Rows marked **TO TEST** have NOT been tested yet. Fill them in yourself after testing in Tableau. Do not mark a test as passed unless you did it.

## Test setup
- Extract mode used: [x] yes (data source set to Extract)
- Rows: race_results 6,464 (42 columns); all sheets 13,748 rows
- Calculated fields: DNF Count, DNF Reason (Filter), Points Cumulative, Driver Rank, Podium, Top N Filter, plus 4 KPI fields (Competing Teams, Seasons in Play, Race Outcomes Logged, Circuits Raced)
- Parameter: Top N (integer, default 10)
- Visualizations: 9 sheets on the dashboard
- Filters: DNF Reason (Filter), Season (Year of Race), Top N

## 1. KPI validation
| KPI | Expected | Tableau shows | Pass? |
|---|---|---|---|
| Competing Teams | 10 | 10 (seen in screenshot) | Yes |
| Seasons in Play | 17 | 17 (seen in screenshot) | Yes |
| Race Outcomes Logged | 6,464 | 6,464 (seen in screenshot) | Yes |
| Circuits Raced | 24 | 24 (seen in screenshot) | Yes |

## 2. Chart checks (no filters)
| Chart | Expected | Tableau shows | Pass? |
|---|---|---|---|
| Leaderboard #1 | Verstappen 4,640 | 4,640 first bar (seen in screenshot) | Yes |
| Leaderboard bars at Top N = 10 | 10 bars | 10 bars (seen in screenshot) | Yes |
| Team Ranking #1 | Red Bull Racing 8,006 | 8,006 (seen in screenshot) | Yes |
| Reliability total | 396 | 396 (status bar, seen in screenshot) | Yes |
| Tyre Pie Soft | 29.2% | 29.22% (seen in screenshot) | Yes |
| Country Bahrain | 2,168 | **TO TEST** | |
| Podium total | 940 | **TO TEST** | |

## 3. Filter tests
| Test | Expected | Result | Pass? |
|---|---|---|---|
| Top N = 5 | 5 bars | **TO TEST** | |
| Top N = 19 | 19 bars | **TO TEST** | |
| Year = 2026 only | 240 race rows | **TO TEST** | |
| Year = 2010 only | 324 race rows | **TO TEST** | |
| DNF Reason = Engine only | Reliability shows 73 | **TO TEST** | |
| Year filter changes Team Championship | Chart updates | **TO TEST** | |
| Clear all filters | Back to Section 2 values | **TO TEST** | |
| Two filters combined, no inflated totals | | **TO TEST** | |

## 4. Speed and layout (measure with a stopwatch)
| Item | Measured |
|---|---|
| Dashboard first load (Desktop), seconds | **TO TEST** |
| Filter change response, seconds | **TO TEST** |
| Dashboard load on Tableau Public, seconds | **TO TEST** (after publishing) |
| Layout OK at full / half screen | **TO TEST** |

## 5. Story check
| Item | Result |
|---|---|
| Number of scenes (required 9) | **TO TEST** (count the tabs) |

## 6. Problems found and fixes
| Problem | Cause | Fix |
|---|---|---|
| Relationship showed red warning when adding extra tables | Tableau relates every table dragged onto the canvas | Removed extra tables; unrelated tables now sit under Disconnected Tables |
| KPI values did not display | Fields were on Detail instead of Text | Moved fields to Text |
| Reliability chart overlapped the map | Sheet was floating | Set to Tiled and placed beside the map |
