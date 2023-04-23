# draftkings-api

A Python wrapper around the DraftKings API.

🚧 This package and documentation are under construction 🚧

# Installing

Install draftkings-api using pip:

```shell
$ pip install draftkings-api
```

# Models

This library utilizes models to represent various data structures returned by DraftKings. Those models are:

- Competition
- Contest
- Draftable
- DraftGroup
- GameSet
- GameStyle
- GameType
- Sport

# Usage

```python
import draftkings-api


client = DraftKingsClient()

# Get upcoming NBA contests
contests = client.get_contests(sport='NBA')

if len(contests) == 0:
    raise Exception('No upcoming contests found')

# Get details of the first contest in the list
contest = client.get_contest_detail(contests[0].id)

# Get the draftable players from the contest in JSON format.
draftables = client.get_draftables(
    draft_group_id=contest.draft_group_id,
    as_json=True
)
```
