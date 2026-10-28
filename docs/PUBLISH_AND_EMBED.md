# Part 7 - Publish to Tableau Public and Embed in Flask

## A. Publish (do these in Tableau Desktop)
1. Check that the dashboard, story and 9 sheets work. Delete unused scratch sheets (keep `Cumulative Points`, it feeds Story scene 4).
2. **File -> Save to Tableau Public As...** and sign in (free account at public.tableau.com).
3. Name the workbook, e.g. `F1_Race_Intelligence`. The browser opens when it finishes.
4. In the browser, confirm: dashboard loads, filters and Top N work, the Story tab shows 9 scenes.
5. On the published page click **Share** and copy the link. Also copy the **Embed Code** (it contains `tableau-viz` and a `src="..."`).
6. Make sure the viz is **not hidden** (Tableau Public profile -> workbook settings -> Show/unhide).

Dashboard URL looks like: `https://public.tableau.com/views/<Workbook>/<Dashboard>`
Story URL looks like: `https://public.tableau.com/views/<Workbook>/<StoryName>`
Copy the `src` value from the embed code, but remove everything after a `?`.

## B. Connect to Flask
1. Open `app.py`. Paste the two URLs into `DASHBOARD_URL` and `STORY_URL`.
2. Run:
   ```
   pip install -r requirements.txt
   python app.py
   ```
3. Open http://127.0.0.1:5000 -> check Home, Dashboard, Story. Try the filters and Top N inside the embedded viz.
4. Needs internet, and the workbook must be public.

## C. Verify (fill in yourself)
| Check | Pass? |
|---|---|
| Dashboard embed loads | |
| Filters work inside the page | |
| Top N changes the leaderboard | |
| Story embed loads with 9 scenes | |
| Page is readable on a narrow window | |

If the embed is blank: check the URL, that the workbook is public, and your internet connection.
