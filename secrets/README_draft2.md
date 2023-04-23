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

Create an instance of the DraftKingsClient class:

```python
>>> import draftkings-api
>>> client = DraftKingsClient()
```

Using the client, get upcoming NBA contests:

```python
>>> contests = client.get_contests(sport='NBA')
>>> print([c.n for c in contests])
```

Get the details of one of the contests from the list:

```python
>>> contest = client.get_contest_detail(contests[0].id)
>>> print(contest.name)
```

Get the draftable players from the contest in JSON format.

```python
>>> draftables = client.get_draftables(draft_group_id=contest.draft_group_id, as_json=True)
>>> print(draftables)
```
