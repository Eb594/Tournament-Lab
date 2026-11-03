import json
from pathlib import Path


def save_tournament(teams, fixtures, filepath="data.json"):
    """Save teams and fixtures to a JSON file."""

    data = {
        "schema_version": 1,
        "teams": teams,
        "fixtures": fixtures
    }

    path = Path(filepath)

    path.write_text(
        json.dumps(data, indent=4),
        encoding="utf-8"
    )


def load_tournament(filepath="data.json"):
    """Load and validate tournament data."""

    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError("Tournament data file was not found.")

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        raise ValueError("Tournament data file contains invalid JSON.")

    if not isinstance(data, dict):
        raise ValueError("Tournament data must be a JSON object.")

    if data.get("schema_version") != 1:
        raise ValueError("Unsupported tournament data version.")

    teams = data.get("teams")
    fixtures = data.get("fixtures")

    if not isinstance(teams, list) or not isinstance(fixtures, list):
        raise ValueError("Teams and fixtures must be lists.")

    if not 4 <= len(teams) <= 8:
        raise ValueError("Tournament must contain between 4 and 8 teams.")

    team_ids = set()
    team_names = set()

    for team in teams:
        if not isinstance(team, dict):
            raise ValueError("Invalid team data.")

        if not isinstance(team.get("id"), str):
            raise ValueError("Invalid team ID.")

        if not isinstance(team.get("name"), str):
            raise ValueError("Invalid team name.")

        name = team["name"].strip()

        if len(name) < 2 or len(name) > 30:
            raise ValueError("Invalid team name length.")

        if team["id"] in team_ids:
            raise ValueError("Duplicate team ID.")

        if name.casefold() in team_names:
            raise ValueError("Duplicate team name.")

        team_ids.add(team["id"])
        team_names.add(name.casefold())

    fixture_ids = set()
    played_pairs = set()

    for fixture in fixtures:
        if not isinstance(fixture, dict):
            raise ValueError("Invalid fixture data.")

        fixture_id = fixture.get("id")
        home_id = fixture.get("home_id")
        away_id = fixture.get("away_id")
        status = fixture.get("status")
        home_score = fixture.get("home_score")
        away_score = fixture.get("away_score")

        if not all(isinstance(value, str) for value in (
            fixture_id, home_id, away_id
        )):
            raise ValueError("Invalid fixture IDs.")

        if fixture_id in fixture_ids:
            raise ValueError("Duplicate fixture ID.")

        if home_id not in team_ids or away_id not in team_ids:
            raise ValueError("Fixture refers to an unknown team.")

        if home_id == away_id:
            raise ValueError("A team cannot play against itself.")

        pair = frozenset((home_id, away_id))

        if pair in played_pairs:
            raise ValueError("Duplicate team pairing.")

        played_pairs.add(pair)
        fixture_ids.add(fixture_id)

        if status == "pending":
            if home_score is not None or away_score is not None:
                raise ValueError("Pending fixtures cannot have scores.")

        elif status == "played":
            for score in (home_score, away_score):
                if type(score) is not int or score < 0:
                    raise ValueError("Invalid fixture score.")

        else:
            raise ValueError("Invalid fixture status.")

    expected_fixtures = len(teams) * (len(teams) - 1) // 2

    if fixtures and len(fixtures) != expected_fixtures:
        raise ValueError("Fixture list is incomplete.")

    return teams, fixtures