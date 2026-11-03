def calculate_standings(teams, fixtures):
    """Calculate and return tournament standings."""

    table = {}

    # Give every team starting statistics.
    for team in teams:
        table[team["id"]] = {
            "team_id": team["id"],
            "name": team["name"],
            "played": 0,
            "wins": 0,
            "draws": 0,
            "losses": 0,
            "goals_for": 0,
            "goals_against": 0,
            "goal_difference": 0,
            "points": 0
        }

    # Process completed fixtures only.
    for fixture in fixtures:
        if fixture["status"] != "played":
            continue

        home = table[fixture["home_id"]]
        away = table[fixture["away_id"]]

        home_score = fixture["home_score"]
        away_score = fixture["away_score"]

        home["played"] += 1
        away["played"] += 1

        home["goals_for"] += home_score
        home["goals_against"] += away_score

        away["goals_for"] += away_score
        away["goals_against"] += home_score

        if home_score > away_score:
            home["wins"] += 1
            away["losses"] += 1
            home["points"] += 3

        elif home_score < away_score:
            away["wins"] += 1
            home["losses"] += 1
            away["points"] += 3

        else:
            home["draws"] += 1
            away["draws"] += 1
            home["points"] += 1
            away["points"] += 1

    # Calculate goal difference.
    for team in table.values():
        team["goal_difference"] = (
            team["goals_for"] - team["goals_against"]
        )

    # Apply tournament ranking rules.
    standings = sorted(
        table.values(),
        key=lambda team: (
            -team["points"],
            -team["goal_difference"],
            -team["goals_for"],
            team["name"].casefold()
        )
    )

    return standings


def get_champion(teams, fixtures):
    """Return the champion only when every fixture is completed."""

    if not fixtures:
        return None

    if any(fixture["status"] != "played" for fixture in fixtures):
        return None

    standings = calculate_standings(teams, fixtures)

    return standings[0]
